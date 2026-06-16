 #!/bin/bash

nprocs=16
foamDictionary system/decomposeParDict -entry numberOfSubdomains -set $nprocs

decomposePar
mpirun -np $nprocs foamRun -parallel | tee log.solver

#foamRun | tee log.solver

reconstructPar

#simpleFoam -postProcess -func wallShearStress -noZero -noFunctionObjects -latestTime
foamPostProcess -solver incompressibleFluid -func wallShearStress -noZero -noFunctionObjects -latestTime

foamPostProcess -func sampleDict0 -latestTime -noZero

foamPostProcess -func probesDict0 -latestTime -noZero

foamPostProcess -func surfacesDict0 -latestTime -noZero
python3 uPyP.py
