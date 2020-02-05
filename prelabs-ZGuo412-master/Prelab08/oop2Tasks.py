#######################################################
#    Author:      <Ziyu Guo >
#    email:       <guo412@purdue.edu >
#    ID:           <ee364d25>
#    Date:         <2019/2/27>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import csv
import copy
import re
import math
from uuid import UUID
from pprint import pprint as pp
from enum import Enum
import collections
from statistics import mean
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

class Datum:
    def __init__(self, *args):
        for x in args:
            if (type(x)) is not float:
                raise TypeError("the input value should be float")
        self._storage = args

    def __str__(self):
        len_args = len(self._storage)
        temp = tuple([format(x, '.2f') for x in self._storage])
        str_args = ''
        for x in temp:
            str_args += x + ', '
        str_args = '(' + str_args[:len(str_args) - 2] + ')'
        return f"{str_args}"
    def __repr__(self):
        len_args = len(self._storage)
        temp = tuple([format(x, '.2f') for x in self._storage])
        str_args = ''
        for x in temp:
            str_args += x + ', '
        str_args = '(' + str_args[:len(str_args) - 2] + ')'
        return f"{str_args}"

    def __hash__(self):
        return hash(self._storage)

    def distanceFrom(self, temp):
        if not isinstance(temp, Datum):
            raise TypeError("only accepts a instance of Datum")
        len1 = len(self._storage)
        len2 = len(temp._storage)
        dis = list()
        if len1 >= len2:
            for i in range(0, len2):
                dis.append(self._storage[i] - temp._storage[i])
            for j in range(len2, len1):
                dis.append(self._storage[j])
        else:
            for i in range(0, len1):
                dis.append(self._storage[i] - temp._storage[i])
            for j in range(len1, len2):
                dis.append(temp._storage[j])
        dis = format(math.sqrt(sum([x**2 for x in dis])), '.2f')
        return float(dis)

    def clone(self):
        return copy.deepcopy(self)

    def __contains__(self, item):
        return item in [x for x in self._storage]

    def __len__(self):
        return len(self._storage)

    def __iter__(self):
        return iter(self._storage)

    def __neg__(self):
        return Datum(*tuple( -x if x > 0 else x for x in self._storage))

    def __getitem__(self, item):
        return self._storage[item]

    def __add__(self, other):
        if type(other) is not float:
            if not isinstance(other, Datum):
                raise TypeError("need an instance of Datum or float")
            len1 = len(self._storage)
            len2 = len(other._storage)
            lis = list()
            if len1 <= len2:
                lis = list(other._storage)
                for x in range(0, len1):
                    lis[x] += self._storage[x]
            else:
                lis = list(self._storage)
                for x in range(0, len2):
                    lis[x] += other._storage[x]
            return Datum(*tuple(lis))
        elif type(other) is float:
            res = self.__radd__(other)
            return res

    def __sub__(self, other):
        if type(other) is float:
            res = [x - other for x in self._storage]
            res = Datum(*tuple(res))
            return res
        if not isinstance(other, Datum):
            raise TypeError("need an instance of Datum or float")
        len1 = len(self._storage)
        len2 = len(other._storage)

        if len1 <= len2:
            lis = list(other._storage)
            for x in range(0, len1):
                lis[x] = self._storage[x] - lis[x]
            for y in range(len1, len2):
                lis[y] = -lis[y]
        else:
            lis = list(self._storage)
            for x in range(0, len2):
                lis[x] -= other._storage[x]
        return Datum(*tuple(lis))
    def __radd__(self, other):
        if type(other) is float:
            res = list()
            for x in self._storage:
                res.append(x + other)
            res = Datum(*tuple(res))
            return res
        else:
            raise TypeError("input should be a float")

    def __rsub__(self, other):
        res = [other - x for x in self._storage]
        res = Datum(*tuple(res))
        return res

    def __mul__(self, other):
        if isinstance(other, float):
            return Datum(*tuple([x * other for x in self._storage]))

    def __truediv__(self, other):
        if isinstance(other, float):
            return Datum(*tuple([x / other for x in self._storage]))
    def __rtruediv__(self, other):
        if isinstance(other, float):
            return Datum(*tuple([other / x for x in self._storage]))
    def __eq__(self, other):
        return self.distanceFrom(Datum(0.0)) == other.distanceFrom(Datum(0.0))
    def __ne__(self, other):
        return self.distanceFrom(Datum(0.0)) != other.distanceFrom(Datum(0.0))
    def __ge__(self, other):
        return self.distanceFrom(Datum(0.0)) >= other.distanceFrom(Datum(0.0))
    def __lt__(self, other):
        return self.distanceFrom(Datum(0.0)) < other.distanceFrom(Datum(0.0))
    def __gt__(self, other):
        return self.distanceFrom(Datum(0.0)) >= other.distanceFrom(Datum(0.0))
    def __le__(self, other):
        return self.distanceFrom(Datum(0.0)) <= other.distanceFrom(Datum(0.0))
