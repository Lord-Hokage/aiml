#!/bin/bash

# Check if there is a file name provided
if [ $# -eq 0 ]
then
    echo "No file name provided"
    exit 1
fi
fil="files/${1}.txt"

cat $fil
printf "\n\n    "