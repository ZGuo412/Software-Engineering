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
cir=$(bash getCircuitsByStudent.bash $1)
subpro=$DataPath"/maps/projects.dat"
ans=$(for f in $cir
do
    grep -E $f $subpro |cut -f15 -d" "
done |sort -u)

for i in $ans
do
    echo $i
done