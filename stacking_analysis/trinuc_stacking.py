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


pdb = "center_dry_renamed.gro"

traj = 'opes_mol.xtc'

#Calculate stacking using barnaba
stackings, pairings, residues = bb.annotate(traj,pdb)

for data in stackings:
    print(data)

#open file to write
f1 = open('stacking_data.dat','w')
print("# unstacked = 0; stacked = 1; cc_stacked = 2; only 0-1 stacked = 3; only 1-2 stacked = 4; intercalated = 5",file=f1)
#print("# Stacking style: (>>) Upward = 1; (<<) Downward = 2; (<>) Outward = 3; (><) Inward = 4.",file=f1)
print("# Columns: Frame Stacked(yes/no)",file=f1)

num_frames = len(stackings)

for i in range(num_frames):
    if is_deeply_empty(stackings[i]) == True:
        #unstacked
        print(i,0,file=f1)
    else :
        #stacked or intercalated --> check which one
        if stackings[i][0] == [[0, 1]]:
            print(i,3,file=f1)
        elif stackings[i][0] == [[1, 2]]:
            print(i,4,file=f1)
        elif stackings[i][0] == [[0, 2]]:
            print(i,2,file=f1)
        elif stackings[i][0] == [[0, 1], [1, 2]]:
            print(i,1,file=f1)
        elif stackings[i][0] == [[0, 2], [1, 2]] or stackings[i][0] == [[0, 1], [0, 2]]:
            print(i,5,file=f1)
        else :
            print(i,6,file=f1)


f1.close()




