#!/bin/bash
#######################################################
#    Author:      <Ziyu Guo>
#    email:       <guo412>
#    ID:           <ee364d25>
#    Date:         <3/6>
#######################################################
DataPath=~ee364/DataFolder/Prelab09
substudent=$DataPath"/maps/students.dat"
cir=$(bash getCircuitsByProject.bash $1)
subcir=$DataPath"/circuits"
files=$(for f in $cir
do
    file=$subcir"/circuit_$f.dat"
    grep -E "[0-9]+-[0-9]" $file
done | sort -u)
(for i in $files
do
    grep -E $i $substudent| cut -f1 -d"|"
done | sort -u)