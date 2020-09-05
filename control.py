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
    # transmit=serial.Serial(NameCOM,115200,timeout=2.5)

    pygame.display.init()
    pygame.joystick.init()
    print("Number device found: ",pygame.joystick.get_count())

    controljoy=pygame.joystick.Joystick(0)
    controljoy.init()
    print(controljoy.get_init())
    print("ID: ",controljoy.get_id())
    print("Name device: ",controljoy.get_name())
    print("Number of axis: ",controljoy.get_numaxes())
    print("Number of ball: ",controljoy.get_numballs())
    print("Number of button: ",controljoy.get_numbuttons())
    print("Number of hat button: ",controljoy.get_numhats())
    time.sleep(1)
    
    while(1):
        pygame.event.pump()
        cachedic = 0
        alpha=0

        #Get and calc data from joystick
        cache=[]
        cache+="["

        x=round(controljoy.get_axis(0)*100,0)
        y=-round(controljoy.get_axis(1)*100,0)
        if(x!=0):
            alpha=math.atan(y/x)
            alpha*=(180/3.14)
        else:
            if(y>=0):
                alpha=90
            elif(y<0):
                alpha=-90

        if(abs(alpha)>80):
            axis[0]=y
            axis[1]=y
        elif(abs(alpha)<=10):
            axis[0]=x
            axis[1]=-x
        else:
            if(x>0):
                axis[0]=y
                axis[1]=y*abs(alpha/100)
            else:
                axis[0]=y*abs(alpha/100)
                axis[1]=y

        for i in range(2):
            if(axis[i]<0 or axis[i]==-0):
                cacheaxis=abs(axis[i])
                if (cacheaxis>70):
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

        for i in range(5):
            button[i]=controljoy.get_button(i)

        # cache+="."
        # cache+=str(len(cache)-1)
        cache+="]"
        datasend=''.join(cache)
        #cache=datasend.encode()
        #print(type(datasend))
        print("{}".format(datasend))
        # print("{}".format(cache))
        # transmit.write(datasend.encode())
        time.sleep(0.02)
        datasend=[] 

if __name__ == "__main__":
    main()