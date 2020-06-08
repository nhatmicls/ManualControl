import pygame
import time
import serial
import math

NameCOM="COM4"

delta=5
button=[0,0,0,0,0]
axis=[0,0,0]
datasend=[]

def main():
    global delta
    data=0
    cache=[]
    transmit=serial.Serial(NameCOM,115200,timeout=2.5)

    time.sleep(1)
    
    while(1):
        if((data==400 and delta >0) or (data==0 and delta < 0)):
            delta=-delta
        data+=delta

        #Get and calc data from joystick

        for i in range(2):
            axis[i]=round(data)

            if(axis[i]==0):
                    axis[i]=1
            if(axis[i]<0):
                cacheaxis=abs(axis[i])
                cachedic=1
            else:
                cacheaxis=axis[i]
                cachedic=0

            if(cacheaxis<10):
                cache+="00"
            elif (cacheaxis<100):
                cache+="0"

            cache+=str(cacheaxis)
            cache+=str(cachedic)

        # cache+="."
        cache+=str(len(cache)-1)
        cache+="]"
        datasend=''.join(cache)
        #cache=datasend.encode()
        #print(type(datasend))
        print("{}".format(datasend))
        transmit.write(datasend.encode())
        time.sleep(0.02)
        cache=[]
        cache+="["
        datasend=[] 

if __name__ == "__main__":
    main()