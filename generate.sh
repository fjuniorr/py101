#!/bin/bash

DIR="lesson3/hard1"
N=5

if [ ! -d "$DIR" ]; then
  mkdir $DIR
fi

for i in $(seq 1 $N)
do
   cp template.md $DIR/ex$(printf %03d $i).md
done
