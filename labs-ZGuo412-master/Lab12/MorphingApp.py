#######################################################
#   Author:     <Ziyu Guo>
#   email:      <guo412@purdue.edu>
#   ID:         <ee364d25>
#   Date:       <2019/4/20>
#######################################################
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QGraphicsScene
from Lab12.MorphingGUI import *
from PyQt5.QtGui import  QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import xml.etree.ElementTree as ET
import numpy as np
import imageio
import math
from Lab12 import Morphing

from scipy.spatial import Delaunay


class MorphingApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MorphingApp, self).__init__(parent)
        self.setupUi(self)
        self.LoadImg1.clicked.connect(self.loadDataleft)
        self.LoadImg2.clicked.connect(self.loadDataright)
        self.lineEdit.setText(str(self.Slider.value()/ 20))
        self.pushButton.setEnabled(False)
        self.Slider.setEnabled(False)
        self.checkBox.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.checkBox.stateChanged.connect(self.triangle)
        self.Slider.valueChanged.connect(self.Morph)
        self.pushButton.clicked.connect(self.morph_img)
        self.path1 = ''
        self.path2 = ''
        self.leftcount = 0
        self.rightcount = 0
        self.new_left = list()
        self.new_right = list()
        self.imagepathl = ''
        self.imagepathr = ''
        self.ratio = 0
        self.ratior = 0
        self.trick = False
        self.finish = False
        self.Img1.mousePressEvent = self.getLeft
        self.Img2.mousePressEvent = self.getRight
        self.keyPressEvent = self.deleteleft
        self.mode = False
        self.doub = False
        self.de = False
     #   self.Img1.mouseReleaseEvent(QGraphicsSceneMouseEvent)
    def deleteleft(self, event):
        if self.mode == False:
            return
        if event.key() == Qt.Key_Backspace:
            if self.leftcount > self.rightcount:
                self.new_left = self.new_left[:- 1]
                if len(self.new_left) == 0:
                    if os.path.exists(self.imagepathl + '.txt') == True:
                        data1 = np.loadtxt(self.imagepathl + '.txt', dtype=np.float64)
                        if np.size(data1, 0) >= 3:
                             self.triangle()
                    else:
                        pix = QPixmap(self.imagepathl)
                        img = QGraphicsScene()
                        img.addPixmap(pix)
                        self.Img1.setScene(img)
                        self.Img1.fitInView(img.sceneRect())

                else:
                    # pix = QPixmap(self.imagepathl)
                    # img = QGraphicsScene()
                    # painter = QPainter(pix)
                    # painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                    # scene = self.Img1.scene()
                    # width_r = scene.width() / self.Img1.width()
                    # height_r = scene.height() / self.Img1.height()
                    # for i in self.new_left:
                    #     x,y = i
                    #     painter.drawEllipse(x * width_r - 12, y * height_r - 12, 24, 24)
                    # painter.end()
                    # img.addPixmap(pix)
                    # self.Img1.setScene(img)
                    # self.Img1.fitInView(img.sceneRect())
                    if len(self.new_left) == 1:
                        # if os.path.exists(self.imagepathl + '.txt') == True:
                        #     data1 = np.loadtxt(self.imagepathl + '.txt', dtype=np.float64)
                        #     if np.size(data1, 0) >= 3:
                        #         self.triangle()
                        # else:
                            pix = QPixmap(self.imagepathl)
                            img = QGraphicsScene()
                            painter = QPainter(pix)
                            painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                            x,y = self.new_left[0]
                            painter.drawEllipse(x* self.ratio - 12,y* self.ratio - 12, 24, 24)
                            painter.end()
                            img.addPixmap(pix)
                            self.Img1.setScene(img)
                            self.Img1.fitInView(img.sceneRect())
                    else:
                        self.triangle()
                self.mode = False
                self.leftcount = self.leftcount - 1
                self.trick = True

            elif self.leftcount == self.rightcount:
                self.new_right = self.new_right[:-1]
                if len(self.new_right) == 0:
                    if os.path.exists(self.imagepathr + '.txt') == True:
                         data1 = np.loadtxt(self.imagepathr + '.txt', dtype=np.float64)
                         if np.size(data1, 0) >= 3:
                             self.triangle()
                    else:
                        pix = QPixmap(self.imagepathr)
                        img = QGraphicsScene()
                        img.addPixmap(pix)
                        self.Img2.setScene(img)
                        self.Img2.fitInView(img.sceneRect())

                else:
                    # pix = QPixmap(self.imagepathr)
                    # img = QGraphicsScene()
                    # painter = QPainter(pix)
                    # painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                    # scene = self.Img2.scene()
                    # width_r = scene.width() / self.Img2.width()
                    # height_r = scene.height() / self.Img2.height()
                    # for i in self.new_right:
                    #     x,y = i
                    #     painter.drawEllipse(x * width_r - 12, y * height_r - 12, 24, 24)
                    # painter.end()
                    # img.addPixmap(pix)
                    # self.Img2.setScene(img)
                    # self.Img2.fitInView(img.sceneRect())
                    if len(self.new_right) == 1:
                    #     if os.path.exists(self.imagepathr + '.txt') == True:
                    #         data1 = np.loadtxt(self.imagepathr + '.txt', dtype=np.float64)
                    #         if np.size(data1, 0) >= 3:
                    #             self.triangle()
                    #     else:
                            pix = QPixmap(self.imagepathr)
                            img = QGraphicsScene()
                            painter = QPainter(pix)
                            painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                            x,y = self.new_right[0]
                            painter.drawEllipse(x* self.ratio - 12,y* self.ratio - 12, 24, 24)
                            painter.end()
                            img.addPixmap(pix)
                            self.Img2.setScene(img)
                            self.Img2.fitInView(img.sceneRect())
                    else:
                        self.de = True
                        self.triangle()
                self.mode = False
                self.rightcount = self.rightcount - 1
                nnn = self.Img1.scene()
                x,y = self.new_left[len(self.new_left) - 1]
                nnn.addEllipse(x * self.ratio - 12, y * self.ratio - 12,24,24,brush=QBrush(Qt.green, Qt.SolidPattern))
                self.Img1.setScene(nnn)
                self.Img1.fitInView(nnn.sceneRect())
                nnn = self.Img2.scene()
                if len(self.new_right) != 0:
                    x,y = self.new_right[len(self.new_right) - 1]
                    nnn.addEllipse(x * self.ratior , y * self.ratior ,24,24,brush=QBrush(Qt.blue, Qt.SolidPattern))
                self.Img2.setScene(nnn)
                self.Img2.fitInView(nnn.sceneRect())
                self.doub =True
                self.de = False
    def loadDataleft(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open Image file ...', filter="Image files (*.jpg *.png)")

        if not filePath:
            return
        self.loadDataFromFile(filePath,1)
    def loadDataright(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open Image file ...', filter="Image files (*.jpg *.png)")

        if not filePath:
            return

        self.loadDataFromFile(filePath,2)
    def loadDataFromFile(self, filePath,num):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """


        ##points
        self.de = False
        self.doub = False
        self.trick = False
        self.finish = False
        self.path1 = ''
        self.path2 = ''
        self.leftcount = 0
        self.rightcount = 0
        self.new_left = list()
        self.new_right = list()
        txt_path = filePath + '.txt'
        if os.path.exists(txt_path) is True:
            data = np.loadtxt(txt_path, dtype=np.float64)
            x = data[:,1]
            y = data[:,0]

        ##
     #   hratio = width / 240
     #   wratio = height / 192
     #   pix = QPixmap(filePath).scaled(240,192, QtCore.Qt.KeepAspectRatio)
            pix = QPixmap(filePath)
            img1 = QGraphicsScene()
            painter = QPainter(pix)
            painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            for i in range(0, len(x)):
                painter.drawEllipse(y[i] - 12 , x[i] - 12, 24,24)
            painter.end()
            img1.addPixmap(pix)
            if num == 1:
                self.path1 = txt_path
            else:
                self.path2 = txt_path
        else:
            pix = QPixmap(filePath)
            img1 = QGraphicsScene()
           # pix_new = pix.scaled(self.Img1.width(),self.Img1.height(),Qt.KeepAspectRatio)
            img1.addPixmap(pix)
        if num == 1:
                self.imagepathl = filePath
                self.Img1.setScene(img1)
                self.Img1.fitInView(img1.sceneRect())
        else:
            self.imagepathr = filePath
            self.Img2.setScene(img1)
            self.Img2.fitInView(img1.sceneRect())
        if self.Img1.scene() and self.Img2.scene():
            self.pushButton.setEnabled(True)
            self.Slider.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.lineEdit.setEnabled(True)

    def triangle(self):
        if os.path.exists(self.imagepathl + '.txt') == False:
            return
        if self.checkBox.isChecked() is True:
            data1 = np.loadtxt(self.imagepathl + '.txt', dtype=np.float64)
            data2 = np.loadtxt(self.imagepathr + '.txt', dtype=np.float64)
            xl = data1[:, 1]
            yl = data1[:, 0]
            xr = data2[:, 1]
            yr = data2[:, 0]
            tril = Delaunay(data1)
            pointl = data1[tril.simplices]
            pointr = data2[tril.simplices]
            self.path1 = self.path1[0:len(self.path1) - 4]
            self.path2 = self.path2[0:len(self.path2) - 4]
            pix1 = QPixmap(self.imagepathl)
            pix2 = QPixmap(self.imagepathr)
            img1 = QGraphicsScene()
            img2 = QGraphicsScene()
            painter1 = QPainter(pix1)
            painter2 = QPainter(pix2)
            length = len(self.new_left)
            if self.finish == False:
                length = len(self.new_left) - 1
            elif len(self.new_left) > len(self.new_right):
                length = length - 1
            elif self.doub == False:
                length = length - 1
            if self.doub == True and len(self.new_left) == 1:
                length = 1
            if length == len(xl):
                painter1.setPen(QPen(Qt.blue,6.0, Qt.SolidLine))
                painter2.setPen(QPen(Qt.blue, 6.0, Qt.SolidLine))
            elif length <= 0:
                painter1.setPen(QPen(Qt.red,6.0, Qt.SolidLine))

                painter2.setPen(QPen(Qt.red,6.0, Qt.SolidLine))
            else:
                painter1.setPen(QPen(Qt.darkYellow, 6.0, Qt.SolidLine))

                painter2.setPen(QPen(Qt.darkYellow, 6.0, Qt.SolidLine))

            for i in range(0, len(pointl)):
                painter1.drawLine(pointl[i][0][0], pointl[i][0][1], pointl[i][1][0], pointl[i][1][1])
                painter1.drawLine(pointl[i][1][0], pointl[i][1][1], pointl[i][2][0], pointl[i][2][1])
                painter1.drawLine(pointl[i][2][0], pointl[i][2][1], pointl[i][0][0], pointl[i][0][1])
                painter2.drawLine(pointr[i][0][0], pointr[i][0][1], pointr[i][1][0], pointr[i][1][1])
                painter2.drawLine(pointr[i][1][0], pointr[i][1][1], pointr[i][2][0], pointr[i][2][1])
                painter2.drawLine(pointr[i][2][0], pointr[i][2][1], pointr[i][0][0], pointr[i][0][1])

            painter1.end()
            painter2.end()
            point1 = QPainter(pix1)
            point2 = QPainter(pix2)
            point1.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            point2.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            for i in range(0, len(xl)):
                point1.drawEllipse(yl[i] - 12, xl[i] - 12, 24, 24)
                point2.drawEllipse(yr[i] - 12, xr[i] - 12, 24, 24)
            if length > 0:
                point1.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                point2.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                #for i in range(len(xl) - length, len(xl)):
                    # point1.drawEllipse(yl[i] - 12, xl[i] - 12, 24, 24)
                    # point2.drawEllipse(yr[i] - 12, xr[i] - 12, 24, 24)
                leng = 0
                if len(self.new_left) > len(self.new_right):
                    leng = len(self.new_right)
                for j in range(0, len(self.new_left)):
                         x1, y1 = self.new_left[j]

                     #    painter1.drawEllipse(yl[i]-12 , xl[i] - 12 , 24, 24)
                      #   painter2.drawEllipse(yr[i] -12, xr[i] -12, 24, 24)
             # for i in range(0, len(self.new_left)):
                         if j == len(self.new_right):
                             point1.setBrush(QBrush(Qt.green, Qt.SolidPattern))
                         point1.drawEllipse(x1 * self.ratio - 12, y1 * self.ratio - 12, 24, 24)
                if self.doub == False:
                    x1,y1 = self.new_left[len(self.new_left) - 1]
                    point1.setBrush(QBrush(Qt.green, Qt.SolidPattern))
                    point1.drawEllipse(x1 * self.ratio - 12, y1 * self.ratio - 12, 24, 24)
                for n in self.new_right:
                    x2, y2 = n
                    point2.drawEllipse(x2 * self.ratior - 12, y2 * self.ratior - 12, 24, 24)
                if self.doub == False:
                    x2,y2 = self.new_right[len(self.new_right) - 1]
                    if self.de == False:
                        point2.setBrush(QBrush(Qt.green, Qt.SolidPattern))
                    point2.drawEllipse(x2 * self.ratior - 12, y2 * self.ratior - 12, 24, 24)
            point1.end()
            point2.end()
            img1.addPixmap(pix1)
            img2.addPixmap(pix2)
            self.Img1.setScene(img1)
            self.Img1.fitInView(img1.sceneRect())
            self.Img2.setScene(img2)
            self.Img2.fitInView(img2.sceneRect())
        else:
            pix1 = QPixmap(self.imagepathl)
            pix2 = QPixmap(self.imagepathr)
            img1 = QGraphicsScene()
            img2 = QGraphicsScene()
            self.path1 = self.path1 + '.txt'
            self.path2 = self.path2 + '.txt'
            data1 = np.loadtxt(self.imagepathl + '.txt', dtype=np.float64)
    #        data2 = np.loadtxt(self.imagepathr + '.txt', dtype=np.float64)
            data2 = np.loadtxt(self.imagepathr + '.txt', dtype=np.float64)
            xl = data1[:, 1]
            yl = data1[:, 0]
            xr = data2[:, 1]
            yr = data2[:, 0]
            point1 = QPainter(pix1)
            point2 = QPainter(pix2)
            point1.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            point2.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            length = len(self.new_left)
            if self.finish == False:
                length = len(self.new_left) - 1
            if self.doub == True and len(self.new_left) == 1:
                length = 1
            for i in range(0, len(xl)):
                point1.drawEllipse(yl[i] - 12, xl[i] - 12, 24, 24)
                point2.drawEllipse(yr[i] - 12, xr[i] - 12, 24, 24)
            if length > 0:
                point1.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                point2.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                # for i in range(len(xl) - length, len(xl)):
                #     point1.drawEllipse(yl[i] - 12, xl[i] - 12, 24, 24)
                #     point2.drawEllipse(yr[i] - 12, xr[i] - 12, 24, 24)
                leng = 0
                if len(self.new_left) > len(self.new_right):
                    leng = len(self.new_right)

                for j in range(0, len(self.new_left)):
                    x1, y1 = self.new_left[j]

                     #    painter1.drawEllipse(yl[i]-12 , xl[i] - 12 , 24, 24)
                      #   painter2.drawEllipse(yr[i] -12, xr[i] -12, 24, 24)
             # for i in range(0, len(self.new_left)):
                    if j == len(self.new_right):
                        point1.setBrush(QBrush(Qt.green, Qt.SolidPattern))
                    point1.drawEllipse(x1 * self.ratio - 12, y1 * self.ratio - 12, 24, 24)
                        # point2.drawEllipse(x2 * self.ratior - 12, y2 * self.ratior - 12, 24, 24)
                if self.doub == False:
                    x1,y1 = self.new_left[len(self.new_left) - 1]
                    point1.setBrush(QBrush(Qt.green, Qt.SolidPattern))
                    point1.drawEllipse(x1 * self.ratio - 12, y1 * self.ratio - 12, 24, 24)
                for m in self.new_right:
                    x2, y2 = m
                    point2.drawEllipse(x2 * self.ratior - 12, y2 * self.ratior - 12, 24, 24)
                if self.doub == False:
                    x2,y2 = self.new_right[len(self.new_right) - 1]
                    if self.de == False:
                        point2.setBrush(QBrush(Qt.green, Qt.SolidPattern))
                    #point2.setBrush(QBrush(Qt.green, Qt.SolidPattern))
                    point2.drawEllipse(x2 * self.ratior - 12, y2 * self.ratior - 12, 24, 24)
            point1.end()
            point2.end()
            img1.addPixmap(pix1)
            img2.addPixmap(pix2)
            self.Img1.setScene(img1)
            self.Img1.fitInView(img1.sceneRect())
            self.Img2.setScene(img2)
            self.Img2.fitInView(img2.sceneRect())
    def Morph(self):
        self.lineEdit.setText(str((self.Slider.value()) / 20))
    def morph_img(self):
        alpha = float(self.lineEdit.text())
        if '.txt' not in self.path1:
            self.path1 = self.path1 + '.txt'
        if '.txt' not in self.path2:
            self.path2 = self.path2 + '.txt'
        a, b = Morphing.loadTriangles(self.imagepathl + '.txt', self.imagepathr + '.txt')
        iml = imageio.imread(self.imagepathl)
        imr = imageio.imread(self.imagepathr)
        d = Morphing.Morpher(iml, a, imr, b)
        blendImg = d.getImageAtAlpha(alpha)
        blend_img = QtGui.QImage(blendImg,np.size(blendImg, 1), np.size(blendImg,0), QtGui.QImage.Format_Grayscale8)
        pix = QPixmap.fromImage(blend_img)
        img = QGraphicsScene()
        img.addPixmap(pix)
        self.Blend.setScene(img)
        self.Blend.fitInView(img.sceneRect())


    def getLeft(self,event):
        self.doub = True
        if self.leftcount > self.rightcount:
            return
        x = event.x()
        y = event.y()
        scene = self.Img1.scene()
        if scene == None:
            return
       # width_r = scene.width() / self.Img1.width()
       # height_r = scene.height() / self.Img1.height()

        if scene.width() / scene.height() > self.Img1.width() / self.Img1.height():
            self.ratio = scene.width() / self.Img1.width()
        else:
            self.ratio = scene.height() / self.Img1.height()
        scener = self.Img2.scene()
        if scener.width() / scener.height() > self.Img2.width() / self.Img2.height():
            self.ratior = scener.width() / self.Img2.width()
        else:
            self.ratior = scener.height() / self.Img2.height()
        scene.addEllipse(x * self.ratio -12  ,y * self.ratio -12 ,24,24,brush = QBrush(Qt.green,Qt.SolidPattern))
        # #scene.addEllipse(x-5, y-5, 10, 10, brush=QBrush(Qt.green, Qt.SolidPattern))
        # self.Img1.setScene(scene)
        # self.Img1.fitInView(scene.sceneRect())
        self.leftcount = self.leftcount + 1
        if len(self.new_left) > 0 :
            # pix1 = QPixmap(self.imagepathl)
            # pix2 = QPixmap(self.imagepathr)
            img1 = QGraphicsScene()
            img2 = QGraphicsScene()
            # painter1 = QPainter(pix1)
            # painter2 = QPainter(pix2)
            # painter1.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            # painter2.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            scene1 = self.Img1.scene()
            scene2 = self.Img2.scene()
            for i in range(0, len(self.new_left)):
                x1,y1 = self.new_left[i]
                x2,y2 = self.new_right[i]
                # painter1.drawEllipse(x1 * width_r1 - 12, y1 * height_r1 - 12, 24, 24)
                # painter2.drawEllipse(x2 * width_r2 - 12, y2 * height_r2 - 12, 24, 24)
                scene1.addEllipse(x1 * self.ratio - 12 , y1 * self.ratio - 12, 24, 24, brush=QBrush(Qt.blue, Qt.SolidPattern))
                scene2.addEllipse(x2 * self.ratior - 12, y2 * self.ratior - 12, 24, 24, brush=QBrush(Qt.blue, Qt.SolidPattern))
            if self.checkBox.isChecked() == False:
                # painter1.setBrush(QBrush(Qt.green, Qt.SolidPattern))
                # painter1.drawEllipse(x * width_r1 - 12, y * height_r1 - 12, 24, 24)
                # painter1.end()
                # painter2.end()
                # img1.addPixmap(pix1)
                # img2.addPixmap(pix2)
                #scene.addEllipse(x * width_r - 12, y * height_r - 12, 24, 24, brush=QBrush(Qt.green, Qt.SolidPattern))
                self.Img1.setScene(scene1)
                self.Img1.fitInView(scene1.sceneRect())
                self.Img2.setScene(scene2)
                self.Img2.fitInView(scene2.sceneRect())
            else:
                # painter1.end()
                # painter2.end()
                self.triangle()
                scene = self.Img1.scene()
                scene.addEllipse(x * self.ratio - 12, y * self.ratio - 12, 24, 24, brush=QBrush(Qt.green, Qt.SolidPattern))
                # scene.addEllipse(x-5, y-5, 10, 10, brush=QBrush(Qt.green, Qt.SolidPattern))
                self.Img1.setScene(scene)
                self.Img1.fitInView(scene.sceneRect())
  #      self.new_left.append((x, y))
        if self.trick == False:
            if self.new_right != list():
                with open(self.imagepathr + '.txt', 'a') as f:
                    xr,yr = self.new_right[len(self.new_right) - 1]
                    f.write('\n'+str(xr * self.ratior ) + ' ' + str(yr * self.ratior ))
            if self.leftcount > self.rightcount and len(self.new_left) >= 1:
                with open(self.imagepathl + '.txt', 'a') as f:
                    xl,yl = self.new_left[len(self.new_left) - 1]
                    f.write('\n'+str(xl * self.ratio) + ' ' + str(yl * self.ratio ))
     #   if len(self.new_left) >=3:
      #      self.triangle()
        if self.trick == True:
            self.trick = False
        if len(self.new_left) >= 3:
            self.triangle()
            hahaha = self.Img1.scene()
            hahaha.addEllipse(x* self.ratio - 12, y * self.ratio - 12,24,24,brush=QBrush(Qt.green, Qt.SolidPattern))
            self.Img1.setScene(hahaha)
            self.Img1.fitInView(hahaha.sceneRect())
        else:
            if os.path.exists(self.imagepathl + '.txt') == True:
                data1 = np.loadtxt(self.imagepathl + '.txt', dtype=np.float64)
                if np.size(data1, 0) >=3:
                    self.triangle()
                    hahaha = self.Img1.scene()
                    hahaha.addEllipse(x * self.ratio - 12, y * self.ratio - 12, 24, 24,
                                  brush=QBrush(Qt.green, Qt.SolidPattern))
                    self.Img1.setScene(hahaha)
                    self.Img1.fitInView(hahaha.sceneRect())
        self.new_left.append((x, y))
        self.mode = True
    def getRight(self,event):
        self.doub = False
        if self.rightcount == self.leftcount:
            return
        x = event.x()
        y = event.y()
        self.mode = True
        scene = self.Img2.scene()
        if scene == None:
            return
        scene.addEllipse(x * self.ratior - 12,y * self.ratior - 12,24,24,brush = QBrush(Qt.green,Qt.SolidPattern))
        #scene.addEllipse(x-5, y-5, 10, 10, brush=QBrush(Qt.green, Qt.SolidPattern))
        self.Img2.setScene(scene)
        self.Img2.fitInView(scene.sceneRect())
        self.rightcount = self.rightcount + 1
        self.new_right.append((x,y))

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        if self.leftcount == 0:
            return
        if self.leftcount != self.rightcount:
            return
        if self.mode == False:
            return
        # pix1 = QPixmap(self.imagepathl)
        # pix2 = QPixmap(self.imagepathr)
        # img1 = QGraphicsScene()
        # img2 = QGraphicsScene()
        # painter1 = QPainter(pix1)
        # painter2 = QPainter(pix2)
        # if os.path.exists(self.imagepathl + '.txt'):
        #     painter1.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        #     painter2.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        #     data1 = np.loadtxt(self.imagepathl + '.txt', dtype=np.float64)
        #     data2 = np.loadtxt(self.imagepathr + '.txt', dtype=np.float64)
        #     xl = data1[:, 1]
        #     yl = data1[:, 0]
        #     xr = data2[:, 1]
        #     yr = data2[:, 0]
        #     length = len(self.new_left)
        #     for i in range(0, len(xl)):
        #         painter1.drawEllipse(yl[i] - 12 , xl[i] - 12 , 24, 24)
        #         painter2.drawEllipse(yr[i] - 12, xr[i] - 12 , 24, 24)
        #     if length > 0:
        #         painter1.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        #         painter2.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        #         #for i in range(len(xl) - length, len(xl)):
        #         for j in range(0, len(self.new_left)):
        #             x1, y1 = self.new_left[j]
        #             x2, y2 = self.new_right[j]
        #         #    painter1.drawEllipse(yl[i]-12 , xl[i] - 12 , 24, 24)
        #          #   painter2.drawEllipse(yr[i] -12, xr[i] -12, 24, 24)
        # # for i in range(0, len(self.new_left)):
        #
        #             painter1.drawEllipse(x1 * self.ratio - 12, y1 * self.ratio - 12, 24, 24)
        #             painter2.drawEllipse(x2 * self.ratior - 12, y2 * self.ratior - 12, 24, 24)
        # #painter1.setBrush(QBrush(Qt.green, Qt.SolidPattern))
        #     #painter1.end()
        #     #painter2.end()
        # else:
        #     painter1.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        #     painter2.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        #     xl, yl = self.new_left[len(self.new_left) - 1]
        #     xr, yr = self.new_right[len(self.new_right) - 1]
        #     painter1.drawEllipse(xl * self.ratio - 12, yl * self.ratio - 12, 24, 24)
        #     painter2.drawEllipse(xr * self.ratior - 12, yr * self.ratior - 12, 24, 24)
        # painter1.end()
        # painter2.end()
        # img1.addPixmap(pix1)
        # img2.addPixmap(pix2)
        # self.Img1.setScene(img1)
        # self.Img1.fitInView(img1.sceneRect())
        # self.Img2.setScene(img2)
        # self.Img2.fitInView(img2.sceneRect())
        self.doub =True
        xl, yl = self.new_left[len(self.new_left) - 1]
        xr, yr = self.new_right[len(self.new_right) - 1]
        scene1 = self.Img1.scene()
        scene2 = self.Img2.scene()
        scene1.addEllipse(xl * self.ratior - 12, yl * self.ratior - 12, 24, 24, brush=QBrush(Qt.blue, Qt.SolidPattern))
        # scene.addEllipse(x-5, y-5, 10, 10, brush=QBrush(Qt.green, Qt.SolidPattern))
        scene2.addEllipse(xr * self.ratior - 12, yr * self.ratior - 12, 24, 24, brush=QBrush(Qt.blue, Qt.SolidPattern))
        self.Img2.setScene(scene2)
        self.Img2.fitInView(scene2.sceneRect())
        self.Img1.setScene(scene1)
        self.Img1.fitInView(scene1.sceneRect())
        with open(self.imagepathr + '.txt', 'a') as f:
            xr, yr = self.new_right[len(self.new_right) - 1]
            f.write('\n'+str(xr * self.ratior) + ' ' + str(yr * self.ratior))
        with open(self.imagepathl + '.txt', 'a') as f:
            xl, yl = self.new_left[len(self.new_left) - 1]
            f.write('\n'+str(xl * self.ratio) + ' ' + str(yl * self.ratio ))
        if len(self.new_left) >= 3:
            self.triangle()
        self.mode = False
        self.finish = True
        self.trick = True
# class graphics(QGraphicsScene):
#     def __init__(self, parent = None):
#         super(graphics, self).__init__(parent)
#     def mouseReleaseEvent(self, QGraphicsSceneMouseEvent):
#         mouse = QGraphicsSceneMouseEvent
#         print(mouse.x(), mouse.y())
#         print(mouse.pos())
#         cursor = QtGui.QCursor
#         print(cursor.pos())
if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MorphingApp()
    currentForm.show()
    currentApp.exec_()
