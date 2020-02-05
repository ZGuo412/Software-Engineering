#######################################################
#   Author:     <Ziyu Guo>
#   email:      <guo412@purdue.edu>
#   ID:         <ee364d25>
#   Date:       <2019/3/31>
#######################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from Prelab11.BasicUI import *
import xml.etree.ElementTree as ET

DataPath = '~ee364/DataFolder/Prelab11'
class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.btnSave.setEnabled(False)
        self.txtCom = ['']*20
        self.txtcname = [''] * 20

        for i in range(0,20):
            self.txtCom[i] = 'self.txtComponentCount_' + str(i + 1)
            self.txtcname[i] = 'self.txtComponentName_' + str(i + 1)


        self.txtStudentName.textChanged.connect(self.entry)
        self.txtStudentID.textChanged.connect(self.entry)
        self.com_txt = [self.txtComponentCount_1,self.txtComponentCount_2,self.txtComponentCount_3,self.txtComponentCount_4,self.txtComponentCount_5,self.txtComponentCount_6,self.txtComponentCount_7,self.txtComponentCount_8,self.txtComponentCount_9,self.txtComponentCount_10
               ,self.txtComponentCount_11,self.txtComponentCount_12,self.txtComponentCount_13,self.txtComponentCount_14,self.txtComponentCount_15,self.txtComponentCount_16,self.txtComponentCount_17,self.txtComponentCount_18,self.txtComponentCount_19,self.txtComponentCount_20]
        self.name_txt = [self.txtComponentName_1,self.txtComponentName_2,self.txtComponentName_3,self.txtComponentName_4,self.txtComponentName_5,self.txtComponentName_6,self.txtComponentName_7,self.txtComponentName_8,self.txtComponentName_9,self.txtComponentName_10,
                self.txtComponentName_11,self.txtComponentName_12,self.txtComponentName_13,self.txtComponentName_14,self.txtComponentName_15,self.txtComponentName_16,self.txtComponentName_17,self.txtComponentName_18,self.txtComponentName_19,self.txtComponentName_20]
        for count in self.txtCom:
            count = count + '.textChanged.connect(self.entry)'
            exec(count)

        for count in self.txtcname:
            count = count + '.textChanged.connect(self.entry)'
            exec(count)

        self.cboCollege.currentIndexChanged.connect(self.entry)
        self.chkGraduate.stateChanged.connect(self.entry)

        self.btnClear.clicked.connect(self.click_clear)
        self.btnLoad.clicked.connect(self.loadData)
        self.btnSave.clicked.connect(self.saveXML)

    def loadData(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        tree = ET.parse(filePath)
        root = tree.getroot()
        for child in root:
            # print(child.tag)   (StudentName), StudentID, College, Components
            #print(child.attrib)   ({'graduate': 'true'})
            if child.tag == 'StudentName':
                self.txtStudentName.setText(child.text)
                if child.attrib['graduate'] ==  "true":
                    self.chkGraduate.setChecked(True)
            if child.tag == 'StudentID':
                self.txtStudentID.setText(child.text)
            if child.tag == 'College':
                self.cboCollege.setCurrentIndex(self.cboCollege.findText(child.text))

            if child.tag == 'Components':
                child_name = list()
                child_count = list()
                for component in child:
                    ans = list(component.attrib.values())
                    child_name.append(ans[0])
                    child_count.append(ans[1])
                for i in range(0,len(child_name)):
                    if i >= 20:
                        break
                    self.name_txt[i].setText(child_name[i])
                    self.com_txt[i].setText(child_count[i])

    def click_clear(self):
        self.txtStudentID.clear()
        self.txtStudentName.clear()
        for count in self.txtCom:
            count = count + '.clear()'
            exec(count)

        for count in self.txtcname:
            count = count + '.clear()'
            exec(count)
        self.cboCollege.setCurrentIndex(0)
        self.chkGraduate.setChecked(False)
        self.btnLoad.setEnabled(True)
        self.btnClear.setEnabled(True)
        self.btnSave.setEnabled(False)
    def entry(self):
        if self.txtStudentName.text is not '':
            self.butt()
        if self.txtStudentID.text is not '':
            self.butt()
        for count in self.txtCom:
            count = count + '.text'
            exec(count)
            if exec(count) is not '':
                self.butt()
        for count in self.txtcname:
            count = count + '.text'
            exec(count)
            if exec(count) is not '':
                self.butt()
        if self.chkGraduate.checkState is True:
            self.butt()
        if self.cboCollege.currentIndex is not '':
            self.butt()
    def butt(self):
        self.btnLoad.setEnabled(False)
        self.btnSave.setEnabled(True)
    def saveXML(self):
        graduate = 'false'
        if self.chkGraduate.isChecked() is True:
            graduate = 'true'
        s_name = self.txtStudentName.text()
        s_id = self.txtStudentID.text()
        college = self.cboCollege.currentText()
        Cname = list()
        Ccount = list()
        for name in self.name_txt:
            if name.text() is not '':
                Cname.append(name.text())
        for count in self.com_txt:
            if count.text() is not '':
                Ccount.append(count.text())
        with open('target.xml', 'w') as output:
            output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            output.write('<Content>\n')
            output.write('    <StudentName graduate="'+graduate+'">'+s_name+'</StudentName>\n')
            output.write('    <StudentID>'+s_id+'</StudentID>\n')
            output.write('    <College>'+college+'</College>\n')
            output.write('    <Components>\n')
            for i in range(0, len(Ccount)):
                output.write('        <Component name="'+Cname[i]+'" count="'+Ccount[i]+'" />\n')
            output.write('    </Components>\n</Content>')



if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()

