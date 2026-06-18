 #!/bin/bash

nprocs=16
foamDictionary system/decomposeParDict -entry numberOfSubdomains -set $nprocs

decomposePar
mpirun -np $nprocs foamRun -parallel | tee log.solver

#foamRun | tee log.solver

