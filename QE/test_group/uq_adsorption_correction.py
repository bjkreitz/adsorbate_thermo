import glob
import pandas as pd
import numpy as np

Name='adsorptionPt111'
N_BEE=1

label=[]
index=[]

#This goes throug all the species list files that were used to construct the ensembles
#each file is for a specific group in the adsorptionPt111 file. The names have to match
groups=[]
for filename in glob.iglob('species_list_*.dat'):
    bits_info=filename.split('_')
    bits=bits_info[2].replace('.dat','')
    groups.append(bits)
    
#Cycle through the entire ensemble of BEEF values
for k in range(N_BEE):
    file="".join((Name,"_",str(k),".py"))
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
    for i in range(1,no):
        s=open(file,'r')
        new_file_content="" 
        idx="".join(("    index = ",str(index[i]),","))
        #When we look for the last script, we have to adjust the index since there is no i+1 for the switch. 
        if i==no-1:
            idx_next="".join(("    index = ",str(index[-1]+1),","))
        else:    
            idx_next="".join(("    index = ",str(index[i+1]),","))
        flag=False
        for line in s: 
            if idx in line:
                flag=True
                old=line.strip()
                new_line=line.replace(old,old)
                new_file_content += new_line 
                for line in s:
                    check=line.strip()
                    if check.startswith("H298=(") and flag:
                        old=line.strip()
                        bits_info=line.split(",")
                        bits=bits_info[0].strip().split("(")   
                        initial_H=float(bits[1])
                        
                        #No nitrogen chemistry at the moment, so these groups are not changed at all
                        #Whenever a group label is not in the list of groups for which ensembles are availabel
                        # the value is not changed
                        if str(label[i]) in groups:
                            filename='ensembles/'+ str(label[i]) + '_bee.txt'
                            data=pd.read_csv(filename, sep="\t", header=0)
                            perturbation=data.iloc[k,0]     
                            changed_H=np.round(initial_H+float(perturbation),2)
                        else:
                            print(label[i])
                            changed_H=initial_H
                            
                        modified=bits[0] + '(' + str(changed_H) + ',' +  bits_info[1] + ','
                        new_line=line.replace(old,modified)
                        new_file_content +=new_line
                        
                    elif idx_next in line:
                        flag=False  
                        old=line.strip()
                        new_line=line.replace(old,old)
                        new_file_content += new_line  
                    else:
                        old=line.strip()
                        new_line=line.replace(old,old)
                        new_file_content += new_line                             

            else:
                old=line.strip()
                new_line=line.replace(old,old)
                new_file_content += new_line                  
               
        s.close()
        writing_file = open(file, "w")
        writing_file.write(new_file_content)
        writing_file.close()  
        
## This is nice and clean!
