import multiprocessing
import time
import os


def run(i) :
    time.sleep(2)
    print(os.getpid())
    return i

# 回调函数是被主进程调用的
def callback(arg):
    print('exec done: ', arg)



if __name__ == '__main__':
    pool = multiprocessing.Pool(5)
    for i in range(10):
        #pool.apply(func=run, args=(i,))
        #pool.apply_async(func=run, args=(i,))
        pool.apply_async(func=run, args=(i,), callback=callback)

    print('end')
    pool.close()
    pool.join()