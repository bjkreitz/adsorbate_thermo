
import numpy as np
import pandas as pd

# declare a class for molecules
class Molecule:
    
        def __init__(self):
                data=pd.read_csv('Eref_bee_qe.txt', sep="\t", header=0)
                #start by defining some physical constants
                self.R = 8.3144621E-3 #ideal Gas constant in kJ/mol-K
                self.kB = 1.38065e-23 #Boltzmann constant in J/K
                self.h = 6.62607e-34 #Planck constant in J*s
                self.c = 2.99792458e8 #speed of light in m/s
                self.amu = 1.6605e-27 #atomic mass unit in kg
                self.Avogadro = 6.0221E23 #mole^-1
                self.eV_to_kJpermole = 96.485 #convert eV/molecule to kJ/mol
                self.rydberg_to_eV = 13.6056980659 #convert Ry/molecule to eV/molecule
                self.scale_BEEF = 0.683 #scaling factor for the BEEF ensemble
                self.dHfatct={'CH4':-66.557,'H2O':-238.929,'H2':0,'NH3':-38.565}#heats of formation (0K) in kJ/mol from the ATcT database for the reference species, version 1.122r (5/13/2022)
                self.Eref={'CH4':-324.294,'H2O':-611.0186083,'H2':-32.6984442,'NH3':-442.6510481} #DFT energies of the reference species (ZPE corrected) in eV
                self.Eslab=-377616.072 #DFT energy of the slab in eV
                self.dHrxnatct={'H2-2H':432.068, 'O2-2O':493.688, 'N2-2N':941.157}
                self.Erefbeeslab=data['Pt'].to_numpy()*self.rydberg_to_eV*self.scale_BEEF
                self.Erefbee={'CH4':data['CH4'].to_numpy()*self.rydberg_to_eV*self.scale_BEEF,'H2O':data['H2O'].to_numpy()*self.rydberg_to_eV*self.scale_BEEF,'H2':data['H2'].to_numpy()*self.rydberg_to_eV*self.scale_BEEF, 'NH3':data['NH3'].to_numpy()*self.rydberg_to_eV*self.scale_BEEF}
                self.molecular_mass_elements={'H': 1.01, 'C': 12.01, 'N': 14, 'O': 16}
                
