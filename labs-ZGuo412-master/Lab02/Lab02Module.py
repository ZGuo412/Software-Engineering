import os
import sys
import csv
DataPath = os.path.expanduser('~ee364/DataFolder/Lab02')

def getCodeFor(stateName):
    path1 = 'zip.dat'
    path2 = 'coordinates.dat'
    zip_path = os.path.join(DataPath, path1)
    coord_path = os.path.join(DataPath, path2)
    with open(zip_path) as file:
        reader = csv.DictReader(file, delimiter = ' ')
        state = [row['State'] for row in reader]
        state = state[1:]
    f = open(zip_path, 'r')
    zip = f.readlines()
    zip = zip[2:]
    for i in range(0, len(zip)):
        zip[i] = zip[i][len(zip[i]) - 6:len(zip[i]) - 1]
    start = 0
    end = 0
    for j in range(0, len(state)):
        if stateName == state[j]:
            start = j
            break
    for m in range(start, len(state)):
        if stateName != state[m]:
            end = m
            break
    zip = zip[start:end]
    zip = sorted(zip)
    return zip

def getMinLatitude(stateName):
    zip = getCodeFor(stateName)
    path = 'coordinates.dat'
    coord_path = os.path.join(DataPath, path)
    with open(coord_path) as file:
        reader = csv.DictReader(file, delimiter = ' ')
        la = [row['Latitude'] for row in reader]
        la = la[1:]
    min_la = max(la)
    f = open(coord_path, 'r')
    nzip = f.readlines()
    nzip = nzip[2:]
    for i in range(0, len(nzip)):
        nzip[i] = nzip[i][len(nzip[i]) - 6:len(nzip[i]) - 1]
    for j in range(0, len(nzip)):
        if nzip[j] in zip:
            if la[j] < min_la:
                min_la = la[j]
    min_la = float(min_la)
    return min_la

def getMaxLongitude(stateName):
    zip = getCodeFor(stateName)
    path = 'coordinates.dat'
    coord_path = os.path.join(DataPath, path)
    f = open(coord_path, 'r')
    nzip = f.readlines()
    nzip = nzip[2:]
    for i in range(0, len(nzip)):
        nzip[i] = nzip[i][len(nzip[i]) - 6:len(nzip[i]) - 1]
    f = open(coord_path, 'r')
    lo = f.readlines()
    lo = lo[2:]
    for j in range(0, len(lo)):
        lo[j] = lo[j][16:24]
    max_lo = max(lo)
    for n in range(0, len(nzip)):
        if nzip[n] in zip:
            if lo[n] < max_lo:
                max_lo = lo[n]
    max_lo = float(max_lo)

    return max_lo