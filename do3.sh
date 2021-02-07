#!/bin/bash

for i in `seq 601 700`
do
    python script.py "xx$i.hcl"
done
