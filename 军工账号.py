from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime

Location = 41167# 252start
location_list = []
locationF = '&x=41167&y=1'
removestr = 'master.php?a'
tasklist = ['tasks/selectBaowu.php?level=5&t','tasks/dailyReward.php?a=9165&t','tasks/randomReward.php?a=7484&t','building/dianjiangtai.php?a=2218&t','combat/dispatch.php?t']

def zi_dong_deng_lu(url_, list_a, list_p):
    global locationF
    global Location
    global location_list

    location_list.append(Location)
    with open('location.txt', 'w') as f:
        f.writelines(str(location_list))
        f.close()
    base = Base()
    base.config(1)
    base.driver.get(url_)
    delay()
    # 登录
    for i in range(250, 299):
        logger.info(f'********************账号：=======================>{list_a[i]}__密码：{list_p[i]}<================================********************')
        base.input_acc_pass(list_a[i], list_p[i])
        base.click_button('确定')
        # 选择区服
        base.select_sh(4)
        mainurl1 = base.driver.current_url
        city_list = base.locate_a('all')
        delay()
        for index in range(0, 11):
            base.click_word(city_list[index])
            mainurl = base.driver.current_url
            numbers = base.shi_bin_num()
            if numbers <= 15000:
                base.driver.back()
                continue
            source = base.resource_num('粮')
            if source <= 0:
                url1 = mainurl.replace(removestr, tasklist[1])
                base.driver.get(url1)
                delay(0.3)
            url2 = mainurl.replace(removestr, tasklist[3])
            base.driver.get(url2)
            delay(0.3)
            base.click_word('招募')
            base.click_word('首页')
            mine_location, location_y = base.location_mine()
            logger.info(f'本机坐标：{mine_location}')
            if Location - 5 <= mine_location <= Location + 5:
                logger.info(f'目标坐标：{Location}')
                url2 = mainurl.replace(removestr, tasklist[4])
                url2 = url2 + locationF
                base.driver.get(url2)
                try:
                    base.click_button('全', '弓箭手')
                except:
                    pass
                try:
                    base.click_button('全', '短刀手')
                except:
                    pass
                base.select_mode_of_battle('增援')
                base.click_button('出征')
                try:
                    base.click_button('普通出征')
                except:
                    pass
                base.driver.get(mainurl1)
                delay(0.3)
            elif Location + 5 < mine_location <= Location + 11:
                time_ = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                location_list.append(time_)
                Location = Location + 11
                logger.info(f'===================={location_list}====================')
                index = index - 1
                location_list.append(Location)
                logger.info(index)
                with open('location.txt', 'w') as f:
                    f.writelines(str(location_list))
                    f.close()

                logger.info(f'目标坐标：{Location}')
                base.click_word('地图')
                base.location_x(Location)
                base.click_word('新的山寨')
                x, y = base.location_others()
                locationF = '&x=' + str(x) + '&y=' + str(y)
                print(locationF)
                url2 = mainurl.replace(removestr, tasklist[4])
                url2 = url2 + locationF
                base.driver.get(url2)
                # try:
                #     base.click_button('全', '弓箭手')
                # except:
                #     pass
                try:
                    base.click_button('全', '短刀手')
                except:
                    pass
                base.click_button('出征')
                base.click_button('普通出征')
                base.driver.get(mainurl1)
                delay(0.3)
            else:
                logger.info('不在范围内')
                base.driver.get(mainurl1)
                delay(0.3)
        base.click_word('重新登录')



if __name__ == '__main__':
    if os.path.exists(r'F:\红颜\location.txt'):
        os.remove(r'F:\红颜\location.txt')
        logger.info('del successful')
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
    # gai_ming(url, list_A, list_P)
