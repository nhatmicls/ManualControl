import inputs
import time

def main():
    while(1):
        pads = inputs.devices.gamepads

        if len(pads) == 0:
            print("can't find gamepad")
        else:
            print(pads)

        time.sleep(3)

if __name__ == "__main__":
    main()