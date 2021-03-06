import shutil,os
import numpy as np
import pandas as pd
import sys
import itertools
path="./"
dst_path="./analysis"
for dir in os.listdir(path):
        if os.path.isdir(dir):
                dir_path=os.path.join(path,dir)
                for file in os.listdir(dir_path):
                        if file=='xtbopt.xyz':
                                file_path=os.path.join(dir_path,file)
                                shutil.copy(file_path,os.path.join(dst_path,dir+'.xyz'))
os.chdir(dst_path)
print(os.getcwd())
def read_energy_from_xyz_file(xyz_file):
    import re
    with open(xyz_file, 'r') as fr:
        comments_line = fr.readlines()[1].rstrip()
    return float(re.split(':|=|\s+', comments_line)[3]) #taken from clustering module

geometry_list = [mol for mol in  os.listdir() if mol.endswith("xyz")]
def remove_similar(list_of_molecules):
    geometry_list = [mol for mol in  os.listdir() if mol.endswith("xyz")]
    final_list = list_of_molecules[:]
    for a, b in itertools.combinations(list_of_molecules, 2):
        energy_difference = read_energy_from_xyz_file(a)-read_energy_from_xyz_file(b)
        if abs(energy_difference) < 1e-6:
#            if energy_difference < 1:
             if a in final_list:
                 final_list.remove(a)
             else:
                if b in final_list:
                    final_list.remove(b)#taken from clustering module
#    print(geometry_list)
#    print(final_list)
    for geometry in geometry_list:
        if geometry not in final_list:
            os.remove(os.path.join(path,geometry))

remove_similar(geometry_list)


def create_dataframe():
    mol_list = [mol for mol in  os.listdir() if mol.endswith("xyz")]
    energy_list = [read_energy_from_xyz_file(mol) for mol in mol_list]
    orient_list = [mol.split('-')[0] for mol in mol_list]
    freq_list = [mol.split('-')[1] for mol in mol_list]
    dict = {"Geometry Name":mol_list,"Orient":orient_list,"Freq":freq_list,"Energy":energy_list}
    s = pd.DataFrame(dict)
    s['RE(eV)'] = (s['Energy']-s['Energy'].min())*27.2114
    pd.set_option('max_colwidth',100)
    s = s.round(decimals=3)
    blankIndex = [''] * len(s)
    s.index = blankIndex
    print(s)

create_dataframe()