def parse_input_file(inputfile, molecule):
    
    import os
    script_dir='dft-data/'
    rel_path = str(script_dir) + str(inputfile) + '.dat'
    abs_file_path = os.path.join(rel_path)
    
    input_file = open(abs_file_path,'r')
    lines = input_file.readlines()
    input_file.close()
    
    error_name = True
    error_DFT_energy = True
    error_ZPE_energy = True
    error_DFT_energy_gas = True
    error_ZPE_energy_gas = True
    error_composition = True
    error_sites = True
    error_gas_BEE = True
    error_BEE = True
    
    molecule.N_BEE=2000
    
    for line in lines:
        #start by looking for the name
        if line.strip().startswith("name"):
            bits = line.split('=')
            name = bits[1].strip().replace("'","").replace('"','')
            molecule.name = name
            error_name = False
        #now look for the DFT energy    
        elif line.strip().startswith("DFT_energy"):
            bits = line.split('=') 
            DFT_energy_info = bits[1].strip().replace("[","").replace("]","").split(',')
            DFT_energy = float(DFT_energy_info[0])
            units = DFT_energy_info[1].strip().replace("'","").replace('"','')
            if units=='eV':
                molecule.DFT_energy = DFT_energy
                molecule.DFT_energy_units = units.strip()
                error_DFT_energy = False
            else:
                print ("DFT energy is missing proper units!\n Please use 'eV'")
                break
           
        #now look for the ZPE energy    
        elif line.strip().startswith("ZPE_energy"):
            bits = line.split('=') 
            ZPE_energy_info = bits[1].strip().replace("[","").replace("]","").split(',')
            ZPE_energy = float(ZPE_energy_info[0])
            units = ZPE_energy_info[1].strip().replace("'","").replace('"','')
            if units=='eV':
                molecule.ZPE_energy = ZPE_energy
                molecule.ZPE_energy_units = units.strip()
                error_ZPE_energy = False
            else:
                print ("ZPE energy is missing proper units!\n Please use 'eV'")
                break
        #now look for the DFT energy    
        elif line.strip().startswith("gas_DFT_energy"):
            bits = line.split('=') 
            DFT_energy_gas_info = bits[1].strip().replace("[","").replace("]","").split(',')
            DFT_energy_gas = float(DFT_energy_gas_info[0])
            units = DFT_energy_gas_info[1].strip().replace("'","").replace('"','')
            if units=='eV':
                molecule.DFT_energy_gas = DFT_energy_gas
                molecule.DFT_energy_gas_units = units.strip()
                error_DFT_energy_gas = False
            else:
                print ("gas DFT energy is missing proper units!\n Please use 'eV'")
                break
           
        #now look for the ZPE energy    
        elif line.strip().startswith("gas_ZPE_energy"):
            bits = line.split('=') 
            ZPE_energy_gas_info = bits[1].strip().replace("[","").replace("]","").split(',')
            ZPE_energy_gas = float(ZPE_energy_gas_info[0])
            units = ZPE_energy_gas_info[1].strip().replace("'","").replace('"','')
            if units=='eV':
                molecule.ZPE_energy_gas = ZPE_energy_gas
                molecule.ZPE_energy_gas_units = units.strip()
                error_ZPE_energy_gas = False
            else:
                print ("gas ZPE energy is missing proper units!\n Please use 'eV'")
                break
        #now look for the composition    
        elif line.strip().startswith("composition"):
            bits = line.split('=') 
            composition = bits[1].strip().replace("{","").replace("}","").split(',')
            molecule.composition = {}
            for pair in composition:
                element, number = pair.split(":")
                element = element.strip().replace("'","").replace('"','')
                number = int(number)
                molecule.composition[element]=number
            N_adsorbate_atoms = 0
            for element in molecule.composition:
                if element!='Pt':
                    N_adsorbate_atoms += molecule.composition[element]            
            error_composition = False
            
        #now look for the BEE   
        elif line.strip().startswith("BEE"):
            bits = line.split('=') 
            BEE_data_info = bits[1].strip().replace("[","").replace("]","").split(',')
            BEE_data = BEE_data_info
            molecule.BEE_energies = []
            for i in range(len(BEE_data)):
                    molecule.BEE_energies.append(float(BEE_data[i]))
            if len(BEE_data)==molecule.N_BEE:
                    error_BEE = False
            else:
                print ("The number of sample of the BEE is not 2000!\n Please check again!")
                break      
        #now look for the gas BEE   
        elif line.strip().startswith("gas_BEE"):
            bits = line.split('=') 
            gas_BEE_data_info = bits[1].strip().replace("[","").replace("]","").split(',')
            gas_BEE_data = gas_BEE_data_info
            molecule.gas_BEE_energies = []
            for i in range(len(gas_BEE_data)):
                    molecule.gas_BEE_energies.append(float(gas_BEE_data[i]))

            if len(gas_BEE_data)==molecule.N_BEE:
                    error_gas_BEE = False
            else:
                print ("The number of sample of the gas BEE is not 2000!\n Please check again!")
                break          
            
    if error_name or error_DFT_energy or error_ZPE_energy or error_DFT_energy_gas or error_ZPE_energy_gas or error_composition or error_gas_BEE or error_BEE:
        print ("Input file is missing information: %s"%(inputfile))
    else:
        print ("successfully parsed file %s"%(inputfile))    
    return

def compute_thermo(molecule):

    if molecule.name=='H_ads':
       molecule.energy_gas=(molecule.DFT_energy_gas+molecule.ZPE_energy_gas+molecule.dHrxnatct['H2-2H']/molecule.eV_to_kJpermole)/2
    elif molecule.name=='O_ads':
       molecule.energy_gas=(molecule.DFT_energy_gas+molecule.ZPE_energy_gas+molecule.dHrxnatct['O2-2O']/molecule.eV_to_kJpermole)/2
    elif molecule.name=='N_ads':
       molecule.energy_gas=(molecule.DFT_energy_gas+molecule.ZPE_energy_gas+molecule.dHrxnatct['N2-2N']/molecule.eV_to_kJpermole)/2
    else:
       molecule.energy_gas=molecule.DFT_energy_gas+molecule.ZPE_energy_gas
        
    molecule.energy=molecule.DFT_energy+molecule.ZPE_energy

    molecule.dHrxndftgas=(molecule.energy_gas-molecule.composition['C']*molecule.Eref['CH4']
              -molecule.composition['O']*molecule.Eref['H2O']
              -molecule.composition['N']*molecule.Eref['NH3']
              -(molecule.composition['H']/2-2*molecule.composition['C']-molecule.composition['O']-3/2*molecule.composition['N'])*molecule.Eref['H2'])
    molecule.dHfgas=(molecule.composition['C']*molecule.dHfatct['CH4']
              +molecule.composition['O']*molecule.dHfatct['H2O']
              +molecule.composition['N']*molecule.dHfatct['NH3']
              +(molecule.composition['H']/2-2*molecule.composition['C']-molecule.composition['O']-3/2*molecule.composition['N'])*molecule.dHfatct['H2']
              +molecule.dHrxndftgas*molecule.eV_to_kJpermole)
    
    molecule.dHads=molecule.energy-molecule.energy_gas-molecule.Eslab
    molecule.dHf=molecule.dHfgas+molecule.dHads*molecule.eV_to_kJpermole
    print(molecule.dHf)
    return

