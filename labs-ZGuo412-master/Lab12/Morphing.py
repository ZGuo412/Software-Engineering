import sys
import numpy as np
import scipy
import imageio
from scipy.spatial import Delaunay
from PIL import ImageDraw, Image
from matplotlib.path import Path
import math
from scipy import interpolate
import os
import matplotlib.pyplot as plt
def loadTriangles(leftPointFilePath, rightPointFilePath):
    lpath = leftPointFilePath
    rpath = rightPointFilePath
    data1 = np.loadtxt(lpath,dtype=np.float64)
    data2 = np.loadtxt(rpath,dtype=np.float64)
    tril = Delaunay(data1)
    pointl = data1[tril.simplices]
    pointr = data2[tril.simplices]
    leftri = list()
    rightri = list()

    for x in range(0, len(pointl)):
        leftri.append(Triangle(pointl[x]))
        rightri.append(Triangle(pointr[x]))
    return(leftri, rightri)


class Triangle:
    def __init__(self, np_array):
        if not isinstance(np_array, np.ndarray):
            raise ValueError("input should be a ndarray")
        if np_array.dtype != np.float64 or len(np_array) != 3:
            raise ValueError("input should be a 3 x 2 numpy array of type float64")
        self.vertices = np_array

    def getPoints(self):
        max_x = max(self.vertices[:,0])
        min_x = min(self.vertices[:,0])
        max_y = max(self.vertices[:,1])
        min_y = min(self.vertices[:,1])
        wid = math.ceil(max_x - min_x)
        len = math.ceil(max_y - min_y)
        im = Image.new('L', (math.floor(max_x),math.ceil(max_y)),0)
        ImageDraw.Draw(im).polygon(tuple(map(tuple,self.vertices)),fill=255,outline=255)
        temp = np.nonzero(im)
        ans = np.transpose(temp)
        ans[:,[0,1]] = ans[:,[1,0]]
        return ans.astype(np.float64)
class Morpher:
    def __init__(self,leftm,leftt,rightm,rightt):
        if leftm.dtype != np.uint8:
            raise TypeError("input type should be unint8")
        if rightm.dtype != np.uint8:
            raise TypeError("input type should be unint8")
        for x in leftt:
            if not isinstance(x, Triangle):
                raise TypeError("input should be the instance of triangle")
        for y in rightt:
            if not isinstance(y,Triangle):
                raise TypeError("input should be the instance of triangle")
        self.leftImage = leftm
        self.leftTriangles = leftt
        self.rightImage = rightm
        self.rightTriangles = rightt

    def getImageAtAlpha(self,alpha):
        midtri = list()
        midmat = list()
        leftmat = list()
        rightmat = list()
        fin_gray = np.zeros((self.leftImage.shape[0] , self.leftImage.shape[1]),np.uint8)
        fin_left = interpolate.RectBivariateSpline(range(self.leftImage.shape[0]), range(self.leftImage.shape[1]),
                                                   self.leftImage)
        fin_right = interpolate.RectBivariateSpline(range(self.rightImage.shape[0]), range(self.rightImage.shape[1]),
                                                    self.rightImage)
        for x in range(0, len(self.rightTriangles)):

            ltemp = self.leftTriangles[x]
            rtemp = self.rightTriangles[x]
            midx = [0]*3
            midy = [0]*3
            midy[0] = ltemp.vertices[0][0] * (1-alpha) + alpha * rtemp.vertices[0][0]
            midx[0] = ltemp.vertices[0][1] * (1-alpha) + alpha * rtemp.vertices[0][1]
            midy[1] = ltemp.vertices[1][0] * (1-alpha) + alpha * rtemp.vertices[1][0]
            midx[1] = ltemp.vertices[1][1] * (1-alpha) + alpha * rtemp.vertices[1][1]
            midy[2] = ltemp.vertices[2][0] * (1-alpha) + alpha * rtemp.vertices[2][0]
            midx[2] = ltemp.vertices[2][1] * (1-alpha) + alpha * rtemp.vertices[2][1]
            ##get each mid triangle above
            midmat = np.array(([midx[0],midy[0],1,0,0,0],[0,0,0,midx[0],midy[0],1],
                                   [midx[1], midy[1], 1, 0, 0, 0], [0, 0, 0, midx[1], midy[1], 1],
                                   [midx[2], midy[2], 1, 0, 0, 0], [0, 0, 0, midx[2], midy[2], 1]))
            ##get mid triangle 6x6 matrix
            leftmat = np.array(([ltemp.vertices[0][1]],[ltemp.vertices[0][0]],[ltemp.vertices[1][1]],[ltemp.vertices[1][0]],[ltemp.vertices[2][1]],[ltemp.vertices[2][0]]))
            rightmat = np.array(([rtemp.vertices[0][1]], [rtemp.vertices[0][0]], [rtemp.vertices[1][1]],
                                      [rtemp.vertices[1][0]], [rtemp.vertices[2][1]], [rtemp.vertices[2][0]]))
            ##get left triangle 6x1 matrix
            left_temp_tran = np.linalg.solve(midmat,leftmat)
            right_temp_tran = np.linalg.solve(midmat,rightmat)
            left_temp_tran = np.append(left_temp_tran, np.array([0,0,1]))
            left_temp_tran = np.reshape(left_temp_tran,(3,3))
            right_temp_tran = np.append(right_temp_tran, np.array([0,0,1]))
            right_temp_tran = np.reshape(right_temp_tran,(3,3))
            mid_tri = Triangle(np.column_stack((midx,midy)))
            mid_points = mid_tri.getPoints()
            new_leftx = np.array([])
            new_rightx = np.array([])
            new_lefty = np.array([])
            new_righty = np.array([])
            for x in mid_points:
                x = np.append(x,1)
                x = np.reshape(x,(3,1))
                new_leftx = np.append(new_leftx,np.dot(left_temp_tran,x)[0])
                new_rightx = np.append(new_rightx,np.dot(right_temp_tran,x)[0])
                new_lefty = np.append(new_lefty, np.dot(left_temp_tran, x)[1])
                new_righty = np.append(new_righty,np.dot(right_temp_tran,x)[1])


            gray_left = fin_left.ev(new_leftx,new_lefty)
            gray_right = fin_right.ev(new_rightx,new_righty)
            x = mid_points[:,0].astype(np.uint64)
            y = mid_points[:,1].astype(np.uint64)
            fin_gray[x,y] = gray_left * (1 - alpha) + gray_right * alpha

        return fin_gray

if __name__ == "__main__":

    DataPath1 = os.path.expanduser('~ee364/DataFolder/Lab12/TestData/points.left.txt')
    DataPath2 = os.path.expanduser('~ee364/DataFolder/Lab12/TestData/points.right.txt')
    a,b = loadTriangles(DataPath1,DataPath2)
    iml = imageio.imread('~ee364/DataFolder/Lab12/TestData/LeftGray.png')
    imr = imageio.imread('~ee364/DataFolder/Lab12/TestData/RightGray.png')
    d = Morpher(iml,a,imr,b)


