#!/bin/bash

for i in `seq 401 500`
do
    python script.py "xx$i.hcl"
done
