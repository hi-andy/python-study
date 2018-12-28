import multiprocessing
import time
import os


def run(child) :
    child.send([123, None, 'Process'])
    child.close()


if __name__ == '__main__':
    parent, child = multiprocessing.Pipe()
    p = multiprocessing.Process(target=run, args=(child,))
    p.start()

    print(parent.recv())

    p.join()