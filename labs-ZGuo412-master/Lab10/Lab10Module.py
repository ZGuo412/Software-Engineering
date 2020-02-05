#######################################################
#    Author:      <Ziyu Guo >
#    email:       <guo412@purdue.edu >
#    ID:           <ee364d25>
#    Date:         <2019/3/27>
#######################################################
import os
import sys
import csv
import re
from Lab10 import measurement
DataPath = os.path.expanduser('~ee364/DataFolder/Lab10')

def getCost(sourceZip, destinationZip):
    szip = sourceZip
    dzip = destinationZip
    coord_path = 'coordinates.dat'
    coord_path = os.path.join(DataPath, coord_path)
    with open(coord_path) as file:
        reader = csv.DictReader(file, delimiter = ',')
        la = [row[' "latitude"'] for row in reader]
    with open(coord_path) as file:
        reader = csv.DictReader(file, delimiter=',')
        lo = [row[' "longitude"'] for row in reader]
    with open(coord_path) as file:
        reader = csv.DictReader(file, delimiter=',')
        zip = [row['zip code'] for row in reader]
    with open(coord_path) as file:
        reader = csv.DictReader(file, delimiter=',')
        stateab = [row[' "state abbreviation"'] for row in reader]
    with open(coord_path) as file:
        reader = csv.DictReader(file, delimiter=',')
        city = [row[' "city"'] for row in reader]
    with open(coord_path) as file:
        reader = csv.DictReader(file, delimiter=',')
        state = [row[' "state"'] for row in reader]

    if sourceZip not in zip:
        return 0.00
    if destinationZip not in zip:
        return 0.00
    splace = zip.index(sourceZip)
    dplace = zip.index(destinationZip)
    szip = (float(la[splace][2:len(la[splace]) - 1]), float(lo[splace][2:len(lo[splace]) - 1]))
    dzip = (float(la[dplace][2:len(la[dplace]) - 1]), float(lo[dplace][2:len(lo[dplace]) - 1]))
    cost = measurement.calculateDistance(szip,dzip)
    cost = round(cost / 100,2)
    return cost
def loadPackages():
    pack_path = 'packages.dat'
    pack_path = os.path.join(DataPath, pack_path)
    with open(pack_path, 'r') as f:
        f.readline()
        data = f.readlines()
    city = list()
    source = list()
    des = list()
    for check in data:
        tempc = re.findall(r"\"([A-Za-z]+)\"", check)
        source.append(re.findall(r"([0-9]{5})\"\,",check)[0])
        des.append(re.findall(r"[\"A-Za-z0-9\s\,]+([0-9]{5})\"",check)[0])
        if tempc == []:
            tempc = re.findall(r"\"([A-Za-z]+\s[A-Za-z]+)\"",check)
        city.append(tempc[0])
    cost = [0.00] * len(source)
    for r in range(0, len(source)):
        print(source[r], des[r])
        cost[r] = getCost(str(source[r]),str(des[r]))
    print(cost)
    name = list()
class PackageGroup:
    pass
