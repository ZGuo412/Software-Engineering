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
ans=$(grep -lr -E $1 $subcir)
wc -w <<< "$ans"
