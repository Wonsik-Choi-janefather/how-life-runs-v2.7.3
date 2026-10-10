"""Curated evidence records. Source paraphrases were checked during drafting.
No autonomous extraction accuracy is claimed. Null means unknown in this packet.
"""
import json
from pathlib import Path
P=Path(__file__).parent
sources={
 'S1':{'url':'https://www.jcvi.org/publications/design-and-synthesis-minimal-bacterial-genome','locator':'Abstract; sentence reporting three design cycles and sentence beginning Unexpectedly','summary':'2016 report: JCVI-syn3.0 has 473 genes; 149 had unknown biological functions.','scope':'Historical report; the reduced genome is not asserted to be a universal minimum across environments.','review_status':'manually checked against public abstract 2026-10-10'},
 'S2':{'url':'https://www.nature.com/articles/nbt0801_751','locator':'Abstract; first sentence','summary':'A protein-synthesizing system was reconstituted from purified recombinant tagged protein factors.','scope':'Supplied translation system; this source statement alone does not establish its autonomous regeneration.','review_status':'manually checked against public abstract 2026-10-10'},
 'M1':{'url':None,'locator':'reproduce.py history function and results.json machinery arrays','summary':'Analyst-set recurrence e_next=0.5e+u+r; initial e=100.','scope':'Constructed model in arbitrary active units, not measured PURE kinetics.','review_status':'computed'},
 'M2':{'url':None,'locator':'reproduce.py partition function and results.json n9','summary':'Independent fair allocation; k=2; model competence threshold.','scope':'Constructed one-component partition model, not whole-cell viability.','review_status':'computed'}
}

def requirement(name,state,source,locator,kind='source_adjudication'):
 return dict(name=name,state=state,evidence_id=source,locator=locator,kind=kind)

def record(cid,target,condition,roles,requirements,basis=None,scope='evidence_record'):
 return dict(claim_id=cid,target=target,system_boundary='Defined per execution_roles and condition_id',condition_id=condition,
  time_window='Historical publication snapshot' if scope=='evidence_record' else 'Declared finite model horizon',
  execution_roles=roles,requirements=requirements,sufficiency_basis=basis,scope=scope,version='0.2',
  provenance_status='author-curated; no automated source-verification claim')

minimal={'source':'JCVI-syn3.0 genome','state':'reported functioning cell','renderer':'cellular machinery; individual functions not all assigned in this packet','boundary':'original culture context; complete recipe not extracted here','biological_carrier':None,'observable':'reported replication and annotation status'}
translation={'source':'translation templates and initial supplies','state':'reconstituted mixture','renderer':'purified protein factors and translation apparatus','boundary':'supplied components; all later exchanges unspecified in packet','biological_carrier':'shared translation machinery at process level; full component inventory not extracted','observable':'protein synthesis'}
partition={'source':'n identical units','state':'parent inventory','renderer':None,'phenotype_map':'competence threshold k=2','boundary':'closed allocation at one division; no new units during partition','biological_carrier':None,'model_scaffold':'one shared fair allocation rule','observable':'competent daughter count'}
machinery={'source':'initial 100 active units','state':'active machinery amount e','renderer':None,'phenotype_map':'assumed output proportional to e','boundary':'retention 0.5; external replacement u separate from internal r','biological_carrier':None,'model_scaffold':'shared recurrence for all ownership scenarios','observable':'active units or proportional output'}
rows=[
 record('C1','The cited report describes replication with the reduced genome','syn3_2016',minimal,[requirement('Report explicitly supports reduced-genome replication',True,'S1','Abstract; three cycles sentence')],'Direct narrow report-level statement; not independent replication.'),
 record('C2','All 473 gene functions are specified in the selected 2016 report','syn3_2016',minimal,[requirement('Complete functional assignment in selected report',False,'S1','Abstract; 149 unknown functions')]),
 record('C3','A complete executable mechanistic explanation can be reconstructed from this packet','syn3_2016',minimal,[requirement('Reported functioning cell',True,'S1','Abstract'),requirement('Complete mechanistic links supplied',None,None,None)]),
 record('C4','The selected source reports protein synthesis using reconstituted machinery','pure_2001',translation,[requirement('Protein synthesis reported',True,'S2','Abstract; first sentence')],'Direct narrow report-level statement; not independent replication.'),
 record('C5','The selected source packet establishes autonomous regeneration of its translation machinery','pure_2001',translation,[requirement('Protein synthesis reported',True,'S2','Abstract; first sentence'),requirement('Permitted external exchanges specified',None,None,None),requirement('New internally made functional machinery established',None,None,None),requirement('Required persistence horizon established',None,None,None)]),
 record('C6','Equal active output can arise from external replacement or internal regeneration','machinery_fixture',machinery,[requirement('Both recurrences execute',True,'M1','results.json machinery arrays','model'),requirement('Outputs equal while u and r differ',True,'M1','reproduce.py history assertions','model')],'Constructive equality under declared recurrence; biological feasibility not asserted.','constructed_model'),
 record('C7','Nine units are minimal for 95 percent joint competence at k=2','partition_fixture',partition,[requirement('n8 below target',True,'M2','results.json partition n=8','model'),requirement('n9 above target',True,'M2','results.json n9','model'),requirement('Monotonicity and smaller n checked',True,'M2','Manuscript 4.3 and reproduce.py minimum search','model')],'Binomial formula and monotonicity in declared candidate family only.','constructed_model')
]
sources['S3']={'url':'https://doi.org/10.1038/s41467-019-10837-2','locator':'Figure 4 caption and Results paragraph beginning For example, MMSYN1_0138','summary':'Computational transporter annotations include a magnesium-importing ATPase proposal and a caveat about an ATP-binding site.','scope':'Predicted functions, not directly measured substrate flux.','review_status':'manually checked against full article 2026-10-10'}
transport={'source':'reported protein sequences and computational annotations','state':'candidate annotated proteins','renderer':'proposed transport machinery; functional activity not established in packet','boundary':'candidate nutrient transport across cellular membrane','biological_carrier':None,'observable':'reported predictions, not measured transport flux'}
for cid,protein,locator in [('C8','MMSYN1_0879','Figure 4 caption'),('C10','MMSYN1_0138','Results; paragraph beginning For example, MMSYN1_0138')]:
 rows.append(record(cid,'The source reports a transport-related annotation or caveat for '+protein,'annotation_2019',transport,[requirement('Annotation or caveat explicitly reported',True,'S3',locator)],'Narrow report-level statement; not functional validation.'))
 rows.append(record('C'+str(int(cid[1:])+1),'The proposed transport mechanism of '+protein+' supplies sufficient flux for the declared maintenance target','annotation_2019',transport,[requirement('Transport-related annotation reported',True,'S3',locator),requirement('Substrate flux and energy dependence established',None,None,None),requirement('Target horizon and required flux established',None,None,None)]))

