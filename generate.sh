#!/bin/bash

DIR="exercises/ch1-easy1"
N=11

if [ ! -d "$DIR" ]; then
  mkdir $DIR
fi

for i in $(seq 1 $N)
do
   cp template.md $DIR/ex$(printf %03d $i).md
done
