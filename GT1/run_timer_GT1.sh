#!/bin/bash

> log.timer

cd laminar
run_timer.sh
cd ..

cd turbulent_planar
run_turbulent_planar.sh
cd ..

cd turbulent_wedge
run_timer.sh
cd ..

