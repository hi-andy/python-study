import multiprocessing
import time
import os


def run(qq) :
    qq.put([123, None, 'Process'])


if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=run, args=(q,))
    p.start()

    print(q.get())

    p.join()