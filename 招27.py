from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime

yijian = '&type=onekey'
removestr = 'master.php?a'
tasklist = ['resource/resourceautobuild.php?t','building/buildingautobuild.php?t','tasks/randomReward.php?a=7484&t','army/zhaobing.php?soldierType=infantry&', 'tasks/dailyReward.php?a=9165&t', 'tasks/randomReward.php?a=7484&t', 'army/zhaobing.php?soldierType=crossbow&']

def qian_dao(url_, list_a, list_p):
    base = Base()
    base.config(0)
    base.driver.get(url_)
    delay()
    # 登录
    for i in range(0, 50):
        logger.info(f'---------------账号：{list_a[i]}__密码：{list_p[i]}-----------------------')
        base.input_acc_pass(list_a[i], list_p[i])
        base.click_button('确定')
        # 选择区服
        base.select_sh(4)
        city_list = base.locate_a('all')
        url = base.driver.current_url
        delay()
        for index in city_list:
            base.click_word(index)
            url1 = base.driver.current_url
            url2 = url1.replace(removestr, tasklist[4])
            base.driver.get(url2)
            delay(0.3)
            url3 = url1.replace(removestr, tasklist[5])
            base.driver.get(url3)
            delay(0.3)
            base.driver.get(url)
            base.driver.back()
            base.driver.back()
            base.driver.back()
            base.driver.back()
        base.click_word('重新登录')
        logger.info(f'===********************{end}********************===')


def zi_dong_deng_lu(url_, list_a, list_p):
    base = Base()
    base.config(1)
    base.driver.get(url_)
    delay()
    # 登录
    for i in range(0, 299):
        logger.info(f'账号：{list_a[i]}__密码：{list_p[i]}')
        base.input_acc_pass(list_a[i], list_p[i])
        base.click_button('确定')
        # 选择区服
        base.select_sh(4)
        city_list = base.locate_a('all')
        url = base.driver.current_url
        delay()
        for index in range(0, 11):
            base.click_word(city_list[index])
            url1 = base.driver.current_url

            # url2 = url1.replace(removestr, tasklist[3]) # 短刀手
            url2 = url1.replace(removestr, tasklist[6]) # 弓箭手

            base.driver.get(url2)
            delay(0.35)

            base.click_word('最大招募')

            # base.driver.find_element(By.XPATH, "//input[@name='s_num']").send_keys(1)
            # base.click_button('确定')

            base.driver.get(url)
        base.click_word('重新登录')


if __name__ == '__main__':
    # if os.path.exists(r'E:\红颜水浒2\location.txt'):
    #     os.remove(r'E:\红颜水浒2\location.txt')
    list_AandP = read_csv2list()
    list_A = []
    list_P = []
    for i in range(0, 299):
        list_A.append(list_AandP[i][0])
        list_P.append(list_AandP[i][1])
    url = 'http://sh.caihonger.com/login.php'
    zi_dong_deng_lu(url, list_A, list_P)
    # qian_dao(url, list_A, list_P)
