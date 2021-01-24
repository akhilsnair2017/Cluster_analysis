import os
from math import *
from statistics import *
cn_max=12 #for FCC lattice
cutoff=3#cutoff bond length for identifying coordination
with open('opt.xyz','r') as f:
    f=f.readlines()
    lines=f[2:12]

def dist_calc(atom_1,atom_2):
    atom_1=atom_1.split()
    atom_2=atom_2.split()
    for j in range(1,4):
        atom_1[j]=float(atom_1[j])
        atom_2[j]=float(atom_2[j])
    dist=sqrt((abs(atom_1[1]-atom_2[1])**2+abs(atom_1[2]-atom_2[2])**2+abs(atom_1[3]-atom_2[3])**2))
    return dist

j=0
for i in range(len(lines)):
    dist=[]
    for j in range(len(lines)):
        if i!=j:
            dist.append(dist_calc(lines[i],lines[j]))
            dist_list=[round(x,2) for x in dist]
    coord_list=[x for x in dist_list if x<=cutoff]
    coord_number='CN: {}'.format(len(coord_list))
    coord_list.append(coord_number)
    print(coord_list)
