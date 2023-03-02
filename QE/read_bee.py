import numpy as np
import os

def parse_input_file(inputfile):

    rel_path = "bee/" + str(inputfile) + "-ensemble.out"
    
    input_file = open(rel_path,'r')
    lines = input_file.readlines()
    input_file.close()
    
    bee=2000
    
    for index, line in enumerate(lines):
        if line.strip().startswith("BEEFens 2000 ensemble energies"):
            bee_start=index
            bee_start+=1
            bee_end=bee_start+bee
            
    bee_energy=[]
    for index, line in enumerate(lines):
        if bee_start<= index < bee_end:
            bits = line.split('             ') 
            energy_data = bits[1].strip().replace("\n","")
            bee_energy.append(energy_data)

    bee_list=str(bee_energy)
    bee_list = bee_list.strip().replace("'","")
    bee_list = bee_list.strip().replace(" ","")
    return bee_list          
            

def parse_gas_input_file(inputfile):

    rel_path = "bee-gas/" + str(inputfile) + "-gas-ensemble.out"
    
    input_file = open(rel_path,'r')
    lines = input_file.readlines()
    input_file.close()
    
    bee=2000
    
    for index, line in enumerate(lines):
        if line.strip().startswith("BEEFens 2000 ensemble energies"):
            bee_start=index
            bee_start+=1
            bee_end=bee_start+bee
            
    bee_energy=[]
    for index, line in enumerate(lines):
        if bee_start<= index < bee_end:
            bits = line.split('             ') 
            energy_data = bits[1].strip().replace("\n","")
            bee_energy.append(energy_data)

    bee_list=str(bee_energy)
    bee_list = bee_list.strip().replace("'","")
    bee_list = bee_list.strip().replace(" ","")
    return bee_list  

species='ch3oco'

adsorbate=parse_input_file(species)
gas=parse_gas_input_file(species)