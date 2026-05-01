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

traj = 'merged.xtc'

#Calculate stacking using barnaba
stackings, pairings, residues = bb.annotate(traj,pdb)


#open file to write
#f1 = open('stacking_data.dat','w')
#print("# unstacked = 0; stacked = 1; inward = 2; only 0-1 stacked = 3; only 1-2 stacked = 4; outward = 5",file=f1)
#print("# Stacking style: (>>) Upward = 1; (<<) Downward = 2; (<>) Outward = 3; (><) Inward = 4.",file=f1)
#print("# Columns: Frame Stacked(yes/no)",file=f1)

unstacked = []
upward = []
downward = []
inward = []
outward = []


num_frames = len(stackings)

for i in range(num_frames):
    if is_deeply_empty(stackings[i]) == True:
        #unstacked
        unstacked.append(i)
    else :
        #stacked --> check stacking style
        if stackings[i][1][0] == '>>':
            upward.append(i)
        elif stackings[i][1][0] == '<<':
            downward.append(i)
        elif stackings[i][1][0] == '<>':
            outward.append(i)
        elif stackings[i][1][0] == '><':
            inward.append(i)

#save frames from trajectory
import mdtraj as md

traj = md.load(traj, top=pdb)

#unstacked
unstacked_frames = traj[unstacked]
unstacked_frames.save('unstacked.xtc')

#upward
upward_frames = traj[upward]
upward_frames.save('upward_stacked.xtc')

#downward
downward_frames = traj[downward]
downward_frames.save('downward_stacked.xtc')

#inward
inward_frames = traj[inward]
inward_frames.save('inward_stacked.xtc')

#outward
outward_frames = traj[outward]
outward_frames.save('outward_stacked.xtc')
