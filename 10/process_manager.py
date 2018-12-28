import multiprocessing
import time
import os


def run(dict, list) :
    dict[1] = '1'
    dict['2'] = 2
    dict[0.25] = None

    list.append(os.getpid())
    print(list)



if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))
        p_list = []

        for i in range(10):
            p = multiprocessing.Process(target=run, args=(d, l,))
            p.start()
            p_list.append(p)

        for p in p_list:
            p.join()

        print(d)
        print(l)