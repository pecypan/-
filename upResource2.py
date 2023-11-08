from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime


def fun(list_):
    base = Base()
    base.config(1)
    for url_ in list_:
        logger.info(f'------------------------{url_}----------------------')
        base.driver.get(url_)
        city_list = base.locate_a('all')
        for city in city_list:
            base.click_word(city)
            base.click_word('资源')
            while True:
                base.click_word('一键')
                base.click_word('返回')
                a = base.is_text_exit('还需')
                if a == 1:
                    base.click_word('速建')
                    base.click_word('返回')
                else:
                    base.click_word('首页')
                    base.click_word('系统')
                    base.click_word('切换')
                    break

def autoResours(base):
    city_list = base.locate_a('all')
    for city in city_list:
        base.click_word(city)
        myName = base.get_maincity_name()
        base.click_word(myName)
        city_names = base.get_citys_names()
        for city_name in city_names:
            base.click_word(city_name)
            base.click_word('资源')
            index_sheng = base.is_text_exit('升')
            if index_sheng == 1:
                base.shen_zi_yuan()
                base.click_word('返回')
                base.click_word('一键')
            base.click_word('首页')
            base.click_word('建筑')
            index_sheng = base.is_text_exit('升')
            if index_sheng == 1:
                base.shen_jian_zhu()
                base.click_word(myName)
                continue
            base.click_word('首页')
            base.click_word(myName)
        base.click_word('首页')
        base.click_word('系统')
        base.click_word('切换好汉')


def shen_zi_yuan(base_, city_names):
    for i in range(0, 11):
        base_.click_word(city_names[i])
        base_.click_word('资源')
        while True:
            base_.shen_zi_yuan()
            index = base_.is_text_exit('不足')
            if index == 1:
                base_.click_word('首页')
                base_.click_word('系统')
                base_.click_word('切换')
                break
            base_.click_word('速建')
            base_.click_word('返回')


def kai_hui_yuan(base_, city_name_):
    for i in range(0, 11):
        base_.click_word(city_name_[i])
        # base_.click_word('状态')
        # base_.click_word('新手牌')
        # base_.click_word('单个使用')
        # base_.click_word('首页')
        base_.click_word('建筑')
        base_.click_word('一键')
        base_.click_word('首页')
        base_.click_word('资源')
        base_.click_word('一键')
        for i in range(0, 6):
            base_.driver.back()

def zi_dong_deng_lu(url_, list_a, list_p):
    base = Base()
    base.config(1)
    base.driver.get(url_)
    delay()
    # 登录
    for i in range(0, 100):
        logger.info(f'账号：{list_a[i]}_______________________________________________________密码：{list_p[i]}')
        base.input_acc_pass(list_a[i], list_p[i])
        base.click_button('确定')
        # 选择区服
        base.select_sh(5)
        city_list = base.locate_a('all')
        delay()
        # shen_zi_yuan(base, city_list)
        kai_hui_yuan(base, city_list)
        base.click_word('重新登录')


if __name__ == '__main__':
    # list_AandP = read_csv2list()
    # list_A = []
    # list_P = []
    # for i in range(0, 300):
    #     list_A.append(list_AandP[i][0])
    #     list_P.append(list_AandP[i][1])

    # # with open('27区自己号书签.txt', 'r') as f:
    # #     url_list = f.readlines()
    # url = 'http://sh.caihonger.com/login.php'
    # zi_dong_deng_lu(url, list_A, list_P)

    # # fun(url_list)

    # -------------------------------------------------------------------------31------------------------------------------------------------------------------------------------------------------------------------------
    url_list = [
        'http://sh31.caihonger.com/selectKings.php?u=RGpFSloxTS9VVGNCWUF0aENUY0VZd1EzQ21JR2J3PT0_c&t=13437594576846656625',
        'http://sh31.caihonger.com/selectKings.php?u=QmpsY01nQnNEbWhVTlZzeFdtUUFad0F6QjJkVk5BPT0_c&t=96509222651156453374&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QnpnQWJsUTRWRElCWUFsakN6VUNaUUl4QUdoWFB3PT0_c&t=73357735097901042776&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QVQ1ZlBBTnJCbUJRTXdsZ0RqRlNNUUk5QTJRRFlnPT0_c&t=63298572785305090746&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QXp3TFpRVnBEMmxiT2dCcUR6RlVNMUpoVURBS2FnPT0_c&t=46474044554666572643&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=RGpFQWFBZHVEMnhUTVExaFdtRUNZd0F5Vmo0RFpRPT0_c&t=62256098960617125657&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=VTJ3QWFGSTdWRGRXTkFGdFdtRlVOUU14Vno5U053PT0_c&t=58788822260315899553&c=0&t=58788822260315899553&u=VTJ3QWFGSTdWRGRXTkFGdFdtRlVOUU14Vno5U053PT0_c&k=1119&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QXp3SllWNDNVakVDWUFwbURqVlNNd1EyQ21JRllRPT0_c&t=51640123345572052114&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QmprQWFBQnBWalVIWlZvMkNqRlVOUVUzVmo0R1pRPT0_c&t=44890266147756239107&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=VldvQWFBQnBCR2RXTkFCc0NUSlhObFprQm00Rlp3PT0_c&t=30036761497506828158&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QXp3TVpGUTlBR01IWlFCc1hHZFJNRkpnQTJzRlpBPT0_c&t=51959919074412943167&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=RHpCYU1nUnRVakZhT0ZzM1hXWlRNZ014VkR3SFp3PT0_c&t=66599823577042819715&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QkRzUFoxVThCV1pYTlF0bkRUWUNZMVprQzJJS1l3PT0_c&t=39802592168217782288&c=0',
    ]
    base = Base()
    base.config(1)
    while True:
        for url in url_list:
            base.driver.get(url)
            autoResours(base)
