import numpy as np
import matplotlib.pyplot as plt
import barnaba as bb
import pandas as pd

def is_deeply_empty(nested_list):
  """
  Checks if a list is empty or contains only other empty lists, recursively.
  """
  if not isinstance(nested_list, list):
    # If the item is not a list (e.g., an integer, string, etc.), 
    # it means the container is not "only empty lists".
    return False
  
  # 'all()' returns True if the list is empty or all its elements are True.
  # We recursively call the function for each sub-item.
  return all(is_deeply_empty(item) for item in nested_list)


pdb = "center_dry.gro"

traj = 'opes_mol.xtc'

#Calculate stacking using barnaba
stackings, pairings, residues = bb.annotate(traj,pdb)

#open file to write
f1 = open('stacking_data.dat','w')
print("# stacked = 1; unstacked = 0",file=f1)
print("# Stacking style: (>>) Upward = 1; (<<) Downward = 2; (<>) Outward = 3; (><) Inward = 4.",file=f1)
print("# Columns: Frame Stacked(yes/no) Stacking_Style",file=f1)

num_frames = len(stackings)

for i in range(num_frames):
    if is_deeply_empty(stackings[i]) == True:
        #unstacked
        print(i,0,0,file=f1)
    else :
        #stacked --> check stacking style
        if stackings[i][1][0] == '>>':
            print(i,1,1,file=f1)
        elif stackings[i][1][0] == '<<':
            print(i,1,2,file=f1)
        elif stackings[i][1][0] == '<>':
            print(i,1,3,file=f1)
        elif stackings[i][1][0] == '><':
            print(i,1,4,file=f1)


f1.close()



# In[ ]:




