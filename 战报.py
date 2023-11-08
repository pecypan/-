from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime

Location = 40982  # 252start
location_list = []


def zi_dong_deng_lu(url_):
    base = Base()
    base.config(0)
    base.driver.get(url_)
    delay()
    while True:
        print('删除')
        delay(1)
    base.driver.quit()


if __name__ == '__main__':
    url = 'http://sh27.caihonger.com/union/unionwarnoticelist.php?t=13832862066228872509&u=QVZWY2NBVXdVek5TTWdoalcyc0VZZ1l3QTJaUk1nY3lBakVCT3dROQ_c_c&k=353&c=0'
    zi_dong_deng_lu(url)
