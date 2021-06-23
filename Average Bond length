#!/usr/env/python3
import os
from math import *
from statistics import *
cn_max=12 #for FCC lattice
cutoff=3#cutoff bond length for identifying coordination
with open('gm.xyz','r') as f:
    f=f.readlines()
    lines=f[2:len(f)]
def dist_calc(atom_1,atom_2):
    atom_1=atom_1.split()
    atom_2=atom_2.split()
    for j in range(1,4):
        atom_1[j]=float(atom_1[j])
        atom_2[j]=float(atom_2[j])
    dist=sqrt((abs(atom_1[1]-atom_2[1])**2+abs(atom_1[2]-atom_2[2])**2+abs(atom_1[3]-atom_2[3])**2))
    return dist

j=0
bond_list=[]
unique_list=[]
for i in lines:
    for j in lines:
        if i!=j:
            bond_length=dist_calc(i,j)
            if bond_length<cutoff:
                bond_list.append(bond_length)
for i in bond_list:
    if i not in unique_list:
        unique_list.append(i)
coord_list=[round(i,2) for i in unique_list]
print(coord_list)
print('Average Pt-Pt Bond length: ',round(mean(coord_list),2))
