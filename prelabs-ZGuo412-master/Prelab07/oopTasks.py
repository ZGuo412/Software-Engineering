#######################################################
#    Author:      <Ziyu Guo >
#    email:       <guo412@purdue.edu >
#    ID:           <ee364d25>
#    Date:         <2019/2/20>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import csv
import copy
import re
from uuid import UUID
from pprint import pprint as pp
from enum import Enum
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################


class Level(Enum):
    Freshman = 1
    Sophomore = 2
    Junior = 3
    Senior = 4

class ComponentType(Enum):
    Resistor = 'R'
    Capacitor = 'C'
    Inductor = 'I'
    Transistor = 'T'

class Student:
    def __init__(self, ID, first, last, level):
        self.ID = ID
        self.firstName = first
        self.LastNmae = last
        self.level = level
        if not isinstance(level, Level):
        #if self.level not in Level.__members__:      #question one
            raise TypeError("The argument must be an instance of the 'Level' Enum.")

    def __str__(self):
        return f"{self.ID}, {self.firstName} {self.LastNmae}, {self.level.name}"


class Component:
    def __init__(self, ID, ctype, price):
        self.ID = ID
        self.ctype = ctype
        self.price = float(format(float(price), '.2f'))
        if not isinstance(ctype, ComponentType):
            raise TypeError("The argument must be an instance of the 'ComponentType' Enum.")

    def __str__(self):
        return f"{self.ctype.name}, {self.ID}, ${format(self.price,'.2f')}"

    def __hash__(self):   #question 4
        return hash(self.ID)


class Circuit:
    def __init__(self, ID, components):
        self.ID = ID
        self.components = components
        cost = 0
        for x in self.components:
            cost += x.price
        self.cost = cost
        for check in self.components:
            if not isinstance(check, Component):
                raise TypeError("The argument must be an instance of the 'ComponentType' Enum")

    def __str__(self):
        numR = len([x for x in self.components if x.ctype == ComponentType.Resistor])
        if numR < 10: numR = '0' + str(numR)
        numC = len([x for x in self.components if x.ctype == ComponentType.Capacitor])
        if numC < 10: numC = '0' + str(numC)
        numI = len([x for x in self.components if x.ctype == ComponentType.Inductor])
        if numI < 10: numI = '0' + str(numI)
        numT = len([x for x in self.components if x.ctype == ComponentType.Transistor])
        if numT < 10: numT = '0' + str(numT)
        return f"{self.ID}: (R = {numR}, C = {numC}, I = {numI}, T = {numT}), Cost = ${format(self.cost, '.2f')}"
    #question 3 getByType function
    def __contains__(self, item):
        if not isinstance(item, Component):
            raise TypeError("The argument must be an instance of the 'ComponentType' Enum")
        return item in self.components

    def __add__(self, other):
        if not isinstance(other, Component):
            raise TypeError("The argument must be an instance of the 'ComponentType' Enum")
        if other in self.components:
            return self
        else:
            self.components.add(other)
            self.cost = self.cost + other.price
            return self
    def __sub__(self, other):
        if not isinstance(other, Component):
            raise TypeError("The argument must be an instance of the 'ComponentType' Enum")
        if other in self.components:
            self.components.remove(other)
            self.cost = self.cost - other.price
            return self
        else:
            return self

    def __eq__(self, other):
        if not isinstance(other, Circuit):
            raise TypeError("circuit2 is not valid circuit class type")
        return self.cost == other.cost
    def __gt__(self, other):
        if not isinstance(other, Circuit):
            raise TypeError("circuit2 is not valid circuit class type")
        return self.cost > other.cost
    def __lt__(self, other):
        if not isinstance(other, Circuit):
            raise TypeError("circuit2 is not valid circuit class type")
        return self.cost < other.cost
    def getByType(self, com):
        if not isinstance(com, ComponentType):
            raise TypeError("type is not ComponentType")
        res = set()
        for x in self.components:
            if x.ctype == com:
                res.add(x)
        return res
class Project:
    def __init__(self, ID, participants, circuits):
        self.ID = ID
        self.participants = participants
        self.circuits = circuits
        cost = 0
        for x in circuits:
            cost+= x.cost
        self.cost = cost
        for check1 in self.participants:
            if not isinstance(check1, Student):
                raise TypeError("The argument must be an instance of the 'Student'")
        for check2 in self.circuits:
            if not isinstance(check2, Circuit):
                raise TypeError("The argument must be an instance of the 'Circuit")

    def __str__(self):
        #ID: (XX Circuits, XX Participants), Cost = $<cost>
        num_c = len(self.circuits)
        if num_c < 10:
            num_c = '0' + str(num_c)
        num_s = len(self.participants)
        if num_s < 10:
            num_s = '0' + str(num_s)
        return f"{self.ID}: ({num_c} Circuits, {num_s} Participants), Cost = ${format(self.cost, '.2f')}"

    def __contains__(self, item):
        if not isinstance(item, Component):
            if not isinstance((item, Circuit)):
                if not isinstance(item, Student):
                    raise TypeError("This item your passed is not valid")
        if isinstance(item, Component):
            for x in self.circuits:
                if x.__contains__(item):
                    return True
            return False
        if isinstance(item, Circuit):
            return item.ID in [circuit.ID for circuit in self.circuits]

        if isinstance(item, Student):
            return item.ID in [student.ID for student in self.participants]

    def __add__(self, other):
        if not isinstance(other, Circuit):
            raise TypeError("The argument must be an instance of the 'Circuit'")
        if other in self.circuits:
            return self
        else:
            self.circuits.append(other)
            self.cost = self.cost + other.cost
            return self

    def __sub__(self, other):
        if not isinstance(other, Circuit):
            raise TypeError("The argument must be an instance of the 'Circuit'")
        if other in self.circuits:
            del self.circuits[other]
            self.cost = self.cost - other.cost
            return self
        else:
            return self

class Capstone(Project):
    def __init__(self, *args):
        if (len(args) == 1):
            super().__init__(args[0].ID, args[0].participants, args[0].circuits)
            check = [part.level for part in self.participants]
            for x in check:
                if x is not Level.Senior:
                    raise ValueError("all students must be senior")

        else:
            super().__init__(args[0].ID, args[0].participants, args[0].circuits)
            check = [part.level for part in self.participants]
            for x in check:
                if x is not Level.Senior:
                    raise ValueError("all students must be senior")