def compute_thermo_bee(molecule):
    compute_thermo(test)
    
    molecule.energy_gas_bee= np.zeros(molecule.N_BEE)
    molecule.energy_bee=np.zeros(molecule.N_BEE)
    molecule.dHrxndftgas_bee= np.zeros(molecule.N_BEE)
    molecule.dHfgas_bee= np.zeros(molecule.N_BEE)
    molecule.dHads_bee=np.zeros(molecule.N_BEE)
    molecule.dHf_bee= np.zeros(molecule.N_BEE)
    
    molecule.ddHads_bee=np.zeros(molecule.N_BEE)
    molecule.ddHf_bee= np.zeros(molecule.N_BEE)
    for i in range(molecule.N_BEE):
        
        if molecule.name=='H_ads':
            molecule.energy_gas_bee[i]=(molecule.DFT_energy_gas-molecule.gas_BEE_energies[i]*molecule.rydberg_to_eV*molecule.scale_BEEF +molecule.ZPE_energy_gas+molecule.dHrxnatct['H2-2H']/molecule.eV_to_kJpermole)/2
        elif molecule.name=='O_ads':
            molecule.energy_gas_bee[i]=(molecule.DFT_energy_gas-molecule.gas_BEE_energies[i]*molecule.rydberg_to_eV*molecule.scale_BEEF+molecule.ZPE_energy_gas+molecule.dHrxnatct['O2-2O']/molecule.eV_to_kJpermole)/2
        elif molecule.name=='N_ads':
            molecule.energy_gas_bee[i]=(molecule.DFT_energy_gas-molecule.gas_BEE_energies[i]*molecule.rydberg_to_eV*molecule.scale_BEEF+molecule.ZPE_energy_gas+molecule.dHrxnatct['N2-2N']/molecule.eV_to_kJpermole)/2
        else:
            molecule.energy_gas_bee[i]=molecule.DFT_energy_gas-molecule.gas_BEE_energies[i]*molecule.rydberg_to_eV*molecule.scale_BEEF+molecule.ZPE_energy_gas

        molecule.energy_bee[i]=molecule.DFT_energy-molecule.BEE_energies[i]*molecule.rydberg_to_eV*molecule.scale_BEEF+molecule.ZPE_energy
 
        molecule.dHrxndftgas_bee[i]=(molecule.energy_gas_bee[i]-molecule.composition['C']*(molecule.Eref['CH4']-molecule.Erefbee['CH4'][i])
              -molecule.composition['O']*(molecule.Eref['H2O']-molecule.Erefbee['H2O'][i])
              -molecule.composition['N']*(molecule.Eref['NH3']-molecule.Erefbee['NH3'][i])
              -(molecule.composition['H']/2-2*molecule.composition['C']-molecule.composition['O']-3/2*molecule.composition['N'])*(molecule.Eref['H2']-molecule.Erefbee['H2'][i]))
        
        molecule.dHfgas_bee[i]=(molecule.composition['C']*molecule.dHfatct['CH4']
              +molecule.composition['O']*molecule.dHfatct['H2O']
              +molecule.composition['N']*molecule.dHfatct['NH3']
              +(molecule.composition['H']/2-2*molecule.composition['C']-molecule.composition['O']-3/2*molecule.composition['N'])*molecule.dHfatct['H2']
              +molecule.dHrxndftgas_bee[i]*molecule.eV_to_kJpermole)
        
        molecule.dHads_bee[i]=molecule.energy_bee[i]-molecule.energy_gas_bee[i]-(molecule.Eslab-molecule.Erefbeeslab[i])

        molecule.dHf_bee[i]=molecule.dHfgas_bee[i]+molecule.dHads_bee[i]*molecule.eV_to_kJpermole

        molecule.ddHf_bee[i]=-molecule.dHf+molecule.dHf_bee[i]
        molecule.ddHads_bee[i]=-molecule.dHads+molecule.dHads_bee[i]
        #print(molecule.dHf_bee[i])
    import os
    
    script_dir=''
    rel_path = str(molecule.name) + '_bee.txt'
    output_file_path = os.path.join(script_dir, rel_path)
    data=np.c_[molecule.dHads_bee, molecule.dHf_bee, molecule.ddHads_bee, molecule.ddHf_bee]
    names=['Hads', 'Hf','deltaHads ref='+str(molecule.dHads), 'deltaHf ref='+str(molecule.dHf)]
    df=pd.DataFrame(data, columns=[names])
    df.to_csv(output_file_path,sep="\t", index=False)
    return

test = Molecule()
parse_input_file('CH',test)

compute_thermo_bee(test)