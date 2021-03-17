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

import os
from MK1 import *

# define number
listrange = 63
Y_min = -110
Y_max = 110
Y1_min = 110
Y1_max = -110
ippppp = 0
timergetdata=200

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
dataread=[]
transmit=[]
comconnect = False
control = mode.stop
lastcontrol = mode.stop
globaldebug=[0,0]
PIDdata=[0,0,0,0,0,0,0,0,0]

class GUI_Init(Ui_MK1):
    def __init__(self):
        super(Ui_MK1,self).__init__()
        self.setupUi()
        self.setupUi1()

    def setupUi1(self):
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
        #timergetdata
        self.timergetdata=QtCore.QTimer()
        self.timergetdata.setInterval(timergetdata)
        self.timergetdata.timeout.connect(self.getdata)
        self.timergetdata.start()

        # startup
        self.stop.setEnabled(False)
        self.connect.setStyleSheet('QPushButton {color: green;}')
        self.connect.setText('CONNECT')
        # self.main_process()

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
            self.transmit.write(datasendalpha.encode())
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
                self.transmit.close()
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
        global PIDdata

    def getdata(self):
        global dataread
        print('Hello mother facker')

class backgroundProcess():
    def __init__(self):
        pass

    def getdatafromJoystick():
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
                cache+=str(len(cache))
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
    GUI = GUI_Init()
    GUI.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    UIbuild()