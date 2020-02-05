#######################################################
#    Author:      <Ziyu Guo >
#    email:       <guo412@purdue.edu >
#    ID:           <ee364d25>
#    Date:         <2019/4/17 >
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
from Lab14 import measurement
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

DataPath = os.path.expanduser('~ee364/DataFolder/Lab14')

class Direction(Enum):
    Incoming = 1
    Outgoing = 2
    Both = 3

class Leg:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        szip = re.findall(r"([0-9]{5})",self.source)[0]
        dzip = re.findall(r"([0-9]{5})",self.destination)[0]
        return f"{szip} => {dzip}"

    def calculateLength(self, locationMap):
        szip = re.findall(r"([0-9]{5})",self.source)[0]
        dzip = re.findall(r"([0-9]{5})",self.destination)[0]
        sour = locationMap[szip]
        des = locationMap[dzip]
        len = measurement.calculateDistance(sour, des)
        return round(len,2)

class Trip:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def calculateLength(self, locationMap):
        total = 0
        for leg in self.legs:
            total = total + leg.calculateLength(locationMap)
        return total

    def getLegsByZip(self, zip, direction):
        ans = list()
        dir = direction.name
        if dir == 'Incoming':
            for leg in self.legs:
                if zip in leg.destination:
                    ans.append(leg)
        elif dir == 'Outgoing':
            for leg in self.legs:
                if zip in leg.source:
                    ans.append(leg)
        elif dir == 'Both':
            for leg in self.legs:
                if zip in leg.source or zip in leg.destination:
                    ans.append(leg)
        return ans

    def getLegsByState(self,state, direction):
        ans = list()
        dir = direction.name
        if dir == 'Incoming':
            for leg in self.legs:
                if state in leg.destination:
                    ans.append(leg)
        elif dir == 'Outgoing':
            for leg in self.legs:
                if state in leg.source:
                    ans.append(leg)
        elif dir == 'BOth':
            for leg in self.legs:
                if state in leg.source or state in leg.destination:
                    ans.append(leg)
        return ans

    def __add__(self, other):
        type = True ####leg
        if not isinstance(other, Leg):
            type = False  ####trip
            if not isinstance(other, Trip):
                raise TypeError("the input should be either an instance of Leg or Trip")
        if type == True:
            length = len(self.legs)
            if self.legs[length - 1].destination != other.source:
                raise ValueError("source place of the leg should be the same as the des of the last leg in the trip")

            else:
                temp = copy.copy(self.legs)
                return Trip(self.name,temp.append(other))

        elif type == False:
            if self.name != other.name:
                raise ValueError("name of two trips should be the same")
            else:
                ans = copy.copy(self)
                for leg in other.legs:
                    ans = ans + leg
                return ans

class RoundTrip(Trip):
    def __init__(self, name, legs):
        super().__init__(name, legs)
        if len(legs) < 2:
            raise ValueError("a trip should contains two or more legs")
        if legs[0].source != legs[len(legs) - 1].destination:
            raise ValueError("the source place of the first should be the same as the last one's")

def getShortestTrip(source, destination,stops):
    szip = re.findall(r"([0-9]{5})",source)[0]
    dzip = re.findall(r"([0-9]{5})",destination)[0]
    ans = list()
    for stop in stops:
        stopzip = re.findall(r"([0-9]{5})",stop)[0]
        ans.append(getCost(szip, stopzip) + getCost(stopzip, dzip))
    final = ans.index(min(ans))
    l1 = Leg(source, stops[final])
    l2 = Leg(stops[final], destination)
    return Trip('',[l1,l2])

def getTotalDistanceFor(person):
    tripath = os.path.join(DataPath,'trips.dat')
    with open(tripath, 'r') as f:
        data = f.readlines()
    names = list()
    places = list()
    for x in data:
        x = x.replace('\n','')
        x = x.split('"')
        names.append(x[1])
        places.append(x[3:])
    ans = 0
    for name in names:
        if person == name:
            ind = names.index(name)
            true_place = list()
            for x in places[ind]:
                if re.findall(r"([0-9]{5})", x) != []:
                    true_place.append(re.findall(r"([0-9]{5})", x)[0])
            for i in range(0, len(true_place) - 2):
                ans = ans + getCost(true_place[i], true_place[i + 1])

    return ans

def getRoundTripCount():
    ans = 0
    tripath = os.path.join(DataPath, 'trips.dat')
    with open(tripath, 'r') as f:
        data = f.readlines()
    names = list()
    places = list()
    for x in data:
        x = x.replace('\n', '')
        x = x.split('"')
        names.append(x[1])
        places.append(x[3:])
    for x in places:
        true_place = list()
        for y in x:
            if re.findall(r"([0-9]{5})", y) != []:
                true_place.append(re.findall(r"([0-9]{5})", y)[0])
        if true_place[0] == true_place[len(true_place) - 1]:
                ans = ans + 1
    return ans

def getCost(sourceZip, destinationZip):
    szip = sourceZip
    dzip = destinationZip
    temp = list()
    coorpath = os.path.join(DataPath,'locations.dat')
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
    return round(ans, 2)