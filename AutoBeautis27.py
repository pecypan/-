from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime


index_return = 0
def ben_zhai_shi_bin(base_):
    base_.click_word('招兵')
    page_source = str(base_.driver.page_source)
    pattern2 = r'短刀手</a>:(\d+)'
    match2 = re.search(pattern2, page_source)
    if match2:
        numbers2 = int(match2.group(1))
        if numbers2 > 6000:
            base_.click_word('首页')
            base_.click_word('地图')
            base_.location_x(40982)
            base_.click_word('喝了几杯')
            base_.click_word('出兵')
            try:
                base_.click_button('全', '短刀手', 6000)
            except:
                logger.info('have no duandaoshou')
            base_.click_button('出征')
            base_.click_button('普通出征')
        elif numbers2 == 0:
            base_.click_word('招兵')
            base_.click_word('(普攻)短刀手')
            base_.driver.find_element(By.XPATH, '//input[@name="s_num"]').send_keys(1)
            base_.click_button('确定')
            base_.click_word('首页')
        else:
            base_.click_word('首页')
    else:
        logger.info('匹配失败,请检查!')

def qiang_duo_beauty(base_, name, location_x):
    base_.click_word('地图')
    base_.location_x(location_x)
    base_.click_word(name)
    base_.driver.find_element(By.XPATH, "//a[starts-with(@href,'mapgetonemap.php?t')]").click()
    delay()
    base_.click_word('出兵')
    try:
        base_.click_button('全', '短刀手')
    except:
        logger.info('have no duandaoshou')
    base_.click_button('出征')
    time_str = base_.get_page_time()
    delay_time = del_path_time(time_str)
    base_.click_button('普通出征')
    return delay_time

def wan_shan_beauty(base_):
    global index_return
    index_return = 0
    base_.click_word('建筑')
    base_.click_word('后厢房')
    index = base_.is_text_exit('夹心')
    if index == 1:
        base_.click_word('夹心')
        index_ = base_.is_text_exit('1200/1200')
        if index_ == 1:
            logger.info('属性已经满级，不能再教导')
            base_.click_word('首页')
            index_return = 1
            return
        base_.click_word('教导', 4)
        a = base_.find_times('1键')
        print(a)
        if a == 3:
            base_.click_word('1键', 2)
            base_.click_word('1键', 1)
            base_.click_word('1键')
        elif a == 2:
            base_.click_word('1键', 1)
            base_.click_word('1键')
        else:
            base_.click_word('1键')
        index_3 = base_.is_text_exit('属性已经满级，不能再教导')
        if index_3 == 1:
            logger.info('属性已经满级，不能再教导')
            base_.click_word('首页')
            index_return = 1
            return
        else:
            logger.info('属性没满')
            base_.click_word('首页')
            return
    else:
        base_.click_word('首页')
        base_.driver.refresh()
        delay(5)
        wan_shan_beauty(base_)
# def wan_shan_beauty(base_):
#     base_.click_word('建筑')
#     base_.click_word('后厢房')
#     index = base_.is_text_exit('夹心')
#     if index == 1:
#         base_.click_word('夹心')
#         index_ = base_.is_text_exit('1200/1200')
#         if index_ == 1:
#             logger.info('属性已经满级，不能再教导')
#             base_.click_word('首页')
#             return 1
#         base_.click_word('教导', 4)
#         a = base_.find_times('1键')
#         print(a)
#         if a == 3:
#             base_.click_word('1键', 2)
#             base_.click_word('1键', 1)
#             base_.click_word('1键')
#         elif a == 2:
#             base_.click_word('1键', 1)
#             base_.click_word('1键')
#         else:
#             base_.click_word('1键')
#         index_3 = base_.is_text_exit('属性已经满级，不能再教导')
#         if index_3 == 1:
#             logger.info('属性已经满级，不能再教导')
#             base_.click_word('首页')
#             return 1
#             print(1)
#         else:
#             logger.info('属性没满')
#             base_.click_word('首页')
#             return 0
#             print(1)
#     else:
#         base_.click_word('首页')
#         base_.driver.refresh()
#         delay(5)
#         wan_shan_beauty(base_)

def zi_dong_deng_lu(url_, list_a, list_p):
    global location
    global name_1
    location = 40895
    name_1 = '成觉名'
    name_2 = '尉迟爽本'
    base = Base()
    base.config(1)
    base.driver.get(url_)
    delay()
    # 登录
    for i in range(92, 299):
        logger.info(f'账号：{list_a[i]}__密码：{list_p[i]}')
        base.input_acc_pass(list_a[i], list_p[i])
        base.click_button('确定')
        # 选择区服
        base.select_sh(5)
        i2 = 0
        city_list = base.locate_a('all')
        for city in city_list:
            if city == name_2:
                break
            else:
                if i2 == 10:
                    i2 = 0
                    break
                else:
                    i2 = i2 + 1
        logger.info(i2)
        delay()
        j = i2
        for index in range(j, 11):
            base.click_word(city_list[index])
            location_x,y = base.location_mine()
            index_2 = abs(location - location_x)
            if index_2 >= 3:
                continue
            # ben_zhai_shi_bin(base)
            base.click_word('武将')
            base.click_word('选将')
            base.click_word('升级')
            base.click_word('速建')
            base.click_word('返回')
            base.click_word('招募')
            base.click_word('返回')
            base.click_word('选将')
            base.click_word('招募')
            base.click_word('返回')
            base.click_word('招募')
            base.click_word('首页')
            ben_zhai_shi_bin(base)
            time_delay = qiang_duo_beauty(base, name_1, location)
            time_delay = time_delay - 20
            time_after(time_delay)
            if index == 0:
                base.click_word('系统')
                base.click_word('重新登录')
                base.input_acc_pass(list_a[i-1], list_p[i-1])
                base.click_button('确定')
                # 选择区服
                base.select_sh(5)
                city_list2 = base.locate_a('all')
                base.click_word(city_list2[10])
                ben_zhai_shi_bin(base)
                base.click_word('系统')
                base.click_word('重新登录')
                base.input_acc_pass(list_a[i], list_p[i])
                base.click_button('确定')
                # 选择区服
                base.select_sh(5)
                base.click_word(city_list[0])
            else:
                base.click_word('系统')
                base.click_word('切换')
                base.click_word(city_list[index - 1])
                ben_zhai_shi_bin(base)
                base.click_word('首页')
                base.click_word('系统')
                base.click_word('切换')
                base.click_word(city_list[index])
            wan_shan_beauty(base)
            print(index_return)
            if index_return == 1:
                logger.info('完成！')
                base.driver.close()
                base.driver.get('www.baidu.com')
                base.driver.quit()
                return
            elif index_return == 0:
                name_1 = city_list[index]
                location = location_x
                logger.info('继续！')
                base.click_word('首页')
                base.click_word('系统')
                base.click_word('切换')
        base.click_word('重新登录')


if __name__ == '__main__':
    # if os.path.exists(r'E:\红颜水浒2\location.txt'):
    #     os.remove(r'E:\红颜水浒2\location.txt')
    list_AandP = read_csv2list()
    list_A = []
    list_P = []
    for i in range(0, 300):
        list_A.append(list_AandP[i][0])
        list_P.append(list_AandP[i][1])
    url = 'http://sh.caihonger.com/login.php'
    zi_dong_deng_lu(url, list_A, list_P)
