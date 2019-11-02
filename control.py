import pygame
import time
import serial
import math

NameCOM="COM4"

button=[0,0,0,0,0]
axis=[0,0,0]
datasend=[]

def main():
    cache=[]
    cache1=[]
    transmit=serial.Serial(NameCOM,115200,timeout=2.5)

    pygame.display.init()
    pygame.joystick.init()
    print("Number device found: ",pygame.joystick.get_count())

    controljoy=pygame.joystick.Joystick(0)
    controljoy.init()
    #print(controljoy.get_init())
    print("ID: ",controljoy.get_id())
    print("Name device: ",controljoy.get_name())
    print("Number of axis: ",controljoy.get_numaxes())
    print("Number of ball: ",controljoy.get_numballs())
    print("Number of button: ",controljoy.get_numbuttons())
    print("Number of hat button: ",controljoy.get_numhats())
    time.sleep(1)
    while(1):
        pygame.event.pump()
        for i in range(2):
            axis[i]=int(abs(round(controljoy.get_axis(i)*100,0)))
            cache=str(axis[i])
            if(axis[i]<10):
                cache="00"+cache
            elif(axis[i]<100):
                cache="0"+cache
            cache1+=cache
        for i in range(5):
            button[i]=controljoy.get_button(i)

        datasend=''.join(cache1)
        #print(type(datasend))
        print("{}\n".format(datasend))
        transmit.write(datasend.encode())
        cache1=[]
        datasend=[] 


if __name__ == "__main__":
    main()