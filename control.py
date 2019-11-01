import inputs
import pygame
import time

def main():
    pygame.display.init()
    pygame.joystick.init()
    print(pygame.joystick.get_count())

    controljoy=pygame.joystick.Joystick(0)
    controljoy.init()
    print(controljoy.get_init())
    print(controljoy.get_id())
    print(controljoy.get_name())
    print(controljoy.get_numaxes())
    print(controljoy.get_numballs())
    print(controljoy.get_numbuttons())
    print(controljoy.get_numhats())
    time.sleep(3)
    while(1):
        pygame.event.pump()
        x=round(controljoy.get_axis(0)*100,0)
        y=-round(controljoy.get_axis(1)*100,0)
        z=-round(controljoy.get_axis(2)*100,0)
        print("X:%s,Y:%s,Z:%s" %(x,y,z))


if __name__ == "__main__":
    main()