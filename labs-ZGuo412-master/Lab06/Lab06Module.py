#######################################################
#    Author:      <Ziyu Guo >
#    email:       <guo412@purdue.edu >
#    ID:           <ee364d25>
#    Date:         <2019/2/20 >
#######################################################
import re
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

def extractArguments(commandline):
    sub_cc = re.findall(r"[\\+]([a-z])\s+([^\s\\+]+)",commandline)
    sub_cc.sort()     #I am not sure about what sort mean: whether it means that the tuples appear first in the commandline or just sort my result. I asked the TA, and TA told me that just sort my result.
    return sub_cc

def extractNumerics(sentence):
    test = re.findall(r"([^\s]+)", sentence)
    res = list()
    pattern1 = r"([-+]?[0-9]+\.[0-9]+[eE][-+][0-9]+)"
    pattern2 = r"([-+]?[0-9]+\.[0-9]+)"
    pattern3 = r"([-+]?[0-9]+)"
    for case in test:
        if re.findall(pattern1, case):
            res.append(re.findall(pattern1, case)[0])
        elif re.findall(pattern2, case):
            res.append(re.findall(pattern2, case)[0])
        elif re.findall(pattern3, case):
            res.append(re.findall(pattern3, case)[0])

    return res