#!/bin/bash

find . -type f -name "*.png" -delete
foamCleanTutorials

> log.timer

cd GT1
sh run_timer_GT1.sh
cd ..

cd GT2
sh run_timer_GT2.sh
cd ..

cd GT3
sh run_timer_GT3.sh
cd ..
