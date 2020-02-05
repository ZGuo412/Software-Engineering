#!/bin/bash
#######################################################
#    Author:      <Ziyu Guo>
#    email:       <guo412>
#    ID:           <ee364d25>
#    Date:         <3/20>
#######################################################
DataPath=~ee364/DataFolder/Lab09
substudent=$DataPath"/maps/students.dat"
subcir=$DataPath"/circuits"
id=$(grep -s -E $1 $substudent | cut -f2 -d"|")
ans=$(grep -lr -E $id $subcir)
for f in $ans
do
    grep -E "[A-Z]{3}-[0-9]{3}" $f | cut -f3 -d" "
done| sort -u