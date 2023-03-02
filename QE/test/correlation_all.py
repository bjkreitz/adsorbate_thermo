import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import matplotlib.gridspec as gridspec

#Makes the diagrams look nice and shiny
plt.rcParams['figure.figsize']=(18,24)
plt.rcParams['axes.linewidth'] = 3
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.rc('axes', labelsize=18)
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

colormap=plt.cm.Dark2
colors = [colormap(i) for i in np.linspace(0, 1, 8)]

kJ_mol_to_eV=96.485

COdata=pd.read_csv('ensembles/O_ads_bee.txt',  sep="\t", header=0)
CO_avg=np.mean(COdata.iloc[:,1])

t50=pd.read_csv('~/BEEF_methane_oxidation/T50.txt',  sep="\t", header=0)
CO=np.zeros(len(t50.Mechanism))
for i in range(len(t50.Mechanism)):
    CO[i]=COdata.iloc[i,1]

colormap=plt.cm.Dark2
colors = [colormap(i) for i in np.linspace(0, 1, 8)]


colors=list(colors)+list(colors)+list(colors)+list(colors)

ax = []
fig, axs = plt.subplots(nrows=10, ncols=6)
fig.subplots_adjust(hspace=0.6, wspace=0.4)
for i, row in enumerate(axs):
    for j, a in enumerate(row):
        ax.append(a)

Name='surfaceThermoPt111_QE'

species=pd.read_csv('species_names.txt', sep="\t", header=0)

label=[]
index=[]
    
file="".join((Name,".py"))
original_file="".join((Name,".py"))
s=open(original_file,'r')
new_file_content=""    

for line in s:
        if line.startswith("    label"):
            old=line.strip()
            bits=line.split(" = ")
            label.append(bits[1].replace(",","").replace("\n","").replace('"',""))
                       
        if line.startswith("    index"):
            old=line.strip()
            bits=line.split(" = ")
            index.append(int(bits[1].replace(",","")))
            new_line=line.replace(old,old)
            new_file_content += new_line  
        else:
            old=line.strip()
            new_line=line.replace(old,old)
            new_file_content += new_line  
            
writing_file = open(file, "w")
writing_file.write(new_file_content)
writing_file.close()
    
#The number of possible entries to modify is given by the number of collected labels
no=len(label)    
        
names=np.arange(0,60)
names=names.reshape(10,6)

for k,l in enumerate(label[1:61]):
     file='ensembles/' + str(l) + '_bee.txt'
     rawdata=pd.read_csv(file, sep="\t", header=0)
     data=np.zeros(len(t50.Mechanism))
     for i in range(len(t50.Mechanism)):
         data[i]=rawdata.iloc[i,1]
         
     col=int(np.where(names==k)[0])
     row=int(np.where(names==k)[1])
     
     y=np.linspace(min(data/kJ_mol_to_eV), max(data/kJ_mol_to_eV), 20)
     x=np.linspace(min(CO/kJ_mol_to_eV), max(CO/kJ_mol_to_eV), 20)
     #.reshape(5001)
     avg=stats.binned_statistic_2d(CO/kJ_mol_to_eV,data/kJ_mol_to_eV,t50['CH4'].to_numpy(), bins=[x,y], statistic='mean')

     eax=axs[col,row].imshow(avg.statistic.T, origin='lower',aspect='equal',extent=(min(x),max(x),min(y),max(y)), interpolation='none', cmap='viridis', vmin=200, vmax=max(t50['CH4'].to_numpy()))
     axs[col,row].set_aspect((max(x)-min(x))/(max(y)-min(y)))

     
     #axs[col,row].plot(CO, data,  color='b', marker='o', linestyle='None', markersize=5, alpha=0.2,markeredgewidth=0, rasterized=True)
     #axs[col,row].plot(CO_avg,np.mean(data.iloc[:,1]), color='r', marker='o')
     #axs[col,row].set_ylim([np.mean(data.iloc[:,1])-60,np.mean(data.iloc[:,1])+60 ])
     title="$\mathbf{" + str(species['species'][k]) + "}$"
     axs[col,row].set_title(title)
     
plt.savefig('correlation_CH4.pdf', transparent=False, bbox_inches='tight')