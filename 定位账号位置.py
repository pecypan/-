from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime

Location = 40780  # 252start
location_list = []


def zi_dong_deng_lu(url_, list_a, list_p):
    global Location
    global location_list
    # time_ = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    location_list.append(Location)
    with open('location.txt', 'w') as f:
        f.writelines(str(location_list))
        f.close()
    base = Base()
    base.driver.get(url_)
    delay()
    # 登录
    for i in range(220, 300):
        base.input_acc_pass(list_a[i], list_p[i])
        base.click_button('确定')
        # 选择区服
        base.select_sh(5)
        city_list = base.locate_a('all')
        delay()
        for index in range(0, 1):
            base.click_word(city_list[index])
            mine_location = base.location_mine()
            logger.info(f'账号：{list_a[i]}__密码：{list_p[i]}')
            logger.info(f'本机坐标：{mine_location}')
            with open('账号位置.txt', 'a') as f:
                f.write(list_a[i] + '==>>')
                f.write(str(mine_location) + '\n')
                f.close()
            base.click_word('系统')
            base.click_word('重新登录')




        # jun_gong(base, Location_x, Location)


if __name__ == '__main__':
    if os.path.exists(r'F:\红颜水浒2\location.txt'):
        os.remove(r'F:\红颜水浒2\location.txt')
    list_AandP = read_csv2list()
    list_A = []
    list_P = []
    for i in range(0, 300):
        list_A.append(list_AandP[i][0])
        list_P.append(list_AandP[i][1])
    url = 'http://sh.caihonger.com/login.php'
    # for i in range(252, 300):
    #     logger.info(f'--------{i}--------')
    #     list_a = list_A[i]
    #     list_p = list_P[i]
    zi_dong_deng_lu(url, list_A, list_P)
