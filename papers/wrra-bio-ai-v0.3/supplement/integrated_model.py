"""One-component restoration model; exact probabilities, no fitted biology."""
from math import comb
from fractions import Fraction
from pathlib import Path
import json

def restoration(n,k,R):
    h=max(k,n-R)
    lo=max(0,h); hi=min(n,n-h)
    p=sum((Fraction(comb(n,a),2**n) for a in range(lo,hi+1)),Fraction(0))
    direct=Fraction(0)
    for mask in range(2**n):
        a=mask.bit_count()
        if a>=k and n-a>=k and a+R>=n and n-a+R>=n:
            direct+=Fraction(1,2**n)
    assert p==direct
    return {'n':n,'k':k,'internal_capacity_per_daughter':R,'effective_threshold':h,'probability':float(p),'exact_probability':str(p)}

def main():
    rows=[restoration(9,2,r) for r in range(10)]
    assert rows[4]['probability']==0
    assert rows[6]['probability']==0.8203125
    assert rows[7]['probability']==0.9609375
    assert min(r['internal_capacity_per_daughter'] for r in rows if r['probability']>=.95)==7
    contrast=[restoration(n,2,4) for n in (8,9)]
    assert contrast[0]['probability']==0.2734375 and contrast[1]['probability']==0
    out={'fixed_capacity_contrast':contrast,'assumptions':'One component; fair independent partition; each daughter can add any integer amount from 0 to R within the horizon if immediately competent; no external active machinery; fixed permitted substrates; no turnover; restoration means n units only, not full cell state.','rows':rows,'minimum_R_for_95_percent':7}
    Path(__file__).with_name('integrated_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
