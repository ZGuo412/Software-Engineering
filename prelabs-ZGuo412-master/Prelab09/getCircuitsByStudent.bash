#!/bin/bash
#######################################################
#    Author:      <Ziyu Guo>
#    email:       <guo412>
#    ID:           <ee364d25>
#    Date:         <3/6>
#######################################################
DataPath=~ee364/DataFolder/Prelab09
substudent=$DataPath"/maps/students.dat"
subcir=$DataPath"/circuits"
id=$(grep -s -E $1 $substudent | cut -f2 -d"|")
ans=$(grep -lr -E $id $subcir)
d_ans=$(for f in $ans
do
    echo $f | cut -d"/" -f9 |tail -c 12
done| sort -u| cut -f1 -d".")
for i in $d_ans
do
    echo $i
done
