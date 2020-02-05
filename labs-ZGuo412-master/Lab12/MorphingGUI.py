# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MorphingGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 717)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LoadImg1 = QtWidgets.QPushButton(self.centralwidget)
        self.LoadImg1.setGeometry(QtCore.QRect(30, 10, 161, 27))
        self.LoadImg1.setObjectName("LoadImg1")
        self.LoadImg2 = QtWidgets.QPushButton(self.centralwidget)
        self.LoadImg2.setGeometry(QtCore.QRect(390, 10, 151, 27))
        self.LoadImg2.setObjectName("LoadImg2")
        self.Img1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.Img1.setGeometry(QtCore.QRect(30, 60, 251, 192))
        self.Img1.setMouseTracking(True)
        self.Img1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Img1.setObjectName("Img1")
        self.Img2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.Img2.setGeometry(QtCore.QRect(390, 60, 256, 192))
        self.Img2.setMouseTracking(True)
        self.Img2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Img2.setAcceptDrops(False)
        self.Img2.setObjectName("Img2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 270, 101, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(441, 270, 91, 20))
        self.label_2.setObjectName("label_2")
        self.Slider = QtWidgets.QSlider(self.centralwidget)
        self.Slider.setGeometry(QtCore.QRect(120, 320, 401, 31))
        self.Slider.setAutoFillBackground(False)
        self.Slider.setMaximum(20)
        self.Slider.setSingleStep(1)
        self.Slider.setPageStep(10)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setTickInterval(0)
        self.Slider.setObjectName("Slider")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 330, 62, 17))
        self.label_3.setObjectName("label_3")
        self.Blend = QtWidgets.QGraphicsView(self.centralwidget)
        self.Blend.setGeometry(QtCore.QRect(210, 390, 256, 192))
        self.Blend.setObjectName("Blend")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 600, 131, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 630, 92, 27))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(280, 280, 93, 22))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 320, 51, 27))
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 350, 62, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 350, 62, 17))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoadImg1.setText(_translate("MainWindow", "Load Starting Image ..."))
        self.LoadImg2.setText(_translate("MainWindow", "Load Ending Image ..."))
        self.label.setText(_translate("MainWindow", "Staring Image"))
        self.label_2.setText(_translate("MainWindow", "Ending Image"))
        self.label_3.setText(_translate("MainWindow", "Alpha"))
        self.label_4.setText(_translate("MainWindow", "Blending Result"))
        self.pushButton.setText(_translate("MainWindow", "Blend"))
        self.checkBox.setText(_translate("MainWindow", "Triangle"))
        self.label_5.setText(_translate("MainWindow", "0.0"))
        self.label_6.setText(_translate("MainWindow", "1.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

