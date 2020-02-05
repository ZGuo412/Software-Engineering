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
size=$(for f in $ans
do
    file=$subcir"/$f"
    echo $(wc -c $file)
done | sort -u)
large=$(echo $size | tail -c 12| head -c 7)
grep -E $large $subpro | sort -u | cut -f15 -d" "
