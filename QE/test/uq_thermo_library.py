
import numpy as np
import pandas as pd

Name='surfaceThermoPt111_QE'
N_BEE=2

for k in range(N_BEE):
    label=[]
    index=[]
    
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
    print(no)
    for i in range(1,no): #
        #print(i)
        #print(label[i])
        #print(index[i])
        
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
                     if check.startswith("NASAPolynomial(coeffs=[") and flag:
                         old=line.strip()
                         bits=line.split("[")
                         thermo=bits[1].split("]")
                         polynom=thermo[0].split(",")
                         initial_H=float(polynom[5])
                         
                         #No nitrogen chemistry at the moment
                         if 'N' not in label[i]:
                             filename='ensembles/' + str(label[i]) + '_bee.txt'
                             data=pd.read_csv(filename, sep="\t", header=0)
                             perturbation=data.iloc[k,3]  
                             changed_H=initial_H+float(perturbation)/8.314e-3      
                         else:
                             changed_H=initial_H
                             print(label[i])
                         end=thermo[1].replace("\n","")

                         #Restore the polynomial first
                         modified="".join((polynom[0],",",polynom[1],",",polynom[2],",",polynom[3],",",polynom[4]," ,",str(changed_H),",",polynom[6]))
                         add_more="".join(("NASAPolynomial(coeffs=[", modified,"]", end))
                         new_line=line.replace(old,add_more)
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