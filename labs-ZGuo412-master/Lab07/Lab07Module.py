import os
from uuid import UUID
from pprint import pprint as pp
from enum import Enum
import sys     # Each  one on a line
import csv
import copy
import re

class Rectangle:
    def __init__(self, llPoint, urPoint):
        self.lowerLeft = llPoint
        self.upperRight = urPoint
        checkx1,checky1 = llPoint
        checkx2,checky2 = urPoint
        if not(checkx1 < checkx2 and checky1 < checky2):
            raise ValueError("the point is not valid")

    def isSquare(self):
        checkx1,checky1 = self.lowerLeft
        checkx2,checky2 = self.upperRight
        if (checkx2 - checkx1 == checky2 - checky1):
            return True
        else:
            return False

    def intersectsWith(self, rect):
        checkx1,checky1 = self.lowerLeft
        checkx2,checky2 = self.upperRight
        rectx1, recty1 = rect.lowerLeft
        rectx2, recty2 = rect.upperRight
        if checkx1 < rectx1 < checkx2:
            if checky1 < recty2 < checky2:
                return True
            elif checky1 < recty1 < checky2:
                return True
        elif checkx1 < rectx2 < checkx2:
            if checky2 < recty2 < checky2:
                return True
            elif checky1 < recty1 < checky2:
                return True
        return False

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("This input is not a valid Rectangle instance")
        x1,y1 = self.lowerLeft
        x2,y2 = self.upperRight
        checkx1,checky1 = other.lowerLeft
        checkx2,checky2 = other.upperRight
        A1 = (x2 - x1) * (y2 - y1)
        A2 = (checkx2 - checkx1) * (checky2 - checky1)
        return A1 == A2


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        if radius <= 0:
            raise ValueError("radius should be greater than 0")

    def intersectsWith(self, other):
        if isinstance(other, Circle):
            x1, y1 = other.center
            x2, y2 = self.center
            disy = (y2 - y1)
            disx = x2 - x1
            cdis = other.radius + self.radius
            if disx**2 + disy**2 < cdis**2:
                return True
            return False
        if isinstance(other, Rectangle):
            point1x, point1y = other.lowerLeft
            point2x, point2y = other.upperRight
            point3x, point3y = point1x, point2y
            point4x, point4y = point2x, point1y
            x1, y1 = self.center
            ra = self.radius ** 2
            dis1 = (x1 - point1x)**2 + (y1 - point1y)**2
            dis2 = (x1 - point2x) ** 2 + (y1 - point2y) ** 2
            dis3 = (x1 - point3x) ** 2 + (y1 - point3y) ** 2
            dis4 = (x1 - point4x) ** 2 + (y1 - point4y) ** 2
            if dis1 < ra:
                return True
            elif dis2 < ra:
                return True
            elif dis3 < ra:
                return True
            elif dis4 < ra:
                return True
            else:
                return False