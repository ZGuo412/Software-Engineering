import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import re
from Lab11.calculator import *

class MathConsumer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)
        self.btnCalculate.clicked.connect(self.performOperation)

    def performOperation(self):
        checknum1 = re.findall(r"([^0-9]+)", self.edtNumber1.text())
        checknum2 = re.findall(r"([^0-9]+)", self.edtNumber2.text())
        if self.edtNumber1.text() == '':
            self.edtResult.setText('E')
        elif self.edtNumber2.text() == '':
            self.edtResult.setText('E')
        elif checknum1 != []:
            if checknum1[0] != '.':
                self.edtResult.setText('E')
            else:
                if len(checknum1) == 1:
                    self.cal()
                else:
                    self.edtResult.setText('E')
        elif checknum2 != []:
            if checknum2[0] != '.':
                self.edtResult.setText('E')
            else:
                if len(checknum2) == 1:
                    self.cal()
                else:
                    self.edtResult.setText('E')

        else:
            self.cal()
    def cal(self):
        if self.cboOperation.currentText() == '+':
            num1 = self.edtNumber1.text()
            num2 = self.edtNumber2.text()
            res = float(num1) + float(num2)
            self.edtResult.setText(str(round(res,12)))
        elif self.cboOperation.currentText() == '-':
            num1 = self.edtNumber1.text()
            num2 = self.edtNumber2.text()
            res = float(num1) - float(num2)
            self.edtResult.setText(str(round(res,12)))
        elif self.cboOperation.currentText() == '*':
            num1 = self.edtNumber1.text()
            num2 = self.edtNumber2.text()
            res = float(num1) * float(num2)
            self.edtResult.setText(str(round(res,12)))
        elif self.cboOperation.currentText() == '/':
            num1 = self.edtNumber1.text()
            num2 = self.edtNumber2.text()
            if float(num2) == 0.0:
                self.edtResult.setText('E')
            else:
                res = float(num1) / float(num2)
                self.edtResult.setText(str(round(res,12)))
if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MathConsumer()
    currentForm.show()
    currentApp.exec_()