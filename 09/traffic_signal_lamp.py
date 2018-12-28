import threading
import time


event = threading.Event()


def lighter() :
    count = 0
    event.set()
    while True:
        if count > 5 and count <= 10:
            event.clear()
            print("\033[41;1mred light is on ...\033[0m")
        elif count >= 10:
            event.set()
            count = 0
        else :
            print("\033[42;1mgreen light is on ...\033[0m")
        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():
            print('[%s] running....' %name)
            time.sleep(1)
        else:
            print('[%s] red waiting....' %name)
            event.wait()

light = threading.Thread(target=lighter,)
light.start()


car1 = threading.Thread(target=car, args=('Tesla',))
car1.start()