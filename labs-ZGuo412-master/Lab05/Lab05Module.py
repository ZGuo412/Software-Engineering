import os
import sys
import csv
import copy
from pprint import pprint as pp




DataPath = os.path.expanduser('~ee364/DataFolder/Lab05')


def _readfiles(num, var1, var2):
    people_path = 'people.dat'
    people_path = os.path.join(DataPath, people_path)
    with open(people_path, 'r') as file:
        file.readline()
        file.readline()
        data = file.readlines()
        data_split = [m.split() for m in data]
        name = [''] * len(data_split)
        ID = [''] * len(data_split)
        for i in range(0, len(data_split)):
            name[i] = data_split[i][0] + ' ' + data_split[i][1]
            ID[i] = data_split[i][3]
    name_id = dict(zip(name,ID))
    id_name = dict(zip(ID, name))

    pin_path = 'pins.dat'
    pin_path = os.path.join(DataPath,pin_path)
    with open(pin_path, 'r') as file:
        data = file.readlines()
    data_split = [m.split() for m in data]
    pin_key = data_split[1]
    data_split = data_split[3:]

    log_path = 'log.dat'
    log_path = os.path.join(DataPath,log_path)
    with open(log_path, 'r') as file:
        file.readline()
        file.readline()
        file.readline()
        data = file.readlines()
    log_data = [m.split() for m in data]
    resource = set()
    log_id = set()

    if num == '4':
        date = var1
        for case4 in log_data:
            if date == case4[0]:
                resource.add(case4[2])
        if resource == set():
            raise ValueError("date does not exist")
        return resource
    if num == '3':
        date = var1
        for case3 in log_data:
            if date == case3[0]:
                log_id.add(case3[3])
        if log_id == set():
            raise ValueError("date does not exist")
        users = set()
        for user in log_id:
            users.add(getUserOf(user, date))
        return users
    if num == '1':
        name_1 = var1
        date = var2
        if name_1 not in name_id:
            raise ValueError("name does not exist")
        id = name_id[name_1]
        if date not in pin_key:
            raise ValueError("date not in the file")
        date_code = pin_key.index(date)
        for case1 in data_split:
            if id == case1[0]:
                return case1[date_code]
    if num == '2':
        date = var2
        pin = var1
        if date not in pin_key:
            raise ValueError("date not in the file")
        date_code = pin_key.index(date)
        for case2 in data_split:
            if pin == case2[date_code]:
                id = case2[0]
                name_2 = id_name[id]
                return name_2
        raise ValueError("code does not exist")

    if num == '5':
        dates = var1
        id_count = {}
        for date in dates:
            for case5 in log_data:
                if date == case5[0]:
                    id_count[case5[3]] = 0
        for date in dates:
            for case5 in log_data:
                if date == case5[0]:
                    id_count[case5[3]] +=1
        keys = list(id_count.keys())
        values = list(id_count.values())
        place = values.index(max(values))
        case5_id = keys[place]
        dates = list(dates)
        for date in dates:
            date_code = pin_key.index(date)
            for case2 in data_split:
                if case5_id == case2[date_code]:
                    id = case2[0]
                    name_2 = id_name[id]
                    return name_2

    if num == '6':
        dates = var1
        re_count = {}
        for date in dates:
            for case5 in log_data:
                if date == case5[0]:
                    re_count[case5[2]] = 0
        for date in dates:
            for case5 in log_data:
                if date == case5[0]:
                    re_count[case5[2]] +=1
        keys = list(re_count.keys())
        values = list(re_count.values())
        place = values.index(max(values))
        return keys[place]

    if num == '7':
        need_uid = set()
        for uid in data_split:
            need_uid.add(uid[0])
        abs = set()
        for all in ID:
            if all not in need_uid:
                abs.add(id_name[all])
        return abs
def getPinFor(name, date):
    code = _readfiles('1', name, date)
    return code


def getUserOf(pin, date):
    name = _readfiles('2', pin, date)
    return name

def getUsersOn(date):
    users = _readfiles('3', date, '')
    return users

def getResourcesOn(date):
    resource = _readfiles('4', date, '')
    return resource

def getMostActiveUserOn(dates):
    name = _readfiles('5', dates, '')
    return name

def getMostAccessedOn(dates):
    re = _readfiles('6', dates, '')
    return re


def getAbsentUsers():
    abs = _readfiles('7','','')
    return abs

def getDifference(slot1, slot2):
    slot_path = 'slots.dat'
    slot_path = os.path.join(DataPath, slot_path)
    with open (slot_path, 'r') as file:
        file.readline()
        data = file.readlines()
        data_split = [m.split() for m in data]
        time = data_split[0]
        info = data_split[2:]
        place1 = time.index(slot1)
        place2 = time.index(slot2)
        count1 = 0
        count2 = 0
        for i in info:
            if i[place1] == '1':
                count1 += 1
            if i[place2] == '1':
                count2 += 1
        diff = abs(count1 - count2)
        return diff