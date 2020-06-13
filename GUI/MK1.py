# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MK1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from random import randint

from enum import Enum

import pygame
import time
import serial
import math
import sys

import threading

# define number
listrange = 63
Y_min = -110
Y_max = 110
Y1_min = 110
Y1_max = -110
ippppp = 0

class mode(Enum):
    auto = 1
    manual = 2
    debug = 3
    stop = 0

joystick_no = []
joystick_choice = 0
choiceJoystickstatus = False
Joystickconect = False
NameCOM = []
button=[0,0,0,0,0]
axis=[0,0,0]
datasendalpha=[]
transmit=[]
comconnect = False
control = mode.stop
lastcontrol = mode.stop
globaldebug=[0,0]

class ComboBox(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBox, self).showPopup()

class Ui_MK1(object):
    def setupUi(self, MK1):
        MK1.setObjectName("MK1")
        MK1.setEnabled(True)
        MK1.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MK1.sizePolicy().hasHeightForWidth())
        MK1.setSizePolicy(sizePolicy)
        MK1.setMinimumSize(QtCore.QSize(1280, 720))
        MK1.setMaximumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/ASUS/Pictures/82362862_762415024581207_8972626692153540608_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MK1.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MK1)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 211, 111))
        self.groupBox.setObjectName("groupBox")
        self.COM = QtWidgets.QComboBox(self.groupBox)
        self.COM.setGeometry(QtCore.QRect(40, 20, 151, 22))
        self.COM.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.COM.setObjectName("COM")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.COM.addItem("")
        self.connect = QtWidgets.QPushButton(self.groupBox)
        self.connect.setGeometry(QtCore.QRect(20, 60, 171, 41))
        self.connect.setObjectName("connect")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 10, 431, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 47, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 47, 16))
        self.label_3.setObjectName("label_3")
        self.ID_device = QtWidgets.QLabel(self.groupBox_2)
        self.ID_device.setGeometry(QtCore.QRect(60, 40, 361, 16))
        self.ID_device.setText("")
        self.ID_device.setObjectName("ID_device")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 47, 16))
        self.label_4.setObjectName("label_4")
        self.SS_device = QtWidgets.QLabel(self.groupBox_2)
        self.SS_device.setGeometry(QtCore.QRect(60, 60, 361, 16))
        self.SS_device.setText("")
        self.SS_device.setObjectName("SS_device")
        self.device = ComboBox(self.groupBox_2)
        self.device.setGeometry(QtCore.QRect(60, 20, 361, 22))
        self.device.setObjectName("device")
        self.choice_mode = QtWidgets.QGroupBox(self.centralwidget)
        self.choice_mode.setGeometry(QtCore.QRect(10, 130, 211, 221))
        self.choice_mode.setObjectName("choice_mode")
        self.auto_2 = QtWidgets.QPushButton(self.choice_mode)
        self.auto_2.setGeometry(QtCore.QRect(20, 20, 171, 41))
        self.auto_2.setObjectName("auto_2")
        self.manual = QtWidgets.QPushButton(self.choice_mode)
        self.manual.setGeometry(QtCore.QRect(20, 70, 171, 41))
        self.manual.setObjectName("manual")
        self.stop = QtWidgets.QPushButton(self.choice_mode)
        self.stop.setGeometry(QtCore.QRect(20, 120, 171, 41))
        self.stop.setObjectName("stop")
        self.debug = QtWidgets.QPushButton(self.choice_mode)
        self.debug.setGeometry(QtCore.QRect(20, 170, 171, 41))
        self.debug.setObjectName("debug")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 360, 341, 331))
        self.groupBox_4.setObjectName("groupBox_4")
        self.re_se_data = QtWidgets.QTextBrowser(self.groupBox_4)
        self.re_se_data.setEnabled(True)
        self.re_se_data.setGeometry(QtCore.QRect(10, 20, 321, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.re_se_data.sizePolicy().hasHeightForWidth())
        self.re_se_data.setSizePolicy(sizePolicy)
        self.re_se_data.setObjectName("re_se_data")
        self.testsend = QtWidgets.QTextEdit(self.groupBox_4)
        self.testsend.setGeometry(QtCore.QRect(10, 290, 231, 31))
        self.testsend.setObjectName("testsend")
        self.send = QtWidgets.QPushButton(self.groupBox_4)
        self.send.setGeometry(QtCore.QRect(250, 290, 75, 31))
        self.send.setObjectName("send")
        self.gr_axis = QtWidgets.QGroupBox(self.centralwidget)
        self.gr_axis.setGeometry(QtCore.QRect(670, 10, 601, 681))
        self.gr_axis.setObjectName("gr_axis")
        self.xaxis = PlotWidget(self.gr_axis)
        self.xaxis.setGeometry(QtCore.QRect(10, 20, 281, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xaxis.sizePolicy().hasHeightForWidth())
        self.xaxis.setSizePolicy(sizePolicy)
        self.xaxis.setObjectName("xaxis")
        self.yaxis = PlotWidget(self.gr_axis)
        self.yaxis.setGeometry(QtCore.QRect(310, 20, 281, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yaxis.sizePolicy().hasHeightForWidth())
        self.yaxis.setSizePolicy(sizePolicy)
        self.yaxis.setObjectName("yaxis")
        self.xaxis_1 = PlotWidget(self.gr_axis)
        self.xaxis_1.setGeometry(QtCore.QRect(310, 250, 281, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xaxis_1.sizePolicy().hasHeightForWidth())
        self.xaxis_1.setSizePolicy(sizePolicy)
        self.xaxis_1.setObjectName("xaxis_1")
        self.yaxis_1 = PlotWidget(self.gr_axis)
        self.yaxis_1.setGeometry(QtCore.QRect(10, 250, 281, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yaxis_1.sizePolicy().hasHeightForWidth())
        self.yaxis_1.setSizePolicy(sizePolicy)
        self.yaxis_1.setObjectName("yaxis_1")
        self.general = PlotWidget(self.gr_axis)
        self.general.setGeometry(QtCore.QRect(10, 470, 281, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general.sizePolicy().hasHeightForWidth())
        self.general.setSizePolicy(sizePolicy)
        self.general.setObjectName("general")
        self.general_2 = PlotWidget(self.gr_axis)
        self.general_2.setGeometry(QtCore.QRect(310, 470, 281, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_2.sizePolicy().hasHeightForWidth())
        self.general_2.setSizePolicy(sizePolicy)
        self.general_2.setObjectName("general_2")
        self.tunepid = QtWidgets.QGroupBox(self.centralwidget)
        self.tunepid.setGeometry(QtCore.QRect(230, 130, 431, 221))
        self.tunepid.setObjectName("tunepid")
        self.pushpid = QtWidgets.QPushButton(self.tunepid)
        self.pushpid.setGeometry(QtCore.QRect(350, 30, 75, 21))
        self.pushpid.setObjectName("pushpid")
        self.label_6 = QtWidgets.QLabel(self.tunepid)
        self.label_6.setGeometry(QtCore.QRect(80, 30, 16, 21))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.tunepid)
        self.label_8.setGeometry(QtCore.QRect(170, 30, 16, 21))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.tunepid)
        self.label_7.setGeometry(QtCore.QRect(260, 30, 21, 21))
        self.label_7.setObjectName("label_7")
        self.kp = QtWidgets.QDoubleSpinBox(self.tunepid)
        self.kp.setGeometry(QtCore.QRect(100, 30, 62, 22))
        self.kp.setMaximum(10000.0)
        self.kp.setObjectName("kp")
        self.ki = QtWidgets.QDoubleSpinBox(self.tunepid)
        self.ki.setGeometry(QtCore.QRect(190, 30, 62, 22))
        self.ki.setMaximum(10000.0)
        self.ki.setObjectName("ki")
        self.kd = QtWidgets.QDoubleSpinBox(self.tunepid)
        self.kd.setGeometry(QtCore.QRect(280, 30, 62, 22))
        self.kd.setMaximum(10000.0)
        self.kd.setObjectName("kd")
        self.label_11 = QtWidgets.QLabel(self.tunepid)
        self.label_11.setGeometry(QtCore.QRect(170, 60, 16, 21))
        self.label_11.setObjectName("label_11")
        self.pushpid_1 = QtWidgets.QPushButton(self.tunepid)
        self.pushpid_1.setGeometry(QtCore.QRect(350, 60, 75, 21))
        self.pushpid_1.setObjectName("pushpid_1")
        self.label_10 = QtWidgets.QLabel(self.tunepid)
        self.label_10.setGeometry(QtCore.QRect(260, 60, 21, 21))
        self.label_10.setObjectName("label_10")
        self.kp_1 = QtWidgets.QDoubleSpinBox(self.tunepid)
        self.kp_1.setGeometry(QtCore.QRect(100, 60, 62, 22))
        self.kp_1.setMaximum(10000.0)
        self.kp_1.setObjectName("kp_1")
        self.ki_1 = QtWidgets.QDoubleSpinBox(self.tunepid)
        self.ki_1.setGeometry(QtCore.QRect(190, 60, 62, 22))
        self.ki_1.setMaximum(10000.0)
        self.ki_1.setObjectName("ki_1")
        self.label_9 = QtWidgets.QLabel(self.tunepid)
        self.label_9.setGeometry(QtCore.QRect(80, 60, 16, 21))
        self.label_9.setObjectName("label_9")
        self.kd_1 = QtWidgets.QDoubleSpinBox(self.tunepid)
        self.kd_1.setGeometry(QtCore.QRect(280, 60, 62, 22))
        self.kd_1.setMaximum(10000.0)
        self.kd_1.setObjectName("kd_1")
        self.label_12 = QtWidgets.QLabel(self.tunepid)
        self.label_12.setGeometry(QtCore.QRect(170, 90, 16, 21))
        self.label_12.setObjectName("label_12")
        self.pushpid_2 = QtWidgets.QPushButton(self.tunepid)
        self.pushpid_2.setGeometry(QtCore.QRect(350, 90, 75, 21))
        self.pushpid_2.setObjectName("pushpid_2")
        self.label_13 = QtWidgets.QLabel(self.tunepid)
        self.label_13.setGeometry(QtCore.QRect(260, 90, 21, 21))
        self.label_13.setObjectName("label_13")
        self.kp_2 = QtWidgets.QDoubleSpinBox(self.tunepid)
        self.kp_2.setGeometry(QtCore.QRect(100, 90, 62, 22))
        self.kp_2.setMaximum(10000.0)
        self.kp_2.setObjectName("kp_2")
        self.ki_2 = QtWidgets.QDoubleSpinBox(self.tunepid)
        self.ki_2.setGeometry(QtCore.QRect(190, 90, 62, 22))
        self.ki_2.setMaximum(10000.0)
        self.ki_2.setObjectName("ki_2")
        self.label_14 = QtWidgets.QLabel(self.tunepid)
        self.label_14.setGeometry(QtCore.QRect(80, 90, 16, 21))
        self.label_14.setObjectName("label_14")
        self.kd_2 = QtWidgets.QDoubleSpinBox(self.tunepid)
        self.kd_2.setGeometry(QtCore.QRect(280, 90, 62, 22))
        self.kd_2.setMaximum(10000.0)
        self.kd_2.setObjectName("kd_2")
        self.label_15 = QtWidgets.QLabel(self.tunepid)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tunepid)
        self.label_16.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tunepid)
        self.label_17.setGeometry(QtCore.QRect(10, 90, 47, 20))
        self.label_17.setObjectName("label_17")
        self.getoldpid = QtWidgets.QPushButton(self.tunepid)
        self.getoldpid.setGeometry(QtCore.QRect(284, 120, 141, 31))
        self.getoldpid.setObjectName("getoldpid")
        self.rightspeed = QtWidgets.QSlider(self.tunepid)
        self.rightspeed.setGeometry(QtCore.QRect(80, 160, 160, 22))
        self.rightspeed.setMaximum(100)
        self.rightspeed.setOrientation(QtCore.Qt.Horizontal)
        self.rightspeed.setObjectName("rightspeed")
        self.leftspeed = QtWidgets.QSlider(self.tunepid)
        self.leftspeed.setGeometry(QtCore.QRect(80, 190, 160, 22))
        self.leftspeed.setMaximum(100)
        self.leftspeed.setOrientation(QtCore.Qt.Horizontal)
        self.leftspeed.setObjectName("leftspeed")
        self.label_30 = QtWidgets.QLabel(self.tunepid)
        self.label_30.setGeometry(QtCore.QRect(10, 160, 61, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tunepid)
        self.label_31.setGeometry(QtCore.QRect(10, 190, 61, 20))
        self.label_31.setObjectName("label_31")
        self.Rightpercent = QtWidgets.QLabel(self.tunepid)
        self.Rightpercent.setGeometry(QtCore.QRect(260, 160, 47, 21))
        self.Rightpercent.setText("")
        self.Rightpercent.setObjectName("Rightpercent")
        self.Leftpercent = QtWidgets.QLabel(self.tunepid)
        self.Leftpercent.setGeometry(QtCore.QRect(260, 190, 47, 21))
        self.Leftpercent.setText("")
        self.Leftpercent.setObjectName("Leftpercent")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(360, 360, 301, 331))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.label_5.setObjectName("label_5")
        self.controlmode_label = QtWidgets.QLabel(self.groupBox_7)
        self.controlmode_label.setGeometry(QtCore.QRect(50, 20, 47, 21))
        self.controlmode_label.setText("")
        self.controlmode_label.setObjectName("controlmode_label")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.choice_mode.raise_()
        self.groupBox_4.raise_()
        self.gr_axis.raise_()
        self.tunepid.raise_()
        self.groupBox_7.raise_()
        MK1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MK1)
        self.statusbar.setObjectName("statusbar")
        MK1.setStatusBar(self.statusbar)

        self.retranslateUi(MK1)

        # event device combo box
        self.device.currentIndexChanged.connect(self.choiceJoystick)
        self.device.popupAboutToBeShown.connect(self.getjoystick)

        # event connect button
        self.connect.clicked.connect(self.connectbtn)

        # event auto/manual/stop button
        self.auto_2.clicked.connect(self.auto_mode)
        self.stop.clicked.connect(self.stop_mode)
        self.manual.clicked.connect(self.manual_mode)
        self.debug.clicked.connect(self.debug_mode)

        # event pusshpid button
        self.pushpid.clicked.connect(self.sendpid)
        self.pushpid_1.clicked.connect(self.sendpid)
        self.pushpid_2.clicked.connect(self.sendpid)

        # event change value debug
        self.rightspeed.valueChanged.connect(self.changevalue)
        self.leftspeed.valueChanged.connect(self.changevalue)

        # addplot
        # xaxis
        self.xaxis.setBackground('w')
        self.xaxis.showGrid(x=True, y=True)
        self.xaxis.setYRange(Y_min, Y_max, padding=0)
        self.xaxis.setMouseEnabled(x=False, y=False)
        # yaxis
        self.yaxis.setBackground('w')
        self.yaxis.showGrid(x=True, y=True)
        self.yaxis.setYRange(Y1_min, Y1_max, padding=0)
        self.yaxis.setMouseEnabled(x=False, y=False)
        # xaxis_1
        self.xaxis_1.setBackground('w')
        self.xaxis_1.showGrid(x=True, y=True)
        self.xaxis_1.setYRange(Y_min, Y_max, padding=0)
        self.xaxis_1.setMouseEnabled(x=False, y=False)
        # yaxis_1
        self.yaxis_1.setBackground('w')
        self.yaxis_1.showGrid(x=True, y=True)
        self.yaxis_1.setYRange(Y_min, Y_max, padding=0)
        self.yaxis_1.setMouseEnabled(x=False, y=False)
        # general
        self.general.setBackground('w')
        self.general.showGrid(x=True, y=True)
        self.general.setYRange(Y_min, Y_max, padding=0)
        self.general.setMouseEnabled(x=False, y=False)
        # general
        self.general_2.setBackground('w')
        self.general_2.showGrid(x=True, y=True)
        self.general_2.setYRange(Y_min, Y_max, padding=0)
        self.general_2.setMouseEnabled(x=False, y=False)
        #updateGUItimer
        self.x = list(range(listrange))
        self.y1 = list(range(listrange))
        self.y2 = list(range(listrange))
        self.y3 = list(range(listrange))
        self.y4 = list(range(listrange))
        self.timer=QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.refreshUI)
        self.timer.start()
        pen = pg.mkPen(color=(0, 0, 0))
        self.data_line1=self.xaxis.plot(self.x, self.y1, pen=pen)
        self.data_line2=self.yaxis.plot(self.x, self.y2, pen=pen)

        # startup
        self.stop.setEnabled(False)
        self.connect.setStyleSheet('QPushButton {color: green;}')
        self.connect.setText('CONNECT')
        # self.main_process()

        QtCore.QMetaObject.connectSlotsByName(MK1)

    def retranslateUi(self, MK1):
        _translate = QtCore.QCoreApplication.translate
        MK1.setWindowTitle(_translate("MK1", "Zero 2"))
        self.groupBox.setTitle(_translate("MK1", "Connect"))
        self.COM.setCurrentText(_translate("MK1", "COM1"))
        self.COM.setItemText(0, _translate("MK1", "COM1"))
        self.COM.setItemText(1, _translate("MK1", "COM2"))
        self.COM.setItemText(2, _translate("MK1", "COM3"))
        self.COM.setItemText(3, _translate("MK1", "COM4"))
        self.COM.setItemText(4, _translate("MK1", "COM5"))
        self.COM.setItemText(5, _translate("MK1", "COM6"))
        self.COM.setItemText(6, _translate("MK1", "COM7"))
        self.COM.setItemText(7, _translate("MK1", "COM8"))
        self.COM.setItemText(8, _translate("MK1", "COM9"))
        self.COM.setItemText(9, _translate("MK1", "COM10"))
        self.COM.setItemText(10, _translate("MK1", "COM11"))
        self.COM.setItemText(11, _translate("MK1", "COM12"))
        self.COM.setItemText(12, _translate("MK1", "COM13"))
        self.COM.setItemText(13, _translate("MK1", "COM14"))
        self.connect.setText(_translate("MK1", "DISCONNECT"))
        self.label.setText(_translate("MK1", "COM:"))
        self.groupBox_2.setTitle(_translate("MK1", "Joystick"))
        self.label_2.setText(_translate("MK1", "Device:"))
        self.label_3.setText(_translate("MK1", "ID:"))
        self.label_4.setText(_translate("MK1", "Status:"))
        self.choice_mode.setTitle(_translate("MK1", "Mode"))
        self.auto_2.setText(_translate("MK1", "AUTO"))
        self.manual.setText(_translate("MK1", "MANUAL"))
        self.stop.setText(_translate("MK1", "STOP"))
        self.debug.setText(_translate("MK1", "DEBUG"))
        self.groupBox_4.setTitle(_translate("MK1", "Received/Send data"))
        self.re_se_data.setHtml(_translate("MK1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.send.setText(_translate("MK1", "SEND"))
        self.gr_axis.setTitle(_translate("MK1", "Axis"))
        self.tunepid.setTitle(_translate("MK1", "PID"))
        self.pushpid.setText(_translate("MK1", "PUSH"))
        self.label_6.setText(_translate("MK1", "Kp:"))
        self.label_8.setText(_translate("MK1", "Ki:"))
        self.label_7.setText(_translate("MK1", "Kd:"))
        self.label_11.setText(_translate("MK1", "Ki:"))
        self.pushpid_1.setText(_translate("MK1", "PUSH"))
        self.label_10.setText(_translate("MK1", "Kd:"))
        self.label_9.setText(_translate("MK1", "Kp:"))
        self.label_12.setText(_translate("MK1", "Ki:"))
        self.pushpid_2.setText(_translate("MK1", "PUSH"))
        self.label_13.setText(_translate("MK1", "Kd:"))
        self.label_14.setText(_translate("MK1", "Kp:"))
        self.label_15.setText(_translate("MK1", "Right Motor"))
        self.label_16.setText(_translate("MK1", "Left Motor"))
        self.label_17.setText(_translate("MK1", "Angle"))
        self.getoldpid.setText(_translate("MK1", "GET PID"))
        self.label_30.setText(_translate("MK1", "Right Motor"))
        self.label_31.setText(_translate("MK1", "Left Motor"))
        self.groupBox_7.setTitle(_translate("MK1", "Status"))
        self.label_5.setText(_translate("MK1", "Mode:"))

    def refreshUI(self):
        global datasendalpha
        if(control==mode.manual or control==mode.debug):
            self.x = self.x[1:]
            self.x.append(self.x[-1] + 1)
            self.y1= self.y1[1:]
            self.y2= self.y2[1:]
            if(control==mode.manual):
                self.y1.append(axis[0])
                self.y2.append(axis[1])
            elif(control==mode.debug):
                self.y1.append(globaldebug[0])
                self.y2.append(globaldebug[1])
            self.data_line1.setData(self.x, self.y1)
            self.data_line2.setData(self.x, self.y2)
        elif(control==mode.stop):
            datasendalpha="STOP"
        else:
            datasendalpha="AUTO"
        if(comconnect==True):
            transmit.write(datasendalpha.encode())
            print(datasendalpha)

    def connectbtn(self):
        global comconnect,transmit
        NameCOM = self.COM.currentText()
        try:
            if(comconnect == False):
                self.transmit = serial.Serial(NameCOM, 115200, timeout=2.5)
                self.COM.setEnabled(False)
                self.connect.setText('DISCONNECT')
                self.connect.setStyleSheet('QPushButton {color: red;}')
                self.re_se_data.append('Serial port ' + NameCOM + ' opened')
                comconnect = True
            else:
                self.COM.setEnabled(True)
                transmit.close()
                self.connect.setText('CONNECT')
                self.connect.setStyleSheet('QPushButton {color: green;}')
                self.re_se_data.append('Serial port ' + NameCOM + ' closed')
                comconnect = False
        except IOError:
            if(comconnect == False):
                self.re_se_data.append('Serial port ' + NameCOM + ' opening error')
            else:
                self.re_se_data.append('Serial port ' + NameCOM + ' closing error')

    def manual_mode(self):
        global control                          
        self.controlmode_label.setText("Manual")
        control = mode.manual
        self.timer.setInterval(16)
        self.controlmode()

    def auto_mode(self):
        global control
        self.controlmode_label.setText("Auto")
        control = mode.auto
        self.timer.setInterval(100)
        self.controlmode()

    def stop_mode(self):
        global control
        self.controlmode_label.setText("Stop")
        control = mode.stop
        self.timer.setInterval(100)
        self.controlmode()

    def debug_mode(self):
        global control
        self.controlmode_label.setText("Debug")
        control = mode.debug
        self.timer.setInterval(16)
        self.controlmode()

    def choiceJoystick(self):
        global joystick_choice,choiceJoystickstatus,Joystickconect
        print(self.device.currentIndex())
        choiceJoystickstatus=True
        Joystickconect=True

    def getjoystick(self):
        global joystick_no
        num_joy = pygame.joystick.get_count()
        if (num_joy > 0):
            self.device.clear()
            for x in range(num_joy):
                joystick_no = pygame.joystick.Joystick(x)
                joystick_no.init()
                self.device.addItem(joystick_no.get_name())
                self.ID_device.setText(str(joystick_no.get_id()))

    def controlmode(self):
        global control
        if (control == mode.stop):
            self.stop.setEnabled(False)
            self.auto_2.setEnabled(True)
            self.manual.setEnabled(True)
            self.debug.setEnabled(True)
        elif (control == mode.manual):
            self.stop.setEnabled(True)
            self.auto_2.setEnabled(True)
            self.manual.setEnabled(False)
            self.debug.setEnabled(True)
        elif(control == mode.debug):
            self.stop.setEnabled(True)
            self.auto_2.setEnabled(True)
            self.manual.setEnabled(True)
            self.debug.setEnabled(False)
        else:
            self.stop.setEnabled(True)
            self.auto_2.setEnabled(False)
            self.manual.setEnabled(True)
            self.debug.setEnabled(True)

    def changevalue(self):
        global globaldebug
        globaldebug[0]=int(self.leftspeed.value())
        globaldebug[1]=int(self.rightspeed.value())

    def sendpid(self):
        pass

def backgroundProcess():
    global control,axis,button,datasendalpha,choiceJoystickstatus,joystick_no,joystick_choice,Joystickconect
    cache = []
    datasend=[]
    while(1):
        cachedic=0
        if(choiceJoystickstatus==True):
            choiceJoystickstatus=False
            joystick_no=pygame.joystick.Joystick(joystick_choice)
            joystick_no.init()
        pygame.event.pump()
        if((control==mode.manual  and Joystickconect==True) or control==mode.debug):
            if(control==mode.manual):
                x=round(joystick_no.get_axis(0)*100,0)
                y=-round(joystick_no.get_axis(1)*100,0)
                if(x!=0):
                    alpha=math.atan(y/x)
                    alpha*=(180/3.14)
                else:
                    if(y>=0):
                        alpha=90
                    elif(y<0):
                        alpha=-90

                if(abs(alpha)>60):
                    axis[0]=y
                    axis[1]=y
                elif(abs(alpha)<=30):
                    axis[1]=x
                    axis[0]=-x
                else:
                    if(x>0):
                        axis[1]=y
                        axis[0]=y*abs(alpha/70)
                    else:
                        axis[1]=y*abs(alpha/70)
                        axis[0]=y
                for i in range(5):
                    button[i]=joystick_no.get_button(i)
            else:
                axis[0]=globaldebug[0]
                axis[1]=globaldebug[1]

            for i in range(2):
                if(axis[i]<0 or axis[i]==-0):
                    cacheaxis=abs(axis[i])
                    if (i==0):
                        cachedic+=1
                    else:
                        cachedic+=2
                else:
                    cacheaxis=axis[i]

                if(cacheaxis<10):
                    cache+="00"
                elif (cacheaxis<100):
                    cache+="0"

                if(i==0):
                    cache+=str(int(cacheaxis))
                elif(i==1):
                    cache+=str(int(cacheaxis))
                    cache+=str(int(cachedic))

            # cache+="."
            # cache+=str(len(cache)-1)
            cache+="]"
            datasend=''.join(cache)
            print("{}".format(datasend))
            datasendalpha=datasend
            #transmit.write(datasend.encode())
            cache=[]
            cache+="["
            datasend=[]
        time.sleep(0.016)
        
def UIbuild():
    app = QtWidgets.QApplication(sys.argv)
    MK1 = QtWidgets.QMainWindow()
    ui = Ui_MK1()
    ui.setupUi(MK1)
    MK1.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    pygame.display.init()
    pygame.joystick.init()
    t1=threading.Thread(target=backgroundProcess)
    t2=threading.Thread(target=UIbuild)
    t1.daemon=True
    t1.start()
    t2.start()
    