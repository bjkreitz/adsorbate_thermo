#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 22:13:05 2022

@author: bkr
"""

from ase import Atoms
from ase.build import molecule
import numpy as np
from ase.io import read,write
from ase.visualize import view

file='ch3'
name="".join((file,'.traj'))

species=read(name)
view(species)

I=Atoms.get_moments_of_inertia(species)
#print(I) #units of amu angstrom2
amu_to_kg = 1.66054e-27 #kg per amu
angstrom_to_m = 1e-10 #m per angstrom
I = I*amu_to_kg*angstrom_to_m**2.0 #kg m2

h=6.62607e-34 #Js or m2kg/s or J Hz-1
c=2.9979e8 #m/s
B = h/(8.0*np.pi**2.0*c*I) #in 1/m
B = B*c/1e9 #in GHZ

B=list(np.round(B,2))
print(B)
