#######################################################
#    Author:      <Ziyu Guo >
#    email:       <guo412@purdue.edu >
#    ID:           <ee364d25>
#    Date:         <2019/4/10 >
#######################################################
import os
from uuid import UUID
from pprint import pprint as pp
from enum import Enum
import sys     # Each  one on a line
import csv
import copy
import re
import math
from Lab13 import measurement
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('~ee364/DataFolder/Lab13')
def getCost(sourceZip, destinationZip):
    szip = sourceZip
    dzip = destinationZip
    temp = list()
    coorpath = os.path.join(DataPath,'coordinates.dat')
    with open(coorpath, 'r') as f:
        f.readline()
        data = f.readlines()
    for x in data:
        x = x.replace("\"", "")
        x = x.replace(" ","")
        x = x.replace('\n','')
        temp.append(x.split(','))
    sour = 0,0
    des = 0,0
    for y in temp:
        if y[0] == szip:
            sour = float(y[2]),float(y[3])
        if y[0] == dzip:
            des = float(y[2]),float(y[3])
    ans = measurement.calculateDistance(sour,des)
    return round(ans/100, 2)

def loadPackages():
    packpath = os.path.join(DataPath,'packages.dat')
    with open(packpath, 'r') as f:
        f.readline()
        data = f.readlines()
    temp = list()
    for x in data:
        temp.append(x.split("\""))
    company = list()
    sadd = list()
    dadd = list()
    for y in temp:
        company.append(y[1])
        sadd.append(re.findall(r".+([0-9]{5})",y[3]))
        dadd.append(re.findall(r".+([0-9]{5})",y[5]))
    cost = list()
    for x in range(0, len(company)):
        cost.append(getCost(sadd[x][0],dadd[x][0]))
    dicost = dict(zip(company,cost))
    company.sort()
    r_cost = list()
    for i in company:
        r_cost.append(dicost[i])
    return

class Package:
    def __init__(self,name,sadd,dadd):
        self.company = name
        self.source = sadd
        self.destination = dadd
        temp_s = re.findall(r".+([0-9]{5})",self.source)
        temp_d = re.findall(r".+([0-9]{5})",self.destination)
        self.cost = getCost(temp_s,temp_d)
    def __str__(self):
        temp_s = re.findall(r".+([0-9]{5})", self.source)
        temp_d = re.findall(r".+([0-9]{5})", self.destination)
        return f"{temp_s} => {temp_d}, Cost = ${self.cost}"

    def __add__(self, other):
        if not isinstance(other, Package):
            raise TypeError("input should be a package instance")
        if other.company != self.company:
            raise ValueError("input should belong to the same company")
        return PackageGroup(self.company,[self,other])
    def gcost(self):
        return self.cost

    def __eq__(self, other):
        if not isinstance(other, Package):
            raise TypeError("input should be a package instance")
        return self.cost == other.cost
    def __ne__(self, other):
        if not isinstance(other, Package):
            raise TypeError("input should be a package instance")
        return self.cost != other.cost
    def __lt__(self, other):
        if not isinstance(other, Package):
            raise TypeError("input should be a package instance")
        return self.cost < other.cost
    def __gt__(self, other):
        if not isinstance(other, Package):
            raise TypeError("input should be a package instance")
        return self.cost > other.cost
    def __le__(self, other):
        if not isinstance(other, Package):
            raise TypeError("input should be a package instance")
        return self.cost <= other.cost
    def __ge__(self, other):
        if not isinstance(other, Package):
            raise TypeError("input should be a package instance")
        return self.cost >= other.cost
class PackageGroup:
    def __init__(self,name, packagelist):
        self.packages = sorted(packagelist, key=Package.gcost, reverse=True)
        self.company = name
        temp = 0
        for x in self.packages:
            temp = temp + x.cost
        self.cost = round(temp,2)

    def __str__(self):
        return f"{self.company}, {len(self.packages)}, Shipments, Cost = ${self.cost}"

    def getByZip(self,zips):
        zips = list(zips)
        if zips == []:
            raise ValueError("the input can not be empty")
        ans = list()
        for x in self.packages:
            temp_s = re.findall(r".+([0-9]{5})", x.source)
            temp_d = re.findall(r".+([0-9]{5})", x.destination)
            if temp_s in zips:
                ans.append(x)
            elif temp_d in zips:
                ans.append(x)
        return ans
    def getByState(self,state):
        state = list(state)
        if  state == []:
            raise ValueError("the input can not be empty")
        ans = list()
        for x in self.packages:
            temp_s = re.findall(r"\,.([A-Za-z]{2})", x.source)
            temp_d = re.findall(r"\,.([A-Za-z]{2})", x.destination)
            if temp_s in state:
                ans.append(x)
            elif temp_d in state:
                ans.append(x)
        return ans
    def getByCity(self,citys):
        citys = list(citys)
        if  citys == []:
            raise ValueError("the input can not be empty")
        ans = list()
        for x in self.packages:
            temp_s = re.findall(r"\,.([A-Za-z]+)\,", x.source)
            temp_d = re.findall(r"\,.([A-Za-z]+)\,", x.destination)
            if temp_s in citys:
                ans.append(x)
            elif temp_d in citys:
                ans.append(x)
        return ans
    def __contains__(self, item):
        if not isinstance(item, Package):
            raise TypeError("input should be a package instance")
        check = False
        for x in self.packages:
            if x.company == item.company:
                if x.source == item.source:
                    if x.destination == item.destination:
                        check = True
        return check

    def __add__(self, other):
        if not isinstance(other, Package):
            raise TypeError("input should be a package instance")
        if self.company != other.company:
            raise ValueError("should be in the same company")
        if self.__contains__(other):
            return self
        else:
            return PackageGroup(self.company,self.packages.extend(other))