class Data(collections.UserList):
    def __init__(self, initial = None):
        if initial is None:
            super(Data, self).__init__(list())
        else:
            for x in initial:
                if not isinstance(x, Datum):
                    raise TypeError("each element in the list should be the instance of Datum")
            super(Data, self).__init__(initial)
    def computeBounds(self):
        lis = self.data
        lenlis = [len(x._storage) for x in lis]
        max_len = max(lenlis)
        minT = [sys.float_info.max] * max_len
        maxT = [0.0] * max_len
        for i in range(0, max_len):
            for j in lis:
                if i >= len(j._storage):
                    minT[i] = 0.0
                else:
                    if j._storage[i] < minT[i]:
                        minT[i] = j._storage[i]
        for i in range(0, max_len):
            for j in lis:
                if i >= len(j._storage):
                    maxT[i] = 0.0
                else:
                    if j._storage[i] > maxT[i]:
                        maxT[i] = j._storage[i]
        return (Datum(*tuple(minT)), Datum(*tuple(maxT)))

    def computeMean(self):
        lis = self.data
        lenlis = [len(x._storage) for x in lis]
        max_len = max(lenlis)
        ans = [0.00] * max_len
        for x in range(0, max_len):
            for y in lis:
                if x >= len(y._storage):
                    ans[x] = ans[x]
                else:
                    ans[x] += y._storage[x]
        for i in range(0, len(ans)):
            ans[i] = ans[i] / len(lis)
        return(Datum(*tuple(ans)))


    def append(self, item):
        if not isinstance(item, Datum):
            raise TypeError("need an instance of Datum")
        super.append(item)
    def count(self, item):
        if not isinstance(item, Datum):
            raise TypeError("need an instance of Datum")
        super.count(item)
    def index(self, item, *args):
        if not isinstance(item, Datum):
            raise TypeError("need an instance of Datum")
        super.index(item, *args)
    def insert(self, i,item):
        if not isinstance(item, Datum):
            raise TypeError("need an instance of Datum")
        super.insert(i,item)
    def remove(self, item):
        if not isinstance(item, Datum):
            raise TypeError("need an instance of Datum")
        super.remove(item)
    def __setitem__(self, key, value):
        if not isinstance(value, Datum):
            raise TypeError("need an instance of Datum")
        super.__setitem__(key, value)
    def extend(self, other):
        if not isinstance(other, Data):
            raise TypeError("input should be an instance of Data")
        super.extend(other)

class DataClass(Enum):
    Class1 = 1
    Class2 = 2

class DataClassifier:
    def __init__(self, group1, group2):
        if group1 is None or group2 is None:
            raise ValueError("input cannot be empty")
        elif not isinstance(group1, Data) or not isinstance(group2, Data):
            raise TypeError("each input should be an instance of Data")
        self._class1 = group1
        self._class2 = group2

    def classify(self, item):
        dis1 = self._class1.computeMean()._storage
        dis2 = self._class2.computeMean()._storage
        dis1 = item.distanceFrom(Datum(*dis1))
        dis2 = item.distanceFrom(Datum(*dis2))

        if dis1 > dis2:
            return DataClass.Class2
        else:
            return DataClass.Class1
