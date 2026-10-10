"""WRRA Bio AI methods 0.1. Standard library only; illustrative, not empirical."""
import math, json, hashlib
from pathlib import Path

def partition(n,k):
    p=[0.,0.,0.]
    for a in range(n+1):
        alive=int(a>=k)+int(n-a>=k)
        p[alive]+=math.comb(n,a)/2**n
    return dict(n=n,k=k,p0=p[0],p1=p[1],p2=p[2],expected_daughters=p[1]+2*p[2])

def gate(items):
    # Each field is adjudicated upstream; this does not verify evidence truth.
    if not isinstance(items,list) or not items:
        raise ValueError('A nonempty list of necessary requirement states is required')
    if any(x is not True and x is not False and x is not None for x in items):
        raise ValueError('Requirement state must be exactly true, false, or null')
    if any(x is False for x in items): return 'FAIL'
    if any(x is None for x in items): return 'OPEN'
    return 'PASS'

def main():
    import itertools
    gate_tests=[]
    for states in itertools.product([False,None,True],repeat=4):
        got=gate(list(states))
        expected='FAIL' if False in states else ('OPEN' if None in states else 'PASS')
        assert got==expected
        gate_tests.append(dict(states=states,verdict=got))
    partitions=[partition(n,2) for n in range(2,9)]
    for r in partitions:
        assert abs(r['p0']+r['p1']+r['p2']-1)<1e-12
        marginal=sum(math.comb(r['n'],a)/2**r['n'] for a in range(2,r['n']+1))
        assert abs(r['expected_daughters']-2*marginal)<1e-12
    assert partition(4,2)['p2']==0.375
    assert partition(4,2)['expected_daughters']==1.375
    nmin=next(n for n in range(2,100) if partition(n,2)['p2']>=0.95)
    assert nmin==9
    invalid_inputs=[[],['unknown'],[1],[0],{},None]
    for bad in invalid_inputs:
        try: gate(bad)
        except ValueError: pass
        else: raise AssertionError('Malformed requirement accepted')
    def history(q,u,r):
        values=[100.]
        for g in range(5): values.append(q*values[-1]+u+r)
        return values
    inherited=history(.5,0,0)
    externally_replaced=history(.5,50,0)
    internally_regenerated=history(.5,0,50)
    assert externally_replaced==internally_regenerated
    out={'scope':'constructed model and rule verification, not AI benchmark or biological validation',
         'gate_truth_table_cases':len(gate_tests),'rejected_malformed_inputs':len(invalid_inputs),'partition':partitions,
         'minimum_n_for_p2_at_least_095_given_k2':nmin,
         'n9':partition(9,2),'inherited_only':inherited,
         'externally_replaced':externally_replaced,'internally_regenerated':internally_regenerated,
         'same_observable_different_ownership':externally_replaced==internally_regenerated}
    p=Path(__file__).parent/'results.json'
    p.write_text(json.dumps(out,indent=2)+'\n')
    print(p.read_text())

if __name__=='__main__': main()
