#!/bin/bash

> log.timer

foamCleanTutorials

echo "run_mesh.sh" >> log.timer
time -p sh run_mesh.sh > /dev/null 2>> log.timer

echo "run_solver.sh" >> log.timer
time -p sh run_solver.sh > /dev/null 2>> log.timer

echo "run_gnuplot.sh" >> log.timer
time -p sh run_gnuplot.sh > /dev/null 2>> log.timer

timeout -s INT 30s pyFoamPlotWatcher.py --hardcopy --format-of-hardcopy=png log.solver

