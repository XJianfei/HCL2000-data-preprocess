#!/bin/bash

for i in `seq 300 400`
do
    python script.py "xx$i.hcl"
done
