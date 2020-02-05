#######################################################
#    Author:      <Ziyu Guo >
#    email:       <guo412@purdue.edu >
#    ID:           <ee364d25>
#    Date:         <2019/1/18 >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import csv

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('~ee364/DataFolder/Prelab02')
def readfile(symbol, number, dat, price):
    if number != 4:
        d_path = symbol+ '.dat'

        if d_path not in os.listdir(DataPath):
            return None
    else:
        d_path = symbol
    path = os.path.join(DataPath, d_path)
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        close = [row['close'] for row in reader]
        close = close[1:]
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        date = [row['date'] for row in reader]
        date = date[1:]
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        volume = [row['volume'] for row in reader]
        volume = volume[1:]
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        opent = [row['open'] for row in reader]
        opent = opent[1:]
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        high = [row['high'] for row in reader]
        high = high[1:]
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        low = [row['low'] for row in reader]
        low = low[1:]
    if number is 1:
        diff = [0] * len(high)
        num = 0
        diff[0] = abs(float(high[0]) - float(low[0]))
        Maxv = diff[0]
        for i in range(1,len(high)):
            diff[i] = float(high[i]) - float(low[i])
            if diff[i] > Maxv:
                Maxv = (diff[i])
                num = i
        return date[num]
    elif number is 2:
        num2 = 0
        for i in range(0,len(close)):
            if float(close[i]) > float(opent[i]):
                num2 = num2 + 1
        return ('%.4f'%(float(num2) * 100/ len(close)))
    elif number is 4:
        for i in range(0,len(date)):
            if dat == date[i]:
                return ('%.4f'%(((float(close[i]) - float(opent[i])) * 100) / float(opent[i])))
    elif number is 5:
        avg = 0
        numb = 0
        for i in range(0, len(date)):
            if str(dat) in date[i]:
                avg = avg + (float(close[i]) + float(opent[i])) / 2
                numb = numb + 1
        avg = avg / numb
        return ('%.4f'%(avg))
    elif number is 3:
        date2 = price
        start = 0
        end = 0
        sum = 0
        for i in range(0, len(date)):
            if (dat == date[i]):
                end = i + 1
                break
            if (date2 == date[i]):
                start = i
        for j in range(start,end):
            sum = sum + float(volume[j])
            sum = int(sum)
        return sum
    elif number is 6:
        count = 0
        for i in range(0,len(date)):
            if float(close[i]) >= price:
                if float(opent[i]) >= price:
                    if float(low[i]) >= price:
                        if float(high[i]) >= price:
                            count = count + 1
        return count



def getMaxDifference(symbol):
    date = readfile(symbol,1,0,0)
    return date
def getGainPercent(symbol):
    percent = readfile(symbol,2,0,0)
    return percent
def getVolumeSum(symbol, date1, date2):
    if date1 < date2:
        sum = readfile(symbol,3,date1,date2)
        return sum
    else:
        return None
def getBestGAIN(date):
    files = os.listdir(DataPath)
    Gain = [0] * len(files)
    for i in range(0,len(files)):
        Gain[i] = readfile(files[i],4,date,0)
    return max(Gain)
def getAveragePrice(symbol, year):
    Price = readfile(symbol,5,year,0)
    return Price
def getCountOver(symbol, price):
    count = readfile(symbol, 6, 0, price)
    return count