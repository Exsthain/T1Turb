#!/bin/bash

> log.timer

cd laminar
run_timer.sh
cd ..

cd turbulent_planar
run_timer.sh
cd ..

cd turbulent_wedge
run_timer.sh
cd ..

