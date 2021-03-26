import os
from enum import Enum
import struct

from database import database

class msg_id_t(Enum):
    imu_gyro = 0
    imu_gyro_bias = 1
    imu_accel = 2
    imu_accel_bias = 3
    imu_rpy = 4
    motor_pos = 5
    motor_vel = 6
    pid_tilt = 7
    pid_vel = 8
    save_load_params = 9

class processData():
    def __init__(self):
        super(processData).__init__()

    def RHY(self,ID):
        pass

class messageProcess():
    def __init__(self):
        super(messageProcess).__init__()

    def messagePack(self,msg,buffer):
        msg_id=int(msg)
        if (msg_id==msg_id_t.imu_gyro.value):
            print('1')
        elif (msg_id==msg_id_t.imu_gyro_bias.value):
            print('2')
        elif (msg_id==msg_id_t.imu_accel.value):
            print('3')
        elif (msg_id==msg_id_t.imu_accel_bias.value):
            print('4')
        elif (msg_id==msg_id_t.imu_rpy.value):
            print('5')
        elif (msg_id==msg_id_t.motor_pos.value):
            print('6')
        elif (msg_id==msg_id_t.motor_vel.value):
            print('7')
        elif (msg_id==msg_id_t.pid_tilt.value):
            print('8')
        elif (msg_id==msg_id_t.pid_vel.value):
            print('9')
        elif (msg_id==msg_id_t.save_load_params.value):
            print('10')
        else:
            print('Wrong ID message !')

    def messageDecoder(self,msg,len_data):
        msg_id=msg[2]
        len_msg=msg[1]
        if (len_msg != len_data):
            print('Message missing element')
            return 1
        if (msg_id==msg_id_t.imu_gyro.value):
            database.imu.gyro_x=struct.unpack("<f",msg[3:7])
            print('1')
        elif (msg_id==msg_id_t.imu_gyro_bias.value):
            print('2')
        elif (msg_id==msg_id_t.imu_accel.value):
            print('3')
        elif (msg_id==msg_id_t.imu_accel_bias.value):
            print('4')
        elif (msg_id==msg_id_t.imu_rpy.value):
            print('5')
        elif (msg_id==msg_id_t.motor_pos.value):
            print('6')
        elif (msg_id==msg_id_t.motor_vel.value):
            print('7')
        elif (msg_id==msg_id_t.pid_tilt.value):
            print('8')
        elif (msg_id==msg_id_t.pid_vel.value):
            print('9')
        elif (msg_id==msg_id_t.save_load_params.value):
            print('10')
        else:
            print('Wrong ID message !')