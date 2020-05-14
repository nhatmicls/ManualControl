import threading
import time


def doit():
    time.sleep(5)
    print("Hi")


def main():
    t = threading.Thread(target=doit)
    t.start()
    print("0")
    time.sleep(1)
    print("1")
    t.join()
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("6")
    

if __name__ == "__main__":
    main()