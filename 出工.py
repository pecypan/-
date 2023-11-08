from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime

# Location = 3392 # 252start
# Location = 40744 #裤裆
# Location = 40979
# Location = 42079 #渣风

# locationF = '&x=12545&y=1'
locationF = '&x=41104&y=3'
removestr = 'master.php?a'
tasklist = ['tasks/selectBaowu.php?level=5&t','tasks/dailyReward.php?a=9165&t','tasks/randomReward.php?a=7484&t','building/dianjiangtai.php?a=2218&t','combat/dispatch.php?t']

def zi_dong_deng_lu(url_, list_a, list_p):
    global Location
    base = Base()
    base.config(1)
    base.driver.get(url_)
    delay()
    # 登录
    for i in range(241, 250):
        global num
        num = 0
        print(f'----------------------账号：{list_a[i]}__密码：{list_p[i]}--------------------------------')
        base.input_acc_pass(list_a[i], list_p[i])
        base.click_button('确定')
        # 选择区服
        base.select_sh(4)
        current_url = base.driver.current_url
        city_list = base.locate_a('all')
        delay()
        for index in range(11):
            base.click_word(city_list[index])
            mainurl = base.driver.current_url
            number = base.shi_bin_num()
            if number < 10000:
                base.driver.back()
            else:
                number = number - 1
                number2 = base.resource_num('粮')
                if number2 <= 0:
                    url2 = mainurl.replace(removestr, tasklist[1])
                    base.driver.get(url2)
                    delay(0.3)
                    base.click_word('首页')
                mine_location, y = base.location_mine()
                print(f'本机坐标：{mine_location}/{y}')
                if mine_location < 40740 or mine_location > 42000:
                    base.driver.get(current_url)
                else:
                    url3 = mainurl.replace(removestr, tasklist[3])
                    base.driver.get(url3)
                    delay(0.3)
                    base.click_word('招募')
                    url4 = mainurl.replace(removestr, tasklist[4])
                    url4 = url4 + locationF
                    base.driver.get(url4)
                    delay(0.3)
                    try:
                        try:
                            base.click_button('全', '弓箭手')
                        except:
                            pass
                        try:
                            base.click_button('全', '短刀手')
                        except:
                            pass
                        base.select_mode_of_battle('歼灭')
                        base.click_button('出征')
                        base.click_button('普通出征')
                        index = base.is_text_exit('出兵限制说明')
                        if index == 0:
                            num = num + 1
                            if num >= 200:
                                base.driver.close()
                                break
                                return
                            else:
                                base.driver.get(current_url)
                        else:
                            print('出兵被限制')
                            base.driver.get(current_url)
                    except:
                        base.driver.get(current_url)
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
