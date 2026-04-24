#!/bin/bash

source ~/source_gpu_gromacs.sh

export OMP_NUM_THREADS=2

for i in {1..3}
do
	cp -r template run$i
	cd run$i
	cp ../stacked_$i.gro .
	gmx_mpi grompp -f prod.mdp -c stacked_$i.gro -p dinic_solvated.top -n index.ndx -o prod.tpr -maxwarn 1
	mpiexec -n 1 gmx_mpi mdrun -s prod.tpr -deffnm opes -nsteps 100000000 -plumed plumed.dat -pin on -pinoffset 0 -gpu_id 0
	cd ..
done
