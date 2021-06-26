import subprocess
from math import *
from statistics import *
import os
import itertools
import shutil
path="./"
geometry_list = [mol for mol in  os.listdir() if mol.endswith("xyz") and mol.startswith("res")]
def remove_similar(list_of_molecules):
#    geometry_list = [mol for mol in  os.listdir() if mol.endswith("xyz")]
    final_list = list_of_molecules[:]
    for a, b in itertools.combinations(list_of_molecules, 2):
        rmsd=float(subprocess.getoutput('calculate_rmsd {} {}'.format(a,b)))
        if rmsd < 0.5:
#            if energy_difference < 1:
            if a in final_list:
                 final_list.remove(a)
            else:
                if b in final_list:
                    final_list.remove(b)#taken from clustering module
    print(final_list)
    dst_dir="unique_geom"
    if os.path.isdir(dst_dir):
        pass
    else:
        os.mkdir(dst_dir)
    for file in final_list:
        file=os.path.join(path,file)
        shutil.copy(file,dst_dir)
remove_similar(geometry_list)
