#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:17:32 2021

@author: bkr
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.gridspec as gridspec

#Makes the diagrams look nice and shiny
plt.rcParams['figure.figsize']=(21,6)
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


H=pd.read_csv('H_ads_bee.txt', sep="\t", header=0)
C=pd.read_csv('C_ads_bee.txt', sep="\t", header=0)
O=pd.read_csv('O_ads_bee.txt', sep="\t", header=0)
CO=pd.read_csv('CO_ads_bee.txt', sep="\t", header=0)

gs=gridspec.GridSpec(nrows=1, ncols=3)
gs.update(wspace=0.3, hspace=0.2)

ax0=plt.subplot(gs[0,0])
ax1=plt.subplot(gs[0,1])
ax2=plt.subplot(gs[0,2])


ax0.set_xlabel('$\mathrm{H^*\ heat\ of\ formation\ (eV)}$')
#ax0.set_ylim([-4.0, -3])
#ax0.set_xlim([-3.0, -2])
ax0.set_ylabel('$\mathrm{C^*\ heat\ of\ formation\ (eV)}$')

ax1.set_xlabel('$\mathrm{H^*\ heat\ of\ formation\ (eV)}$')
#ax1.set_ylim([-2.5, -0.5])
#ax1.set_xlim([-1, 1])
ax1.set_ylabel('$\mathrm{O^*\ heat\ of\ formation\ (eV)}$')

ax2.set_xlabel('$\mathrm{H^*\ heat\ of\ formation\ (eV)}$')
#ax1.set_ylim([-2.5, -0.5])
#ax1.set_xlim([-1, 1])
ax2.set_ylabel('$\mathrm{CO^*\ heat\ of\ formation\ (eV)}$')


ax0.plot(H.iloc[:,1], C.iloc[:,1],  color='b', marker='o', linestyle='None', markersize=5, markerfacecolor='w')

ax1.plot(H.iloc[:,1], O.iloc[:,1],  color='b', marker='o', linestyle='None', markersize=5, markerfacecolor='w')

ax2.plot(H.iloc[:,1], CO.iloc[:,1],  color='b', marker='o', linestyle='None', markersize=5, markerfacecolor='w')


initial_H_Hf=-23.109538200349135
initial_O_Hf=-137.49019573110039

ax0.plot(np.mean(H.iloc[:,1]), np.mean(C.iloc[:,1]),  color='r', marker='o', linestyle='None', markersize=10)

ax1.plot(initial_H_Hf, initial_O_Hf,  color='r', marker='o', linestyle='None', markersize=10)

ax2.plot(np.mean(H.iloc[:,1]), np.mean(CO.iloc[:,1]),  color='r', marker='o', linestyle='None', markersize=10)

plt.savefig('BEEFensemble.png',dpi=300, bbox_inches='tight', transparent=False)

# H_average=np.mean(H.iloc[:,0])
# O_average=np.mean(O.iloc[:,0])

# delta_H=(-H_average+H.iloc[:,0])*96.485
# delta_O=(-O_average+O.iloc[:,0])*96.485

# ax2.plot(delta_H, delta_O,  color='b', marker='o', linestyle='None', markersize=5, markerfacecolor='w')
# ax2.plot(H.iloc[:,3], O.iloc[:,3],  color='r', marker='o', linestyle='None', markersize=5, markerfacecolor='w')

# H_sigma=np.std(H.iloc[:,1])
# O_sigma=np.std(O.iloc[:,1])

# count=0
# for i in range(len(O.iloc[:,1])):
#     if abs(O.iloc[i,1])>abs(O_average+2*O_sigma) and abs(O.iloc[i,1])<abs(O_average-2*O_sigma):
#         count+=1
#         ax0.plot(H.iloc[i,0], O.iloc[i,0],  color='r', marker='o', linestyle='None', markersize=5, markerfacecolor='w')
#         ax1.plot(H.iloc[i,1], O.iloc[i,1],  color='r', marker='o', linestyle='None', markersize=5, markerfacecolor='w') 
        
# print(count)    



#ax0.plot(H_average, O_average,  color='r', marker='o', linestyle='None', markersize=8, markerfacecolor='r')

#plt.savefig('BEEF_O_H.png',dpi=300, bbox_inches='tight', transparent=False)