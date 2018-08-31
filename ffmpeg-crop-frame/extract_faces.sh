#!/usr/bin/env bash

new_path="extracted_files"
mkdir -p $new_path

# Extract train data
files=('real-train' 'real-test' 'attack-print-allsupports-train' 'attack-print-allsupports-test')
for new_file in ${files[@]};
do
    i=0
    output="$new_path/$new_file"
    mkdir -p $output
    i=0; 
    for vid in $(cat "protocols/$new_file.txt"); 
    do 
        echo "python extract_faces.py $vid $output $i"; 
        ((i++)); 
    done
done
