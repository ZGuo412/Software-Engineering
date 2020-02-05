#######################################################
#    Author:      <Ziyu Guo >
#    email:       <guo412@purdue.edu >
#    ID:           <ee364d25>
#    Date:         <2019/2/15 >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import csv
import copy
import re
from uuid import UUID
from pprint import pprint as pp
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('~ee364/DataFolder/Prelab06')





def getUrlParts(url):
    sub_url = re.findall(r"[/]{2}.*\?", url)
    parts = re.findall(r"[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-z]+",sub_url[0])[0]
    other_o = re.findall(r"(\/[a-zA-Z0-9]+\/)",sub_url[0])[0]
    other_o = other_o[1:len(other_o) - 1]
    other_t = re.findall(r"(\/[a-zA-Z0-9]+\?)",sub_url[0])[0]
    other_t = other_t[1:len(other_t) - 1]
    ans = parts, other_o, other_t
    return ans

def getQueryParameters(url):
    sub_url = re.findall(r"(\?.*)", url)[0][1:]
    parts = re.findall(r"([A-Za-z0-9\.\-\_]+\=)", sub_url)
    parts_o = re.findall(r"(\=[A-Za-z0-9\.\-\_]+)", sub_url)
    res = [('','')] * len(parts)
    for i in range(0, len(parts)):
        res[i] = parts[i][0:len(parts[i]) - 1],parts_o[i][1:]
    return res

def getSpecial(sentence, letter):
    case1 = re.findall(r"[A-Za-z]+",sentence)
    res = list()
    for case2 in case1:
        if re.findall(r"\w+%c\b"%letter, case2, re.IGNORECASE) != []:
            if re.findall(r"\b%c\w+"%letter, case2, re.IGNORECASE) == []:
                res.append(case2)
        elif re.findall(r"\b%c\w+"%letter, case2, re.IGNORECASE) != []:
            res.append(case2)
    return res


def getRealMac(sentence):
    ass = re.findall(r"([a-fA-F0-9]{2}\-[a-fA-F0-9]{2}\-[a-fA-F0-9]{2}\-[a-fA-F0-9]{2}\-[a-fA-F0-9]{2}\-[a-fA-F0-9]{2})", sentence)
    if ass == []:
        ass = re.findall(r"([a-fA-F0-9]{2}\:[a-fA-F0-9]{2}\:[a-fA-F0-9]{2}\:[a-fA-F0-9]{2}\:[a-fA-F0-9]{2}\:[a-fA-F0-9]{2})",sentence)
    if ass != []:
        return ass
    return None

def getRejectedEntries():
    path = 'Employees.txt'
    path = os.path.join(DataPath, path)
    with open(path, 'r') as f:
        data = f.readlines()
    name = list()
    for check in data:
        temp = re.findall(r"(^[a-zA-Z]+\s[a-zA-Z]+)[\,\;\s]+\n", check)
        if temp == []:
            temp = re.findall(r"(^[a-zA-Z]+)\,\s([a-zA-Z]+)[\,\;\s]+\n", check)
            if temp != []:
                Last, First = temp[0]
                name.append(First + ' ' + Last)
        else:
            name.append(temp[0])
    name.sort()
    return name

def getEmployeesWithIDs():
    path = 'Employees.txt'
    path = os.path.join(DataPath, path)
    with open(path, 'r') as f:
        data = f.readlines()
    name_dict = list()
    id_dict = list()
    for check in data:
        id = re.findall(r"([a-zA-Z0-9\-]{36})",check)
        if id != []:
            id_dict.append(id[0])
            temp = re.findall(r"(^[a-zA-Z]+\s[a-zA-Z]+)", check)
            if temp == []:
                temp = re.findall(r"(^[a-zA-Z]+)\,\s([a-zA-Z]+)", check)
                if temp != []:
                    Last, First = temp[0]
                    name_dict.append(First + ' ' + Last)
            else:
                name_dict.append(temp[0])
        else:
            id = re.findall(r"([a-zA-Z0-9]{32})", check)
            if id != []:
                id = '{' + id[0] + '}'
                id = str(UUID(id))
                id_dict.append(id)
                temp = re.findall(r"(^[a-zA-Z]+\s[a-zA-Z]+)", check)
                if temp == []:
                    temp = re.findall(r"(^[a-zA-Z]+)\,\s([a-zA-Z]+)", check)
                    if temp != []:
                        Last, First = temp[0]
                        name_dict.append(First + ' ' + Last)
                else:
                    name_dict.append(temp[0])
    ans = dict(zip(name_dict, id_dict))
    return ans


