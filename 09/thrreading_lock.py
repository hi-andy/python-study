import threading
import time


count = 0
lock = threading.Lock()

def run(p1) :
    lock.acquire()  # 3.x 可不加锁，加锁变串行
    global count
    count += 1
    lock.release()


t_list = []
for i in range(50):
    t = threading.Thread(target=run, args=('t-%s' %i,))
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()


print('Number: ', count)