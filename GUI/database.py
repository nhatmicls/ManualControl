from dataclasses import dataclass
from typing import List

@dataclass
class velocity_t:
    velocity1: float=10
    velocity2: float=0

@dataclass
class position_t:
    position1: int=0
    position2: int=0

@dataclass
class MPU6050_t:
    accel_x: float=0
    accel_y: float=0
    accel_z: float=0

    gyro_x: float=0
    gyro_y: float=0
    gyro_z: float=0

    roll: float=0
    pitch: float=0

@dataclass
class PID_t:
    Kp: float=0
    Ki: float=0
    Kd: float=0

    P_part: float=0
    I_part: float=0
    D_part: float=0
    I_saturation: float=0

    error: float=0
    last_error: float=0

@dataclass
class prama_t:
    vector: List[velocity_t]
    position: List[position_t]
    imu: List[MPU6050_t]    
    PID_tilt: List[PID_t]
    PID_vel: List[PID_t]

class main_database(prama_t):
    def __init__(self):
        self.velocity=velocity_t()
        self.position=position_t()
        self.imu=MPU6050_t()
        self.PID_ti=PID_t()
        self.PID_ve=PID_t()

database = main_database()