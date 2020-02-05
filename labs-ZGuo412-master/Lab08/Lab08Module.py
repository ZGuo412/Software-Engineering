#######################################################
#    Author:      <Ziyu Guo >
#    email:       <guo412@purdue.edu >
#    ID:           <ee364d25>
#    Date:         <2019/3/6 >
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
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

class TimeSpan:
    def __init__(self, weeks, days, hours):
        if weeks < 0 or days < 0 or hours < 0:
            raise ValueError("The arguments cannot be negative")
        act_hour = hours % 24
        days = days + hours // 24
        act_days = days % 7
        weeks = weeks + days // 7
        self.weeks = weeks
        self.days = act_days
        self.hours = act_hour

    def __str__(self):
        if self.hours < 10:
            s_hour = '0' + str(self.hours)
        else:
            s_hour = str(self.hours)
        if self.weeks < 10:
            s_weeks = '0' + str(self.weeks)
        else:
            s_weeks = str(self.weeks)
        return f"{s_weeks}W {str(self.days)}D {s_hour}H"

    def __repr__(self):
        if self.hours < 10:
            s_hour = '0' + str(self.hours)
        else:
            s_hour = str(self.hours)
        if self.weeks < 10:
            s_weeks = '0' + str(self.weeks)
        else:
            s_weeks = str(self.weeks)
        return f"{s_weeks}W {str(self.days)}D {s_hour}H"

    def getTotalHours(self):
        return self.weeks * (7 * 24) + self.days * 24 + self.hours

    def __add__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("An TImeSPan instance is expected")
        return(TimeSpan(self.weeks + other.weeks, self.days + other.days, self.hours + other.hours))

    def __mul__(self, other):
        if type(other) is not int and type(other) is not float:
            raise TypeError("an integer or a float is expected")
        if other <= 0:
            raise ValueError("the value should be greater than 0")
        if type(other) is int:
            return(TimeSpan(self.weeks * other, self.days * other, self.hours * other))
        else:
            weeks = self.weeks * other
            rest_d = (weeks - int(weeks)) * 7
            days = self.days * other + rest_d
            rest_h = (days - int(days)) * 24
            hours = self.hours * other
            rest_h = hours + rest_h
            if rest_h - int(rest_h) >= 0.5:
                rest_h = math.ceil(rest_h)
            else:
                rest_h = math.floor(rest_h)
            return(TimeSpan(int(weeks), int(days), rest_h))

    def __eq__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("an TimeSpan instance is expected")
        return self.getTotalHours() == other.getTotalHours()
    def __ne__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("an TimeSpan instance is expected")
        return self.getTotalHours() != other.getTotalHours()
    def __le__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("an TimeSpan instance is expected")
        return self.getTotalHours() <= other.getTotalHours()
    def __lt__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("an TimeSpan instance is expected")
        return self.getTotalHours() < other.getTotalHours()
    def __ge__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("an TimeSpan instance is expected")
        return self.getTotalHours() >= other.getTotalHours()
    def __gt__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("an TimeSpan instance is expected")
        return self.getTotalHours() > other.getTotalHours()