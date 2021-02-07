#!/bin/bash

for i in `seq 201 300`
do
    python script.py "xx$i.hcl"
done
