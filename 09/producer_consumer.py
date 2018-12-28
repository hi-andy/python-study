import queue
import threading

q = queue.Queue()


def producer():
    while True:
        if q.qsize() < 10:
            for i in range(10):
                q.put('Bone%s' %i)
        else:
            continue


def consumer(name):
    while q.qsize() > 0:
        print('%s got %s' % (name, q.get()))


p = threading.Thread(target=producer, )
c = threading.Thread(target=consumer, args=('hai',))

p.start()
c.start()
