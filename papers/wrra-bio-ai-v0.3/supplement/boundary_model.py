"""Illustrative capacities and costs; not measurements or actual gene counts."""
import itertools,json
from pathlib import Path
def enumerate_boundary(import_allowed):
    rows=[]
    for synthesis,transporter in itertools.product((0,1),repeat=2):
        capacity=synthesis+transporter*import_allowed
        rows.append(dict(synthesis=synthesis,transporter=transporter,cost=3*synthesis+transporter,capacity=capacity,feasible=capacity>=1))
    return dict(inventories=rows,minimum=min(r['cost'] for r in rows if r['feasible']))
def main():
    out={'provenance':'constructed model; abstract units, not biological measurements','no_import':enumerate_boundary(False),'import_permitted':enumerate_boundary(True)}
    assert out['no_import']['minimum']==3 and out['import_permitted']['minimum']==1
    a={(r['synthesis'],r['transporter']) for r in out['no_import']['inventories'] if r['feasible']}
    b={(r['synthesis'],r['transporter']) for r in out['import_permitted']['inventories'] if r['feasible']}
    assert a<=b
    Path(__file__).with_name('boundary_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
