from pathlib import Path
from math import comb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from integrated_model import restoration
P=Path(__file__).parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(1,2,figsize=(10,3.8),layout='constrained')
rs=list(range(10));ps=[restoration(9,2,r)['probability'] for r in rs]
ax[0].plot(rs,ps,'o-',color='#234f78',label='Joint restoration')
ax[0].axhline(.95,color='#777777',ls='--',lw=1,label='95% target')
ax[0].set(xlabel='Attainable capacity R per daughter',ylabel='Probability both daughters meet target',title='A  Fixed inventory n = 9, k = 2',ylim=(-.03,1.05),xticks=range(0,10,2))
ns=list(range(4,13))
competence=[sum(comb(n,a) for a in range(2,n-1))/2**n for n in ns]
joint=[restoration(n,2,4)['probability'] for n in ns]
ax[1].plot(ns,competence,'o-',color='#8b5b1b',label='Immediate competence')
ax[1].plot(ns,joint,'s-',color='#234f78',label='Restore candidate inventory n')
ax[1].set(xlabel='Candidate parent inventory n',title='B  Fixed capacity R = 4, k = 2',ylim=(-.03,1.05),xticks=range(4,13,2))
for a in ax:a.legend(fontsize=8,loc='lower left' if a==ax[0] else 'center right');a.grid(axis='y',alpha=.15)
fig.savefig(P/'Figure_1.png',dpi=350)
fig.savefig(P/'Figure_1.pdf')
plt.close(fig)
