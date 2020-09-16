import time
import serial
import math

NameCOM="COM4"

delta=5
button=[0,0,0,0,0]
cache=[]
datasend=[]
receivebuffer=[]

def main():
    global delta
    transmit=serial.Serial(NameCOM,115200,timeout=2.5)

    time.sleep(1)
    
    while(1):
        receivebuffer=transmit.read(1)
        cache=str(receivebuffer)
        cache=cache.replace('b\'','')
        cache=cache.replace('\'','')
        datasend=str(cache)
        print("{}{}".format(datasend,type(datasend)))
        if(len(datasend)>0):
            transmit.write(datasend.encode())

if __name__ == "__main__":
    main()