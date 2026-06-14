#!/bin/bash

find . -type f -name "*.png" -delete
foamCleanTutorials

> log.timer

cd RANS-kklo
sh run_timer.sh
cd ..

cd RANS-kOmegaSSTLM
sh run_timer.sh
cd ..

cd setup_TM
cd LES-smagorinsky
sh run_timer.sh
cd ..

cd LES-wale
sh run_timer.sh
cd ..

cd RANS-koSSTv1
sh run_timer.sh
cd ..

cd RANS-koSSTv2
sh run_timer.sh
cd ..

cd RANS-launderSharmaKE
sh run_timer.sh
cd ..

cd RANS-liencubickE
sh run_timer.sh
cd ..

cd RANS-realizableKE
sh run_timer.sh
cd ..

cd RANS-rngKE
sh run_timer.sh
cd ..

cd RANS-SA
sh run_timer.sh
cd ..
cd ..
