import parmed as pmd

dinic = pmd.load_file("dinic_solv.prmtop","dinic_solv.inpcrd")

dinic.save("dinic_solvated.top", format='gromacs')
dinic.save("dinic_solvated.gro")
