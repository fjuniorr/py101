#!/bin/bash

DIR="exercises/ch3-easy3"
N=10

if [ ! -d "$DIR" ]; then
  mkdir $DIR
fi

for i in $(seq 1 $N)
do
   cp template.md $DIR/ex$(printf %03d $i).md
done
