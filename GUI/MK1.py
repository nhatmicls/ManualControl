# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MK1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Enum
import serial

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")


class mode(Enum):
    auto = 1
    manual = 2
    stop = 0


NameCOM = []
transmit = []
comconnect = False
control = mode.stop


class Ui_MK1(object):
    def setupUi(self, MK1):
        MK1.setObjectName("MK1")
        MK1.setEnabled(True)
        MK1.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MK1.sizePolicy().hasHeightForWidth())
        MK1.setSizePolicy(sizePolicy)
        MK1.setMinimumSize(QtCore.QSize(1280, 720))
        MK1.setMaximumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "C:/Users/ASUS/Pictures/82362862_762415024581207_8972626692153540608_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MK1.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MK1)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 201, 111))
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
        self.connect = QtWidgets.QPushButton(self.groupBox)
        self.connect.setGeometry(QtCore.QRect(40, 50, 151, 51))
        self.connect.setObjectName("connect")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 20, 671, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 47, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 47, 16))
        self.label_3.setObjectName("label_3")
        self.ID_device = QtWidgets.QLabel(self.groupBox_2)
        self.ID_device.setGeometry(QtCore.QRect(60, 40, 601, 16))
        self.ID_device.setText("")
        self.ID_device.setObjectName("ID_device")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 47, 16))
        self.label_4.setObjectName("label_4")
        self.SS_device = QtWidgets.QLabel(self.groupBox_2)
        self.SS_device.setGeometry(QtCore.QRect(60, 60, 601, 16))
        self.SS_device.setText("")
        self.SS_device.setObjectName("SS_device")
        self.device = QtWidgets.QComboBox(self.groupBox_2)
        self.device.setGeometry(QtCore.QRect(60, 19, 601, 21))
        self.device.setObjectName("device")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 140, 201, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.auto_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.auto_2.setGeometry(QtCore.QRect(20, 30, 171, 61))
        self.auto_2.setObjectName("auto_2")
        self.manual = QtWidgets.QPushButton(self.groupBox_3)
        self.manual.setGeometry(QtCore.QRect(20, 100, 171, 61))
        self.manual.setObjectName("manual")
        self.stop = QtWidgets.QPushButton(self.groupBox_3)
        self.stop.setGeometry(QtCore.QRect(20, 170, 171, 61))
        self.stop.setObjectName("stop")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(910, 20, 351, 361))
        self.groupBox_4.setObjectName("groupBox_4")
        self.re_se_data = QtWidgets.QTextBrowser(self.groupBox_4)
        self.re_se_data.setEnabled(True)
        self.re_se_data.setGeometry(QtCore.QRect(10, 20, 331, 331))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.re_se_data.sizePolicy().hasHeightForWidth())
        self.re_se_data.setSizePolicy(sizePolicy)
        self.re_se_data.setObjectName("re_se_data")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(230, 140, 671, 241))
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 390, 881, 301))
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(910, 390, 351, 301))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.label_5.setObjectName("label_5")
        self.controlmode_label = QtWidgets.QLabel(self.groupBox_7)
        self.controlmode_label.setGeometry(QtCore.QRect(50, 20, 47, 21))
        self.controlmode_label.setObjectName("controlmode_label")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.groupBox_6.raise_()
        self.groupBox_7.raise_()
        MK1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MK1)
        self.statusbar.setObjectName("statusbar")
        MK1.setStatusBar(self.statusbar)

        # event connect button
        self.connect.clicked.connect(self.connectbtn)

        # event auto/manual/stop button
        self.auto_2.clicked.connect(self.auto_mode)
        self.stop.clicked.connect(self.stop_mode)
        self.manual.clicked.connect(self.manual_mode)

        # startup
        self.stop.setEnabled(False)

        # addplot

        self.retranslateUi(MK1)
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
        self.connect.setStyleSheet('QPushButton {color: green;}')
        self.connect.setText(_translate("MK1", "CONNECT"))
        self.label.setText(_translate("MK1", "COM:"))
        self.groupBox_2.setTitle(_translate("MK1", "Joystick"))
        self.label_2.setText(_translate("MK1", "Device:"))
        self.label_3.setText(_translate("MK1", "ID:"))
        self.label_4.setText(_translate("MK1", "Status:"))
        self.groupBox_3.setTitle(_translate("MK1", "Mode"))
        self.auto_2.setText(_translate("MK1", "AUTO"))
        self.manual.setText(_translate("MK1", "MANUAL"))
        self.stop.setText(_translate("MK1", "STOP"))
        self.groupBox_4.setTitle(_translate("MK1", "Received/Send data"))
        self.re_se_data.setHtml(_translate("MK1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_5.setTitle(_translate("MK1", "Axis"))
        self.groupBox_6.setTitle(_translate("MK1", "Analysis"))
        self.groupBox_7.setTitle(_translate("MK1", "Status"))
        self.label_5.setText(_translate("MK1", "Mode:"))
        self.controlmode_label.setText("Stop")

    def connectbtn(self):
        global comconnect
        NameCOM = self.COM.currentText()
        try:
            transmit = serial.Serial(NameCOM, 115200, timeout=2.5)
            if(comconnect == False):
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
            self.re_se_data.append('Serial port ' + NameCOM + ' opening error')

    def manual_mode(self):
        global control
        self.controlmode_label.setText("Manual")
        control = mode.manual
        self.controlmode()

    def auto_mode(self):
        global control
        self.controlmode_label.setText("Auto")
        control = mode.auto
        self.controlmode()

    def stop_mode(self):
        global control
        self.controlmode_label.setText("Stop")
        control = mode.stop
        self.controlmode()

    def controlmode(self):
        global control
        if (control == mode.stop):
            self.stop.setEnabled(False)
            self.auto_2.setEnabled(True)
            self.manual.setEnabled(True)
        elif (control == mode.manual):
            self.stop.setEnabled(True)
            self.auto_2.setEnabled(True)
            self.manual.setEnabled(False)
        else:
            self.stop.setEnabled(True)
            self.auto_2.setEnabled(False)
            self.manual.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MK1 = QtWidgets.QMainWindow()
    ui = Ui_MK1()
    ui.setupUi(MK1)
    MK1.show()
    sys.exit(app.exec_())
