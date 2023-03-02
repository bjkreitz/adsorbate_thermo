

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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


colormap=plt.cm.Dark2
colors = [colormap(i) for i in np.linspace(0, 1, 8)]


colors=list(colors)+list(colors)+list(colors)+list(colors)

ax = []
fig, axs = plt.subplots(nrows=10, ncols=6)
fig.subplots_adjust(hspace=0.6, wspace=0.4)
for i, row in enumerate(axs):
    for j, a in enumerate(row):
        ax.append(a)
 
import numpy as np
import pandas as pd

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

CO=pd.read_csv('ensembles/CO_ads_bee.txt',  sep="\t", header=0)
CO_avg=np.mean(CO.iloc[:,1])
for i, ax in enumerate(ax):
    ax.set_xlim([CO_avg-60, CO_avg+60])
    #ax.text(0.1, 0.75, '$\mathbf{'+rxn[i]+'}$', transform=ax.transAxes,  size=16, weight='bold')
    #ax.set_ylabel('$\mathrm{\Theta\ /\ 1}$')
    #ax.set_xlabel('$\mathrm{temperature\ /\ K}$')
    #ax.set_rasterization_zorder(-10)
    
names=np.arange(0,60)
names=names.reshape(10,6)

for k,l in enumerate(label[1:61]):
     file='ensembles/' + str(l) + '_bee.txt'
     data=pd.read_csv(file, sep="\t", header=0)
     col=int(np.where(names==k)[0])
     row=int(np.where(names==k)[1])
     axs[col,row].plot(CO.iloc[:,1], data.iloc[:,1],  color='b', marker='o', linestyle='None', markersize=5, alpha=0.2,markeredgewidth=0, rasterized=True)
     axs[col,row].plot(CO_avg,np.mean(data.iloc[:,1]), color='r', marker='o')
     axs[col,row].set_ylim([np.mean(data.iloc[:,1])-60,np.mean(data.iloc[:,1])+60 ])
     title="$\mathbf{" + str(species['species'][k]) + "}$"
     axs[col,row].set_title(title)

plt.savefig('uq_thermo_library1.pdf', transparent=False, bbox_inches='tight')