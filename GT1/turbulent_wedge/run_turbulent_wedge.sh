#!/bin/bash

cd turbulent_wedge_kE
cd turbulent_wedge_kE_HRN_WF
cd turbulent_wedge_kE_HRN_WF_high_I
sh run_timer.sh
cd ..

cd turbulent_wedge_kE_HRN_WF_low_I
sh run_timer.sh
cd ..
cd ..

cd turbulent_wedge_kE_noWF
cd turbulent_wedge_kE_noWF_high_I
sh run_timer.sh
cd ..

cd turbulent_wedge_kE_noWF_low_I
sh run_timer.sh
cd ..
cd ..
cd ..

cd turbulent_wedge_kO
cd turbulent_wedge_kO_HRN_WF
cd turbulent_wedge_kO_HRN_WF_high_I
sh run_timer.sh
cd ..

cd turbulent_wedge_kO_HRN_WF_low_I
sh run_timer.sh
cd ..
cd ..

cd turbulent_wedge_kO_noWF
cd turbulent_wedge_kO_noWF_high_I
sh run_timer.sh
cd ..

cd turbulent_wedge_kO_noWF_low_I
sh run_timer.sh
cd ..
cd ..
cd ..

