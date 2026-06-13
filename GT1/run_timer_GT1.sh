#!/bin/bash

find . -type f -name "*.png" -delete
foamCleanTutorials

> log.timer

cd laminar
sh run_timer.sh
cd ..

cd turbulent_planar
sh run_turbulent_planar.sh
cd ..

cd turbulent_wedge
sh run_timer.sh
cd ..