sources['M3']={'url':None,'locator':'boundary_model.py and boundary_results.json','summary':'Constructed synthesis/import capacity enumeration.','scope':'Abstract component costs, not measured gene counts.','review_status':'computed'}
sources['M4']={'url':None,'locator':'integrated_model.py and integrated_results.json','summary':'Partition followed by attainable per-daughter internal restoration.','scope':'Finite one-component contract, no full-cell viability claim.','review_status':'computed'}
boundary_roles={'source':'candidate synthesis and transport modules','state':'internal inventory','renderer':None,'boundary':'optional import profiles','biological_carrier':None,'observable':'feasibility and minimum internal cost'}
joint_roles={'source':'n active units','state':'daughter inheritance and restoration capacity','renderer':None,'boundary':'permitted substrates; no external active machinery; no loss','biological_carrier':None,'observable':'probability both daughters restore n before next division'}
rows.extend([
 record('C12','Minimum internal cost changes from 3 to 1 when Q import is permitted','boundary_fixture',boundary_roles,[requirement('Feasible sets and minima enumerated',True,'M3','boundary_results.json','model')],'Exact enumeration under specified abstract costs and capacities.','constructed_model'),
 record('C13','At n9 k2 capacity R7 is minimal for 95 percent joint restoration','joint_fixture',joint_roles,[requirement('Formula agrees with allocation enumeration',True,'M4','integrated_model.py restoration','model'),requirement('R0 through R6 below target and R7 above',True,'M4','integrated_results.json rows','model')],'Exact finite model enumeration, not measured cell regeneration.','constructed_model'),
 record('C14','At fixed R4, n8 to n9 raises immediate competence but eliminates joint restoration','joint_fixture',joint_roles,[requirement('Restoration contrast enumerated',True,'M4','integrated_results.json fixed_capacity_contrast','model'),requirement('Immediate competence probabilities computed',True,'M2','results.json partition n8 and n9','model')],'Targets restore each candidate parent inventory; not comparison at one common fixed inventory endpoint.','constructed_model')
])
for row in rows:
 if row['claim_id'] in ('C10','C11'):
  row['requirements'].append(requirement('Source reports ATP-binding site not conserved',True,'S3','Results; paragraph beginning For example, MMSYN1_0138'))
links={'C2':(['C1'],'separates functional completeness from reported growth'),'C3':(['C1','C2'],'asks for a stronger mechanistic account'),'C5':(['C4'],'asks for machinery regeneration beyond output'),'C6':(['C5'],'provides a model non-identifiability example'),'C9':(['C8'],'asks for functional transport beyond annotation'),'C11':(['C10'],'asks for functional transport beyond annotation')}
links.update({'C12':([], 'boundary model root'),'C13':(['C6','C7'], 'combines inherited competence with internal regeneration capacity'),'C14':(['C7','C13'], 'contrasts candidate inventories at fixed regeneration capacity')})
for row in rows:
 row['version']='0.3'
 row['parent_claim_ids'],row['relation']=links.get(row['claim_id'],([], 'source or model root'))
 for r in row['requirements']:r['condition_id']=row['condition_id']
(P/'evidence_ledger.json').write_text(json.dumps({'schema_version':'0.3','sources':sources,'claims':rows},ensure_ascii=False,indent=2)+'\n')
