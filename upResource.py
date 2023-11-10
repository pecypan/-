from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime

removestr = 'master.php?a'
tasklist = ['tasks/selectBaowu.php?level=5&t','tasks/dailyReward.php?a=9165&t','tasks/randomReward.php?a=7484&t','building/dianjiangtai.php?a=2218&t','combat/dispatch.php?t','resource/resourceList.php?a=7740&t']

def fun_auto(base, city_list):
    current_url = base.driver.current_url
    for i in range(0,11):
        base.click_word(city_list[i])
        mainurl = base.driver.current_url
        jianzhuurl = mainurl.replace(removestr, tasklist[3])
        base.driver.get(jianzhuurl)
        delay(0.3)
        base.click_word('一键')
        ziyuanurl = mainurl.replace(removestr, tasklist[4])
        base.driver.get(ziyuanurl)
        delay(0.3)
        base.click_word('一键')
        while True:
            exit_loop = True
            page_source = str(base.driver.page_source)
            patt = r'→(\d+)级'
            patter = re.compile(patt)
            result = patter.findall(page_source)
            print(result)
            for i in range(len(result)):
                print(int(result[i]))
                if int(result[i]) <= 18:
                    continue
                else:
                    base.click_word('取消', i)
                    exit_loop = False
                    break
            if exit_loop == True:
                if int(result[len(result) - 1]) <= 18:
                    base.driver.get(current_url)
                    delay(0.3)
                    break
        base.driver.get(current_url)


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


def fun2(base, city_list):
    for i in range(11):
        base.click_word(city_list[i])
        base.click_word('状态')
        try:
            base.click_word('屏蔽播报', 1)
            for i in range(3):
                base.driver.back()
        except:
            base.click_word('首页')
            base.click_word('系统')
            base.click_word('切换')


def fun3(base, city_list):
    for i in range(0, 11):
        base.click_word(city_list[i])
        base.click_word('美女')
        index = base.is_text_exit('小薇')
        if index == 1:
            base.click_word('小薇')
            base.click_word('放逐')
            base.click_word('放逐')
            base.click_word('放逐')
        base.click_word('首页')
        base.click_word('宝箱')
        base.click_word('功能')
        index = base.is_text_exit('神秘')
        if index == 1:
            base.click_word('神秘')
            base.click_word('使用')
            base.click_word('全部使用')
            base.click_word('宝箱')
            base.click_word('功能')
            index2 = base.is_text_exit('梳妆')
            if index2 == 0:
                base.click_word('后页')
                base.click_word('梳妆')
                base.click_word('使用')
                base.click_word('全部使用')
            else:
                base.click_word('梳妆')
                base.click_word('使用')
                base.click_word('全部使用')
        else:
            base.click_word('后页')
            base.click_word('神秘')
            base.click_word('使用')
            base.click_word('全部使用')
            base.click_word('宝箱')
            base.click_word('功能')
            index2 = base.is_text_exit('梳妆')
            if index2 == 0:
                base.click_word('后页')
                base.click_word('梳妆')
                base.click_word('使用')
                base.click_word('全部使用')
            else:
                base.click_word('梳妆')
                base.click_word('使用')
                base.click_word('全部使用')
        base.click_word('首页')
        base.click_word('系统')
        base.click_word('切换')





def shen_zi_yuan(base_, city_names):
    for i in range(11, 22):
        current_url = base_.driver.current_url
        base_.click_word(city_names[i])
        mainurl = base_.driver.current_url
        url1 = mainurl.replace(removestr, tasklist[5])
        base_.driver.get(url1)
        delay(0.3)
        while True:
            base_.shen_zi_yuan()
            index = base_.is_text_exit('不足')
            if index == 1:
                base_.driver.get(current_url)
                break
            base_.click_word('速建')
            base_.click_word('返回')


def kai_hui_yuan(base_, city_name_):
    current_url = base_.driver.current_url
    for i in range(11):
        base_.click_word(city_name_[i])
        # base_.click_word('状态')
        # base_.click_word('新手牌')
        # base_.click_word('单个使用')
        base_.driver.get(current_url)


def zi_dong_deng_lu(url_, list_a, list_p):
    base = Base()
    base.config(0)
    base.driver.get(url_)
    delay()
    # 登录
    for i in range(39, 50):
        logger.info(f'账号：{list_a[i]}_______________________________________________________密码：{list_p[i]}')
        base.input_acc_pass(list_a[i], list_p[i])
        base.click_button('确定')
        # 选择区服
        base.select_sh(4)
        city_list = base.locate_a('all')
        delay()
        shen_zi_yuan(base, city_list)
        # fun2(base, city_list)
        # fun3(base, city_list)
        # fun_auto(base, city_list)
        # kai_hui_yuan(base, city_list)
        base.click_word('重新登录')


if __name__ == '__main__':
    list_AandP = read_csv2list()
    list_A = []
    list_P = []
    for i in range(0, 300):
        list_A.append(list_AandP[i][0])
        list_P.append(list_AandP[i][1])

    # with open('27区自己号书签.txt', 'r') as f:
    #     url_list = f.readlines()
    url = 'http://sh.caihonger.com/login.php'
    zi_dong_deng_lu(url, list_A, list_P)

    # fun(url_list)