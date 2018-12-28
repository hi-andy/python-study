import threading
import time


def run(p1) :
    print(p1)
    time.sleep(2)

start_time = time.time()

for i in range(50):
    t = threading.Thread(target=run, args=('t-%s' %i,))
    t.setDaemon(True)
    t.start()




print('cost: ', time.time() - start_time)