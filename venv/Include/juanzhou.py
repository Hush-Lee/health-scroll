# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'juanzhou.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 576)
        MainWindow.setMaximumSize(QtCore.QSize(1024, 576))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(227, 490, 500, 40))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(" \n"
"font: 14pt \"华文细黑\";\n"
"gridline-color: rgb(255, 255, 127);\n"
" ")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.detail = QtWidgets.QPushButton(self.centralwidget)
        self.detail.setGeometry(QtCore.QRect(797, 490, 70, 40))
        self.detail.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.detail.setStyleSheet("background-color: rgb(255, 170, 0);\n"
                                      "font: 75 14pt \"Comic Sans MS\";\n"
                                      " \n"
                                      "color: rgb(255, 255, 255);\n"
                                      " ")
        self.detail.setObjectName("pushButton")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(727, 490, 70, 40))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 75 14pt \"Comic Sans MS\";\n"
" \n"
"color: rgb(255, 255, 255);\n"
" ")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 576))
        self.label.setStyleSheet("background-image: url(res/juanzhou_bg.png);\n"
" ")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 110, 701, 321))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "健康卷轴"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.detail.setText(_translate("MainWindow", "详情"))
        self.menu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))


