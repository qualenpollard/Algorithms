#!/bin/bash

for i in 10 20 30 40 50 60 70 80 90 100
do
    python3 stable_matching_2800144.py sm_${i}.txt > sm_${i}.out
done