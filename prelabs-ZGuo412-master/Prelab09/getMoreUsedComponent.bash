#!/bin/bash
#######################################################
#    Author:      <Ziyu Guo>
#    email:       <guo412>
#    ID:           <ee364d25>
#    Date:         <3/6>
#######################################################
count1=$(bash getComponentUses.bash $1)
count2=$(bash getComponentUses.bash $2)
if [ "$count1" \> "$count2" ]
then
    echo $1
else
    echo $2
fi