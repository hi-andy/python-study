import time


def timmer(func):
    def wapper(*args, **kwargs):
        star_time = time.time()
        func()
        stop_time = time.time()
        print('The func run time is %s' % (stop_time - star_time))

    return wapper()


@timmer
def func1():
    time.sleep(3)
    print('Func run done!')


func1
