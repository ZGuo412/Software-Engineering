#!/bin/bash
#######################################################
#    Author:      <Ziyu Guo>
#    email:       <guo412>
#    ID:           <ee364d25>
#    Date:         <3/6>
#######################################################
DataPath=~ee364/DataFolder/Prelab09
subfile=$DataPath"/maps/projects.dat"
grep -E $1 $subfile |sort -u| cut -f5 -d" "