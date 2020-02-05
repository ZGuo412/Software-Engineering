import os
import sys
import csv
import copy
from pprint import pprint as pp




DataPath = os.path.expanduser('~ee364/DataFolder/Lab04')


def readfiles(number, var1, var2):
    pro_path = os.path.expanduser('~ee364/DataFolder/Lab04/providers')
    pro_list = os.listdir(pro_path)
    if number == '1':
        var1 = var1 + '.dat'
        var2 = var2 + '.dat'
        if var1 not in pro_list:
            raise ValueError('the first provider does not in the folder')
        elif var2 not in pro_list:
            raise ValueError('the second provider does not in the folder')
        place1 = pro_list.index(var1)
        place2 = pro_list.index(var2)
        pro_1 = os.path.join(pro_path, pro_list[place1])
        pro_2 = os.path.join(pro_path, pro_list[place2])
        with open(pro_1, 'r') as file:
            file.readline()
            file.readline()
            file.readline()
            data = file.readlines()
            data_split = [m.split() for m in data]
            name1 = [''] * len(data_split)
            for i in range(0, len(data_split)):
                name1[i] = data_split[i][0] + ' ' + data_split[i][1]
        with open(pro_2, 'r') as file:
            file.readline()
            file.readline()
            file.readline()
            data = file.readlines()
            data_split = [m.split() for m in data]
            name2 = [''] * len(data_split)
            for i in range(0, len(data_split)):
                name2[i] = data_split[i][0] + ' ' + data_split[i][1]
        diff = set('')
        for x in range(0,len(name1)):
            if name1[x] not in name2:
                diff.add(name1[x])
        return diff
    elif number == '2':
        name = var1
        var2 = var2 + '.dat'
        if var2 not in pro_list:
            raise ValueError('provider does not in the file')
        pro_path = os.path.join(pro_path, var2)
        with open(pro_path, 'r') as file:
            file.readline()
            file.readline()
            file.readline()
            data = file.readlines()
            data_split = [m.split() for m in data]
            pro_name = [''] * len(data_split)
            for i in range(0, len(data_split)):
                pro_name[i] = data_split[i][0] + ' ' + data_split[i][1]
                if pro_name[i] == name:
                    return data_split[i][3][1:]
            raise ValueError('the provider does not carry the SBC request')

    elif number == '3':
        sbcSet = list(var1)
        tur= [(0, '')] * len(sbcSet)
        for i in range(0, len(sbcSet)):
            for pro in pro_list:
                pro_path = os.path.expanduser('~ee364/DataFolder/Lab04/providers')
                pro_path = os.path.join(pro_path, pro)
                with open(pro_path, 'r') as file:
                    file.readline()
                    file.readline()
                    file.readline()
                    data = file.readlines()
                    data_split = [m.split() for m in data]
                    pro_name = [''] * len(data_split)
                    for j in range(0, len(data_split)):
                        pro_name[j] = data_split[j][0] + ' ' + data_split[j][1]
                        if pro_name[j] == sbcSet[i]:
                            price,_ = tur[i]
                            if price == 0:
                                tur[i] = float(data_split[i][3][1:]), pro[:9]
                            else:
                                tur[i] = min(price, float(data_split[i][3][1:])), pro[:9]
        min_price = dict(zip(sbcSet, tur))
        return min_price

def getDifference(provider1, provider2):
    sbc_names = readfiles('1',provider1, provider2)
    return sbc_names

def getPriceOf(sbc, provider):
    price = readfiles('2', sbc, provider)
    return price


def checkAllPrices(sbcSet):
    min_price = readfiles('3', sbcSet, '')
    return min_price

def getFilter():
    phone_path = os.path.expanduser('~ee364/DataFolder/Lab04/phones.dat')
    with open(phone_path, 'r') as file:
        reader = csv.DictReader(file)
        phone = [row['Phone Number'] for row in reader]
    test_phone = copy.copy(phone)
    for i in range(0, len(test_phone)):
        test_phone[i] = test_phone[i].replace('(','')
        test_phone[i] = test_phone[i].replace(')', '')
        test_phone[i] = test_phone[i].replace(' ', '')
        test_phone[i] = test_phone[i].replace('-', '')
    f_phone = list()
    case = list()
    for k in range(0,999):
        j = copy.copy(k)
        if j < 10:
            j = '0' + '0' + str(j)
        elif j < 100:
            j = '0' + str(j)
        j = str(j)
        count = 0

        for m in range(0, len(test_phone)):
            if count > 1:
                f_phone = f_phone[0:len(f_phone) - 1]
                case = case[0:len(case) - 1]
                break
            if j in test_phone[m]:
                f_phone.append(phone[m])
                case.append(j)
                count += 1
    match = dict(zip(case, f_phone))
    return match