#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('~ee364/DataFolder/Prelab01')
def find(pattern) :
    path = os.path.join(DataPath, 'sequence.txt')
    f = open(path)
    data = f.read()
    length_data = len(data)
    length_pattern = len(pattern)
    res1 = [0] * length_data
    count = 0
    if(length_pattern > length_data) :
        return
    for i in range(0, length_data - length_pattern):
        for j in range(0, length_pattern):
            if data[i + j] is not pattern[j]:
               if pattern[j] is not 'X':
                    break
            if j == length_pattern - 1:
                res1[count] = data[i:i + length_pattern]
                count = count + 1
    res1 = res1[0:count]
    f.close()
    print(res1)

def getStreakProduct(sequence, maxSize, product):
    t_pro: int = 1
    count = 0
    num = 0
    res2 = [0] * 2**len(sequence)
    for i in range(0,len(sequence)):
        while int(t_pro) < int(product):
            num = num + 1
            t_pro = t_pro * int(sequence[i])
            if t_pro == product:
                if num <= maxSize:
                    res2[count] = sequence[i - num + 1: i + 1]
                    count = count + 1
            i = i + 1
            if i == len(sequence):
                break
        num = 0
        t_pro = 1
    res2 = res2[0:count]
    print(res2)

def writePyramids(filePath, baseSize, count, char):
    f = open(filePath,'w+')
    depth = int((baseSize) / 2) + 1
    for i in range(depth,0,-1):
        num = 1 + 2 * (depth - i)
        space = " " * (i - 1)
        py_char = char * num
        pyr = (space + py_char + space + " ") * (count - 1)
        pyr = pyr + space + py_char + space
        f.writelines([pyr,'\n'])
    f.close()

def getStreaks(sequence, letters):
    res4 = [0]*len(sequence)
    count = 0
    num = 0
    i_loop = 0
    while i_loop < len(sequence):
        if i_loop != len(sequence) - 1:
            while sequence[i_loop] is sequence[i_loop + 1]:
                count = count + 1
                i_loop = i_loop + 1
        for j in range(0,len(letters)):
            if sequence[i_loop] is letters[j]:
                res4[num] = sequence[i_loop - count:i_loop + 1]
                num = num + 1
        i_loop = i_loop + 1
        count = 0
    res4 = res4[0:num]
    print(res4)

def findNames(nameList, part, name):
    name = name.lower()
    if part == "F":
        name = name + " "
    if part == "L":
        name = " " + name
    if part != "FL":
        if part != "F":
            if part != "L":
                return []
    res5 = [0] * len(nameList)
    count = 0
    for i in range(0, len(nameList)):
        nameList[i] = nameList[i].lower()
        if nameList[i].find(name) != -1:
            check = 0
            if part == "F":
                if nameList[i][0:len(name)] == name:
                    res5[count] = nameList[i].title()
                    count = count + 1
            elif part == "L":
                if nameList[i][len(nameList[i]) - len(name) : len(nameList[i])] == name:
                    res5[count] = nameList[i].title()
                    count = count + 1
            elif part == "FL":
                if nameList[i][len(name)] == " ":
                    res5[count] = nameList[i].title()
                    count = count + 1
                elif nameList[i][len(nameList[i]) - len(name) - 1] == " ":
                    res5[count] = nameList[i].title()
                    count = count + 1
    return res5[0:count]


def convertToBoolean(num, size):
    res6 = ['X']
    if type(num) is not int:
        return []
    elif type(size) is not int:
            return []
    while(num != 0):
        bool = num % 2
        num = int(num / 2)
        res6.append(str(bool))
    if len(res6) - 1 > size:
        size = len(res6) - 1
    r_res6 = [True] * size
    for i in range (0,size):
        if res6[len(res6) - 1 - i] == '1':

            r_res6[i] = True
        else:
            r_res6[i] = False
    print(r_res6)

def convertToInteger(boolList):
    if type(boolList) is not list:
        return None
    for j in range(0,len(boolList)):
        if type(boolList[j]) is not bool:
            return None
    if boolList == []:
        return None
    while(boolList[0] == False):
        boolList = boolList[1:]
    res7: int = 0
    size = len(boolList) - 1
    for i in range(0,len(boolList)):
        if boolList[i] == True:
            res7 = res7 + 2**size
            size = size - 1
        else:
            size = size - 1
    return res7

if __name__ == "__main__":
    writePyramids("temp.txt",10,3,"a")
