from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime

# Location = 3392 # 252start
Location = 1604 #管夜山
# Location = 1978 #Tiam
# Location = 2116 #九门
# Location = 25 #熙
# Location = 10 #清风
location_list = []


def zi_dong_deng_lu(url_, list_a, list_p):
    global Location
    base = Base()
    base.config(1)
    base.driver.get(url_)
    delay()
    # 登录
    for i in range(70, 80):
        logger.info(f'账号：{list_a[i]}__密码：{list_p[i]}')
        base.input_acc_pass(list_a[i], list_p[i])
        base.click_button('确定')
        # 选择区服
        base.select_sh(6)
        # city_list = base.locate_a('all')
        # delay()
        # for index in range(0, 11):
            # base.click_word(city_list[index])
            # number = base.shi_bin_num()
            # if number < 30000:
            #     base.driver.back()
            # else:
            #     mine_location, y = base.location_mine()
            #     logger.info(f'本机坐标：{mine_location}/{y}')
            #     # if mine_location < 40740 or mine_location > 41240:
            #         # base.driver.back()
            #     # else:
            #     logger.info(f'目标坐标：{Location}')
            #     base.click_word('武将')
            #     wu_jiang_exit = base.is_text_exit('空闲')
            #     if wu_jiang_exit == 1:
            #         base.click_word('首页')
            #     else:
            #         base.click_word('选将')
            #         base.click_word('招募')
            #         base.click_word('首页')
            #     base.click_word('地图')
            #     base.location_x(Location)
            #     # delay()
            #     # base.locate_a('0', 'mapgetonemap.php?')
            #     base.click_word('灯依旧') #管夜山
            #     # base.click_word('花千') #Tiam
            #     # base.click_word('黄') #九门
            #     # base.click_word('白泽') #熙
            #     # base.click_word('天在') #清风
            #     base.click_word('出兵')
            #     try:
            #         base.click_button('全', '短刀手')
            #         base.select_mode_of_battle('歼灭')
            #         base.click_button('出征')
            #         try:
            #             base.click_button('普通出征')
            #             index = base.is_text_exit('美女')
            #             if index == 1:
            #                 base.click_word('系统')
            #                 base.click_word('切换好汉')
            #             else:
            #                 logger.info('出兵被限制')
            #                 base.driver.quit()
            #                 return
            #         except:
            #             logger.info('没有武将！')
            #             base.click_word('首页')
            #             base.click_word('系统')
            #             base.click_word('切换好汉')
            #     except:
            #         base.click_word('首页')
            #         base.click_word('系统')
            #         base.click_word('切换好汉')
            # base.driver.back()
        # base.driver.refresh()
        delay(1)
        base.click_word('重新登录')


if __name__ == '__main__':
    list_AandP = read_csv2list()
    list_A = []
    list_P = []
    for i in range(0, 300):
        list_A.append(list_AandP[i][0])
        list_P.append(list_AandP[i][1])
    url = 'http://sh.caihonger.com/login.php'
    zi_dong_deng_lu(url, list_A, list_P)
