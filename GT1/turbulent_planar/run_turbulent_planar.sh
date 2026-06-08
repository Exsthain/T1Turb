#!/bin/bash

cd turbulent_planar_kE
cd turbulent_planar_kE_HRN_WF
cd turbulent_planar_kE_HRN_WF_high_I
sh run_timer.sh
cd ..

cd turbulent_planar_kE_HRN_WF_low_I
sh run_timer.sh
cd ..
cd ..

cd turbulent_planar_kE_noWF
cd turbulent_planar_kE_noWF_high_I
sh run_timer.sh
cd ..

cd turbulent_planar_kE_noWF_low_I
sh run_timer.sh
cd ..
cd ..
cd ..

cd turbulent_planar_kO
cd turbulent_planar_kO_HRN_WF
cd turbulent_planar_kO_HRN_WF_high_I
sh run_timer.sh
cd ..

cd turbulent_planar_kO_HRN_WF_low_I
sh run_timer.sh
cd ..
cd ..

cd turbulent_planar_kO_noWF
cd turbulent_planar_kO_noWF_high_I
sh run_timer.sh
cd ..

cd turbulent_planar_kO_noWF_low_I
sh run_timer.sh
cd ..
cd ..
cd ..

