#!/bin/bash

for i in `seq 501 600`
do
    python script.py "xx$i.hcl"
done
