#!/bin/bash

find . -type f -name "*.png" -delete
foamCleanTutorials

> log.timer

cd RANS
cd KEpsilon_highRE_V1_g1
sh run_timer.sh
cd ..

cd KEpsilon_highRE_V1_g2
sh run_timer.sh
cd ..

cd KEpsilon_LaunderSharma_lowRE_V1_g1
sh run_timer.sh
cd ..

cd KEpsilon_LaunderSharma_lowRE_V1_g2
sh run_timer.sh
cd ..

cd KEpsilon_realizable_highRE_g1
sh run_timer.sh
cd ..

cd KEpsilon_realizable_highRE_g2
sh run_timer.sh
cd ..

cd KOmegaSST_highRE_g1
sh run_timer.sh
cd ..

cd KOmegaSST_highRE_g2
sh run_timer.sh
cd ..

cd KOmegaSST_lowRE_V1_g1
sh run_timer.sh
cd ..

cd KOmegaSST_lowRE_V1_g2
sh run_timer.sh
cd ..

cd no_TM_g1
sh run_timer.sh
cd ..

cd no_TM_g2
sh run_timer.sh
cd ..

cd SA_LRN_g1
sh run_timer.sh
cd ..

cd SA_LRN_g2
sh run_timer.sh
cd ..
cd ..

cd SRS
cd DES_KO_HRN_g1
sh run_timer.sh
cd ..

cd DES_KO_HRN_g2
sh run_timer.sh
cd ..

cd DES_KO_LRN_g1
sh run_timer.sh
cd ..

cd DES_KO_LRN_g2
sh run_timer.sh
cd ..

cd DES_SA_LRN_g1
sh run_timer.sh
cd ..

cd DES_SA_LRN_g2
sh run_timer.sh
cd ..

cd LES-WALE_HRN_g1
sh run_timer.sh
cd ..

cd LES-WALE_HRN_g2
sh run_timer.sh
cd ..

LES-WALE_LRN_g1
sh run_timer.sh
cd ..

LES-WALE_LRN_g2
sh run_timer.sh
cd ..
cd ..


