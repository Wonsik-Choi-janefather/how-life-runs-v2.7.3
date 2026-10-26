"""Structural audit of the EPI-Clone M.1-M.3 Seurat object, not an EPI-Clone rerun.

Usage: python audit.py /path/to/seurat_for_figshare.rds --out results
Dependency: rdata==1.1.0 (and its NumPy/pandas dependencies).
Source data: Scherer et al., Figshare doi:10.6084/m9.figshare.24204750.v2, CC BY 4.0.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import warnings

import numpy as np
import rdata


def run(path, out):
    out.mkdir(parents=True, exist_ok=True)
    digest = hashlib.md5(path.read_bytes()).hexdigest()
    assert path.stat().st_size == 173210114, 'Unexpected source size'
    assert digest == '0cc0bc53add7acb3aee39c673ff8adba', 'Unexpected source MD5'
    parsed = rdata.parser.parse_file(path, expand_altrep=True)
    with warnings.catch_warnings(record=True) as notes:
        warnings.simplefilter('always')
        obj = rdata.conversion.convert(parsed)
    # Unsupported S4 classes are preserved as namespaces, not silently discarded.
    m = getattr(obj, 'meta.data')
    assert m.index.is_unique and len(m) == 28782
    required = ['Experiment', 'ProcessingBatch', 'CellType', 'LARRY', 'LARRYSize']
    assert all(c in m.columns for c in required)
    assert m[['Experiment', 'ProcessingBatch', 'CellType']].notna().all().all()
    assays = getattr(obj, 'assays')
    matrices = {}
    for name, rows in [('DNAm',453), ('integrated',453), ('AB',20)]:
        a = assays[name]
        for slot in ['counts','data']:
            x = getattr(a, slot)
            if hasattr(x, 'Dim'):
                dims = list(map(int,x.Dim))
                if dims == [0,0]:
                    matrices[name+'.'+slot] = {'shape':dims, 'empty':True}
                    continue
                assert dims == [rows,len(m)]
                assert np.array_equal(np.asarray(x.Dimnames[1]).astype(str),np.asarray(m.index).astype(str))
                assert len(x.p)==len(m)+1 and x.p[0]==0 and x.p[-1]==len(x.x)==len(x.i)
                assert np.all(np.diff(x.p)>=0) and np.all((x.i>=0)&(x.i<rows))
                matrices[name+'.'+slot] = {'shape':dims,'stored_entries':len(x.x),
                    'nonfinite_stored_entries':int((~np.isfinite(x.x)).sum())}
            else:
                assert list(x.shape) == [rows,len(m)]
                assert np.array_equal(np.asarray(x.coords[x.dims[1]]).astype(str),np.asarray(m.index).astype(str))
                matrices[name+'.'+slot] = {'shape':list(x.shape),
                    'nonfinite_entries':int((~np.isfinite(x.values)).sum())}
    labeled=m.loc[m.LARRY.notna()].copy()
    assert labeled.LARRY.astype(str).str.len().gt(0).all()
    assert m.LARRY.notna().equals(m.LARRYSize.notna())
    observed=labeled.groupby('LARRY',observed=True).size()
    sizes=labeled.groupby('LARRY',observed=True).LARRYSize.agg(['nunique','first'])
    assert (sizes['nunique']==1).all()
    assert np.array_equal(sizes['first'].astype(int).values,observed.values)
    group_summary=[]
    for exp,g in m.groupby('Experiment',observed=True):
        lab=g[g.LARRY.notna()]
        group_summary.append({'experiment':str(exp),'cells':len(g),'labeled_cells':len(lab),
            'label_coverage':len(lab)/len(g),'barcodes':int(lab.LARRY.nunique()),
            'batches':int(g.ProcessingBatch.nunique())})
    cross_type=labeled.groupby('LARRY',observed=True).CellType.nunique()
    cross_batch=labeled.groupby('LARRY',observed=True).ProcessingBatch.nunique()
    antibody=np.asarray(assays['AB'].data.values)
    finite_antibody=np.isfinite(antibody)
    antibody_coverage=[]
    for exp in m.Experiment.unique():
        mask=(m.Experiment==exp).to_numpy(dtype=bool)
        a=finite_antibody[:,mask]
        antibody_coverage.append({'experiment':str(exp),'cells':int(mask.sum()),
            'cells_with_any_finite_antibody':int(a.any(axis=0).sum()),
            'cells_with_all_20_finite_antibodies':int(a.all(axis=0).sum()),
            'finite_entries':int(a.sum()),'total_entries':int(a.size)})
    reductions={}
    for name,v in getattr(obj,'reductions').items():
        e=getattr(v,'cell.embeddings')
        assert e.shape[0]==len(m)
        assert np.array_equal(np.asarray(e.coords[e.dims[0]]).astype(str),np.asarray(m.index).astype(str))
        reductions[str(name)]=list(e.shape)
    result={'audit_version':'0.1','audit_date':'2026-10-26','input_size':path.stat().st_size,
        'input_md5':digest,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'python':platform.python_version(),'rdata':rdata.__version__,
        'metadata_shape':list(m.shape),'metadata_columns':list(map(str,m.columns)),
        'labeled_cells':len(labeled),'barcodes':len(observed),'size_consistency_passed_barcodes':len(sizes),
        'experiments':group_summary,'matrices':matrices,'reductions':reductions,
        'barcodes_in_multiple_cell_types':int((cross_type>1).sum()),
        'barcodes_in_multiple_processing_batches':int((cross_batch>1).sum()),
        'antibody_coverage':antibody_coverage,
        'conversion_warnings':sorted(set(str(w.message) for w in notes)),
        'scope':'Structural and metadata audit only; no AUC/ARI reproduction or causal memory test.'}
    (out/'audit_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    # Derived records retain original identifiers. Missing labels are excluded, not treated as clones.
    labeled.rename_axis('cell_id').reset_index()[['cell_id']+required].to_json(
        out/'cell_lineage.jsonl',orient='records',lines=True,force_ascii=False)
    clone_rows=[]
    for barcode,g in labeled.groupby('LARRY',observed=True):
        clone_rows.append({'LARRY':str(barcode),'observed_cells':len(g),
            'reported_LARRYSize':int(g.LARRYSize.iloc[0]),'cell_types':sorted(map(str,g.CellType.unique())),
            'processing_batches':sorted(map(str,g.ProcessingBatch.unique()))})
    with (out/'clone_summary.jsonl').open('w') as f:
        for row in clone_rows: f.write(json.dumps(row,ensure_ascii=False)+'\n')
    # A second extraction directly from the parsed metadata checks conversion-independent counts.
    def deref(x):
        return x.referenced_object if getattr(x,'referenced_object',None) is not None else x
    def symbol(x):
        x=deref(x)
        return deref(x.value).value.decode() if x.info.type.name=='SYM' else None
    def attrs(x):
        a=x.attributes; d={}
        while a is not None and a.info.type.name=='LIST':
            d[symbol(a.tag)]=a.value[0]; a=a.value[1]
        return d
    raw_meta=attrs(parsed.object)['meta.data']
    raw_names=[deref(x).value.decode() for x in attrs(raw_meta)['names'].value]
    raw_larry=raw_meta.value[raw_names.index('LARRY')]
    raw_vals=[deref(x).value for x in raw_larry.value]
    nonmissing=[v for v in raw_vals if v is not None]
    independent={'raw_metadata_rows':len(raw_vals),'raw_labeled_cells':len(nonmissing),
        'raw_unique_barcodes':len(set(nonmissing))}
    assert independent['raw_labeled_cells']==len(labeled)
    assert independent['raw_unique_barcodes']==len(observed)
    (out/'raw_parser_check.json').write_text(json.dumps(independent,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    print('RAW_PARSER_CHECK',independent)


if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('rds',type=Path); p.add_argument('--out',type=Path,default=Path('results'))
    a=p.parse_args(); run(a.rds,a.out)
