#!/bin/bash
#######################################################
#    Author:      <Ziyu Guo>
#    email:       <guo412>
#    ID:           <ee364d25>
#    Date:         <3/20>
#######################################################
DataPath=~ee364/DataFolder/Lab09
subpro=$DataPath"/maps/projects.dat"
subcir=$DataPath"/circuits"
ans=$(ls $subcir)
for f in $ans
do
    file=$subcir"/$f"
    check=$(wc -c $file| cut -f1 -d" ")
    if [ "$check" -ge "200" ]
    then
        echo $(wc -c $file | tail -c 12 | head -c 7)
    fi
done | sort -u