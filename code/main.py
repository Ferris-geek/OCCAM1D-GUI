# -*- coding: utf-8 -*-

"""
    CREATED BY FYMAO,
    email: fymao@zju.edu.cn
    Any question please contact me!
    2022.6.1, Zhejiang University.
    """

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from OCCAM1D import Ui_OCCAM1D
from OCCAM1DMTpy import Ui_OCCAM1DMTpy
import os


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(389, 404)
        self.labelwelcome = QtWidgets.QLabel(self)
        self.labelwelcome.setGeometry(QtCore.QRect(90, 10, 201, 141))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.labelwelcome.setFont(font)
        self.labelwelcome.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelwelcome.setTextFormat(QtCore.Qt.AutoText)
        self.labelwelcome.setScaledContents(False)
        self.labelwelcome.setAlignment(QtCore.Qt.AlignCenter)
        self.labelwelcome.setWordWrap(False)
        self.labelwelcome.setOpenExternalLinks(False)
        self.labelwelcome.setObjectName("labelwelcome")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(110, 320, 181, 51))
        self.label.setObjectName("label")
        self.Buttonoccam = QtWidgets.QPushButton(self)
        self.Buttonoccam.setGeometry(QtCore.QRect(80, 160, 231, 31))
        self.Buttonoccam.setObjectName("Buttonoccam")
        self.ButtonMtpy = QtWidgets.QPushButton(self)
        self.ButtonMtpy.setGeometry(QtCore.QRect(80, 210, 231, 31))
        self.ButtonMtpy.setObjectName("ButtonMtpy")
        self.Buttonreadme = QtWidgets.QPushButton(self)
        self.Buttonreadme.setGeometry(QtCore.QRect(80, 260, 231, 31))
        self.Buttonreadme.setObjectName("Buttonreadme")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        os.chdir(os.path.split(os.path.abspath(sys.argv[0]))[0])
        """Button
        """
        self.Buttonoccam.clicked.connect(self.occaminv)
        self.Buttonreadme.clicked.connect(self.readme)
        self.ButtonMtpy.clicked.connect(self.occamMtpy)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelwelcome.setText(_translate("MainWindow", "MT Series"))
        self.label.setText(_translate("MainWindow", "Copyright@MaoFangyuan"))
        self.Buttonoccam.setText(_translate("MainWindow", "Occam1D Inversion"))
        self.ButtonMtpy.setText(_translate("MainWindow", "MTpy"))
        self.Buttonreadme.setText(_translate("MainWindow", "Introduction"))
        
    def occaminv(self):
        self.uioccam1d = Ui_OCCAM1D()
        self.uioccam1d.show()
    
    def occamMtpy(self):
        self.uioccam1dmtpy = Ui_OCCAM1DMTpy()
        self.uioccam1dmtpy.show()
    
    def readme(self):
        introduction = "\
            请阅读文件夹中的readme !\n\
            有问题请联系 fymao@zju.edu.cn\n\
            :)\
        "
        QMessageBox.information(
            self, "提醒", introduction, 
            QMessageBox.Yes, QMessageBox.Yes
            )



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    uimainwindow = Ui_MainWindow()
    uimainwindow.show()
    sys.exit(app.exec_())