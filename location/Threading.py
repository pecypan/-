from threading import Thread, current_thread
from BasePartDLL import *


def threading_1():
    time_after(5)
    thread_num = 1
    print('线程{}结束运行！', thread_num)


def threading_2():
    time_after(5)
    thread_num = 2
    print('线程{}结束运行！', thread_num)


if __name__ == '__main__':
    thread01 = Thread(target=threading_1)
    time_after(10)
    thread02 = Thread(target=threading_2)
    thread02.start()
    thread01.start()