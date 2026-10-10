"""Validate curated ledger shape and compute contract results, not source truth."""
import json,copy
from pathlib import Path
from reproduce import gate
P=Path(__file__).parent
def audit(claim,sources):
 required=['claim_id','target','system_boundary','condition_id','time_window','execution_roles','requirements','scope','version','provenance_status']
 for key in required:
  if key not in claim or not claim[key]:raise ValueError('Missing field: '+key)
 for key in ['source','state','renderer','boundary','biological_carrier','observable']:
  if key not in claim['execution_roles']:raise ValueError('Missing execution role: '+key)
 req=claim['requirements']
 if not isinstance(req,list) or not req:raise ValueError('Nonempty requirements required')
 for r in req:
  if not isinstance(r,dict) or not r.get('name') or 'state' not in r:raise ValueError('Malformed requirement')
  if r.get('condition_id')!=claim['condition_id']:raise ValueError('Condition mismatch')
  if r['state'] is not None and (r.get('evidence_id') not in sources or not r.get('locator')):raise ValueError('Adjudicated requirement lacks evidence locator')
 verdict=gate([r['state'] for r in req])
 # All true is only satisfaction of declared checks. Sufficiency is a separate assertion.
 verdict={'PASS':'CHECKS_SATISFIED','FAIL':'CONTRACT_FAIL','OPEN':'OPEN'}[verdict]
 basis=claim.get('sufficiency_basis')
 return dict(claim_id=claim['claim_id'],check_verdict=verdict,
  claim_conclusion='declared narrow conclusion; see manually supplied sufficiency basis' if verdict=='CHECKS_SATISFIED' and basis else 'not established by checker',
  sufficiency_basis=basis,unknown_requirements=[r['name'] for r in req if r['state'] is None],
  failed_requirements=[r['name'] for r in req if r['state'] is False],
  biological_carrier_status='OPEN' if claim['execution_roles']['biological_carrier'] is None else 'specified in curated record')

def main():
 data=json.loads((P/'evidence_ledger.json').read_text())
 ids=[c['claim_id'] for c in data['claims']]
 if len(set(ids))!=len(ids):raise ValueError('Duplicate claim id')
 for c in data['claims']:
  if not isinstance(c.get('parent_claim_ids'),list) or not c.get('relation'):raise ValueError('Missing trace relation')
  if any(p not in ids or p==c['claim_id'] for p in c['parent_claim_ids']):raise ValueError('Invalid trace reference')
 output=[audit(c,data['sources']) for c in data['claims']]
 # Mutations exercise risks identified by review, not biological correctness.
 cases=[]
 for field in ['condition_id','target','execution_roles']:
  c=copy.deepcopy(data['claims'][0]);del c[field];cases.append(c)
 c=copy.deepcopy(data['claims'][0]);c['requirements']=[];cases.append(c)
 c=copy.deepcopy(data['claims'][0]);c['requirements'][0]['state']='unknown';cases.append(c)
 c=copy.deepcopy(data['claims'][0]);c['requirements'][0]['locator']=None;cases.append(c)
 c=copy.deepcopy(data['claims'][0]);c['requirements'][0]['condition_id']='other';cases.append(c)
 for c in cases:
  try:audit(c,data['sources'])
  except ValueError:pass
  else:raise AssertionError('Invalid ledger accepted')
 out={'claims':output,'rejected_ledger_mutations':len(cases),'limitation':'Evidence truth, source semantics, and sufficiency bases require human adjudication.'}
 (P/'audit_results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
