# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TYHOmain.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 350, 141, 71))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 180, 561, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 210, 561, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 240, 551, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 140, 391, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 470, 431, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 270, 581, 31))
        self.label_6.setObjectName("label_6")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(330, 40, 111, 81))
        self.heading.setObjectName("heading")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Analyze Me!"))
        self.label.setText(_translate("MainWindow", "Welcome to Tweet Your Heart Out. TYHO is a student developed language analysis tool, scripted entirely in python."))
        self.label_2.setText(_translate("MainWindow", "Clicking the button below will redirect you to a page where you will be prompted to validate your twitter credentials,"))
        self.label_3.setText(_translate("MainWindow", " TYHO will then pull the number of tweets you specify. Your tweets are filtered, categorized, and then analyzed by "))
        self.label_4.setText(_translate("MainWindow", "Have you ever wondered what your posts on social media say about your mood? "))
        self.label_5.setText(_translate("MainWindow", "Your personal information is never stored or shared, this tool is purely for self evaluation"))
        self.label_6.setText(_translate("MainWindow", "the tool, which will provide you a visualization of your personalized results, in your choice of a bar graph or a pie chart. "))
        self.heading.setText(_translate("MainWindow", "Tweet Your Heart Out"))

