

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob

#Makes the diagrams look nice and shiny
plt.rcParams['figure.figsize']=(18,24)
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
plt.rc('axes', labelsize=16)
plt.rc('legend', fontsize=14)
plt.rcParams['lines.markersize'] = 10
plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
plt.rcParams['xtick.major.size']=10
plt.rcParams['xtick.major.width']=2
plt.rcParams['ytick.major.size']=10
plt.rcParams['ytick.major.width']=2
plt.rcParams['legend.edgecolor']='k'
plt.rcParams['axes.unicode_minus']=False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8
plt.rcParams['legend.handletextpad']=0.4
plt.rcParams['legend.columnspacing']=0.5
plt.rcParams['legend.labelspacing']=0.3
plt.rcParams['legend.title_fontsize'] = 14
plt.rcParams['axes.formatter.limits']=(-3, 6)

ax = []
fig, axs = plt.subplots(nrows=9, ncols=8)
fig.subplots_adjust(hspace=0.6, wspace=0.4)
for i, row in enumerate(axs):
    for j, a in enumerate(row):
        ax.append(a)


groups=[]
for filename in glob.iglob('ensembles/*_bee.txt'):
    bits_dat_info=filename.split('_')
    bits_dat=bits_dat_info[0].replace('.txt','').replace('ensembles/','')
    groups.append(bits_dat)

group_names=[sub.replace('#','\u2261') for sub in groups] 
group_names=[sub.replace('2','_2') for sub in group_names]  
group_names=[sub.replace('3','_3') for sub in group_names] 
group_names=[sub.replace('4','_4') for sub in group_names] 

CO=pd.read_csv('../ensembles/CO_ads_bee.txt',  sep="\t", header=0)
CO_avg=np.mean(CO.iloc[:,1])
for i, ax in enumerate(ax):
    ax.set_xlim([CO_avg-60, CO_avg+60])
    #ax.text(0.1, 0.75, '$\mathbf{'+rxn[i]+'}$', transform=ax.transAxes,  size=16, weight='bold')
    #ax.set_ylabel('$\mathrm{\delta\Delta H_{ads}, (kJ\,mol^{-1})}$')
    #ax.set_xlabel('$\mathrm{\Delta_f H_{\,^*CO} \, (kJ\,mol^{-1})}$')
    
names=np.arange(0,72)
names=names.reshape(9,8)

for k,l in enumerate(groups):
      file='ensembles/' + str(l) + '_bee.txt'
      data=pd.read_csv(file, sep="\t", header=0)
      col=int(np.where(names==k)[0])
      row=int(np.where(names==k)[1])
      axs[col,row].plot(CO.iloc[:,1], data.iloc[:,0],  color='b', marker='o', linestyle='None', markersize=5, alpha=0.2,markeredgewidth=0, rasterized=True)
      axs[col,row].plot(CO_avg,np.mean(data.iloc[:,0]), color='r', marker='o')
      axs[col,row].set_ylim([np.mean(data.iloc[:,0])-60,np.mean(data.iloc[:,0])+60 ])
      title="$\mathbf{" + str(group_names[k]) + "}$"
      axs[col,row].set_title(title)
      
axs[-1,-1].set_visible(False) # to remove last plot

plt.savefig('uq_ads_corr.pdf', transparent=False, bbox_inches='tight')