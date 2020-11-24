#Usage python3 bond_length.py xyz_file_name first_atom_number second_atom_number
import math
import os
import sys
if len(sys.argv)<4:
    sys.exit("Insufficient arguments;correct usage python3 bond_length.py xyz_file_name first_atom_number second_atom_number")
with open(sys.argv[1],'r') as f:
    f=f.readlines()
    i,j=int(sys.argv[2]),int(sys.argv[3])
    line_first=f[i+1].split()
    print('Coordinates of first atom\n{}'.format(line_first))
    line_second=f[j+1].split()
    print('Coordinates of second atom\n{}'.format(line_second))
    rms=math.sqrt((float(line_first[1])-float(line_second[1]))**2+(float(line_first[2])-float(line_second[2]))**2+(float(line_first[3])-float(line_second[3]))**2)
#    coord_second=float(line_second[1])**2+float(line_second[2])**2+float(line_second[3])**2
    print('Distance between the atoms: {:.3f}'.format(rms))
    
else:
    print("none")