def getEmployeesWithoutIDs():
    path = 'Employees.txt'
    path = os.path.join(DataPath, path)
    with open(path, 'r') as f:
        data = f.readlines()
    name_dict = list()
    for check in data:
        id = re.findall(r"([a-zA-Z0-9\-]{36})",check)
        if id == []:
            id = re.findall(r"([a-zA-Z0-9]{32})", check)
            if id == []:
                temp = re.findall(r"(^[a-zA-Z]+\s[a-zA-Z]+)", check)
                if temp == []:
                    temp = re.findall(r"(^[a-zA-Z]+)\,\s([a-zA-Z]+)", check)
                    if temp != []:
                        Last, First = temp[0]
                        name_dict.append(First + ' ' + Last)
                else:
                    name_dict.append(temp[0])
    re_name = getRejectedEntries()
    res = list()
    for i in name_dict:
        if i not in re_name:
            res.append(i)
    res.sort()
    return res

def getEmployeesWithPhones():
    path = 'Employees.txt'
    path = os.path.join(DataPath, path)
    with open(path, 'r') as f:
        data = f.readlines()
    name_dict = list()
    phone_dict = list()

    for check in data:
        phone = re.findall(r"([0-9]{10});", check)
        if phone != []:
            phone = '(' + phone[0][0:3] + ') ' + phone[0][3:6] + '-' + phone[0][6:]
            phone_dict.append(phone)
            temp = re.findall(r"(^[a-zA-Z]+\s[a-zA-Z]+)", check)
            if temp == []:
                temp = re.findall(r"(^[a-zA-Z]+)\,\s([a-zA-Z]+)", check)
                if temp != []:
                    Last, First = temp[0]
                    name_dict.append(First + ' ' + Last)
            else:
                name_dict.append(temp[0])
        elif re.findall(r"([0-9]{3}-[0-9]{3}-[0-9]{4})", check) != []:
            phone = re.findall(r"([0-9]{3}-[0-9]{3}-[0-9]{4})", check)[0]
            phone_dict.append('(' + phone[0:3] + ') ' + phone[4:])
            temp = re.findall(r"(^[a-zA-Z]+\s[a-zA-Z]+)", check)
            if temp == []:
                temp = re.findall(r"(^[a-zA-Z]+)\,\s([a-zA-Z]+)", check)
                if temp != []:
                    Last, First = temp[0]
                    name_dict.append(First + ' ' + Last)
            else:
                name_dict.append(temp[0])
        elif re.findall(r"(\([0-9]{3}\)\s[0-9]{3}-[0-9]{4})", check) != []:
            phone_dict.append(re.findall(r"(\([0-9]{3}\)\s[0-9]{3}-[0-9]{4})", check)[0])
            temp = re.findall(r"(^[a-zA-Z]+\s[a-zA-Z]+)", check)
            if temp == []:
                temp = re.findall(r"(^[a-zA-Z]+)\,\s([a-zA-Z]+)", check)
                if temp != []:
                    Last, First = temp[0]
                    name_dict.append(First + ' ' + Last)
            else:
                name_dict.append(temp[0])
    res = dict(zip(name_dict, phone_dict))
    return res


def getEmployeesWithStates():
    path = 'Employees.txt'
    path = os.path.join(DataPath, path)
    with open(path, 'r') as f:
        data = f.readlines()
    states_dict = list()
    name_dict = list()
    for check in data:
        if re.findall(r"([A-Za-z]+\s[A-Za-z]+)\n", check) != []:
            states_dict.append(re.findall(r"([A-Za-z]+\s[A-Za-z]+)\n", check)[0])
            temp = re.findall(r"(^[a-zA-Z]+\s[a-zA-Z]+)", check)
            if temp == []:
                temp = re.findall(r"(^[a-zA-Z]+)\,\s([a-zA-Z]+)", check)
                if temp != []:
                    Last, First = temp[0]
                    name_dict.append(First + ' ' + Last)
            else:
                name_dict.append(temp[0])
        elif re.findall(r"([A-Za-z]+)\n", check) != []:
            states_dict.append(re.findall(r"([A-Za-z]+)\n", check)[0])
            temp = re.findall(r"(^[a-zA-Z]+\s[a-zA-Z]+)", check)
            if temp == []:
                temp = re.findall(r"(^[a-zA-Z]+)\,\s([a-zA-Z]+)", check)
                if temp != []:
                    Last, First = temp[0]
                    name_dict.append(First + ' ' + Last)
            else:
                name_dict.append(temp[0])
    res = dict(zip(name_dict, states_dict))
    return res


def getCompleteEntries():
    id = getEmployeesWithIDs()
    phone = getEmployeesWithPhones()
    states = getEmployeesWithStates()
    res = {}
    for name in id:
        if name in phone.keys():
            if name in states.keys():
                res[name] = id[name], phone[name], states[name]
    return res
