#!/bin/bash

awk -F '\",\"' 'NR==1 {a=$0; next} {b=$2".csv"} !($2 in c) {c[$2]; print a > b} {print >> b}' "../ex03/hh_positions.csv"