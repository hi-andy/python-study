import threading
import time


def run(p1) :
    print(p1)
    time.sleep(2)

start_time = time.time()
t_list = []
for i in range(50):
    t = threading.Thread(target=run, args=('t-%s' %i,))
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()


print('cost: ', time.time() - start_time)