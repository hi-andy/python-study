import multiprocessing
import time
import os


def run(name) :
    # print('Hello, %s' %name)
    print('model name: ', __name__ )
    print('Parent id: ', os.getppid())
    print('Process id: ', os.getpid())
    print('\n')
    # time.sleep(100)


if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run, args=('Bob %s' %i,))
        p.start()