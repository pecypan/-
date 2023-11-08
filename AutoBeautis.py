from BasePartDLL import *

target_name = '戴和斌'
target_location = 22931
name_ = ''


def zhao_xia_ge_target(base_, location_x, index, acc_dict_):
    is_city = base_.is_text_exit('寨主名')
    if is_city == 1:
        name = base_.driver.find_element(By.XPATH, "//a[starts-with(@href,'getuserinfo.php?')]").text
        if name in acc_dict_:
            return name
        else:
            logger.info(f'{name}——不属于小号书签范围')
            base_.driver.back()
            return 0
    else:
        logger.info(f'{target_location}/{index}不是城市')
        base_.driver.back()
        return 0


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


def ben_zhai_shi_bin(base_, location_x):
    base_.click_word('招兵')
    a = base_.is_text_exit('工匠手:0')
    if a == 0:
        page_source = str(base_.driver.page_source)
        pattern1 = r'工匠手</a>:(\d+)'
        pattern2 = r'短刀手</a>:(\d+)'
        pattern3 = r'弓箭手</a>:(\d+)'
        match1 = re.search(pattern1, page_source)
        match2 = re.search(pattern2, page_source)
        match3 = re.search(pattern3, page_source)
        if match1:
            numbers = int(match1.group(1))
            logger.info(f'本寨有建手: {numbers}')
            if numbers == 0:
                if match2 and match3:
                    numbers2 = int(match2.group(1))
                    numbers3 = int(match3.group(1))
                    if numbers2 >= 1 or numbers3 >= 1:
                        base_.click_word('首页')
                        base_.click_word('地图')
                        base_.location_x(22905)
                        base_.click_word('贫石县')
                        base_.click_word('出兵')
                        try:
                            base_.click_button('全', '短刀手')
                        except:
                            logger.info('have no duandaoshou')
                        try:
                            base_.click_button('全', '弓箭手')
                        except:
                            logger.info('have no gongjianshou')
                        base_.click_button('出征')
                        base_.click_button('普通出征')
                        base_.click_word('招兵')
                        base_.click_word('(普攻)短刀手')
                        base_.driver.find_element(By.XPATH, '//input[@name="s_num"]').send_keys(1)
                        base_.click_button('确定')
                        base_.click_word('首页')
                        delay(9)
                    else:
                        base_.click_word('(普攻)短刀手')
                        base_.driver.find_element(By.XPATH, '//input[@name="s_num"]').send_keys(1)
                        base_.click_button('确定')
                        base_.click_word('首页')
                        delay(9)
                else:
                    logger.error('ERROR, pls check, match1')

            else:
                base_.click_word('首页')
                base_.click_word('地图')
                base_.location_x(location_x)
                base_.click_word('新的山寨')
                base_.click_word('出兵')
                base_.select_mode_of_battle('增援')
                try:
                    base_.click_button('全', '工匠手')
                except:
                    logger.info('have no gongjiangshou')
                base_.click_button('出征')
                base_.click_button('普通出征')

                if match2 and match3:
                    numbers2 = int(match2.group(1))
                    numbers3 = int(match3.group(1))
                    if numbers2 >= 1 or numbers3 >= 1:
                        base_.click_word('地图')
                        base_.location_x(22905)
                        base_.click_word('贫石县')
                        base_.click_word('出兵')
                        try:
                            base_.click_button('全', '短刀手')
                        except:
                            logger.info('have no duandaoshou')
                        try:
                            base_.click_button('全', '弓箭手')
                        except:
                            logger.info('have no gongjianshou')
                        base_.click_button('出征')
                        base_.click_button('普通出征')
                        base_.click_word('招兵')
                        base_.click_word('(普攻)短刀手')
                        base_.driver.find_element(By.XPATH, '//input[@name="s_num"]').send_keys(1)
                        base_.click_button('确定')
                        base_.click_word('首页')
                        delay(9)
                    else:
                        base_.click_word('招兵')
                        base_.click_word('(普攻)短刀手')
                        base_.driver.find_element(By.XPATH, '//input[@name="s_num"]').send_keys(1)
                        base_.click_button('确定')
                        base_.click_word('首页')
                        delay(9)
                else:
                    logger.error('ERROR, pls check, match1')
        else:
            logger.error('ERROR, pls check, match1')
    else:
        page_source = str(base_.driver.page_source)
        pattern2 = r'短刀手</a>:(\d+)'
        pattern3 = r'弓箭手</a>:(\d+)'
        match2 = re.search(pattern2, page_source)
        match3 = re.search(pattern3, page_source)
        if match2 and match3:
            numbers2 = int(match2.group(1))
            numbers3 = int(match3.group(1))
            if numbers2 >= 1 or numbers3 >= 1:
                base_.click_word('首页')
                base_.click_word('地图')
                base_.location_x(22905)
                base_.click_word('贫石县')
                base_.click_word('出兵')
                try:
                    base_.click_button('全', '短刀手')
                except:
                    logger.info('have no duandaoshou')
                try:
                    base_.click_button('全', '弓箭手')
                except:
                    logger.info('have no gongjianshou')
                base_.click_button('出征')
                base_.click_button('普通出征')
                base_.click_word('招兵')
                base_.click_word('(普攻)短刀手')
                base_.driver.find_element(By.XPATH, '//input[@name="s_num"]').send_keys(1)
                base_.click_button('确定')
                base_.click_word('首页')
                delay(9)
            else:
                base_.click_word('(普攻)短刀手')
                base_.driver.find_element(By.XPATH, '//input[@name="s_num"]').send_keys(1)
                base_.click_button('确定')
                base_.click_word('首页')
                delay(9)
        else:
            logger.error('ERROR, pls check, match2 or match3')


def shen_dian_jiang_tai(base_):
    base_.click_word('建筑')
    level_dianjiangtai = base_.jian_zhu_level('点将台')
    if level_dianjiangtai < 3:
        base_.click_word('首页')
        base_.click_word('宝箱')
        base_.click_word('资源')
        base_.click_word('资源箱')
        base_.click_word('使用')
        base_.click_word('单个')
        base_.click_word('首页')
        base_.click_word('建筑')
        base_.locate_a('0', 'dianjiangtai.php?')
        base_.click_word('升级')
        base_.click_word('速建')
        base_.click_word('返回')
        base_.click_word('升级')
        base_.click_word('速建')
        base_.click_word('返回')
        base_.click_word('选将')
        base_.click_word('招募')
        base_.click_word('返回')
        base_.click_word('招募')
        base_.click_word('返回')
        base_.click_word('招募')
        base_.click_word('首页')
    else:
        base_.locate_a('0', 'dianjiangtai.php?')
        base_.click_word('选将')
        base_.click_word('招募')
        base_.click_word('返回')
        base_.click_word('招募')
        base_.click_word('返回')
        base_.click_word('招募')
        base_.click_word('首页')


def kai_he_zi(base_):
    base_.click_word('宝箱')
    base_.click_word('美女')
    a = base_.is_text_exit('烈女传全卷')
    if a == 1:
        base_.click_word('功能')
        index = base_.is_text_exit('神秘礼物')
        if index == 0:
            base_.click_word('后页')
            index = base_.is_text_exit('神秘礼物')
            if index == 0:
                base_.click_word('首页')
                return 1
            else:
                base_.click_word('神秘礼物')
                base_.click_word('使用')
                base_.click_word('全部使用')
                base_.click_word('返回')
                base_.click_word('功能')
                base_.click_word('后页')
                base_.click_word('梳妆盒')
                base_.click_word('使用')
                base_.click_word('全部使用')
                base_.click_word('首页')
                return 1
        else:
            base_.click_word('神秘礼物')
            base_.click_word('使用')
            base_.click_word('全部使用')
            base_.click_word('返回')
            base_.click_word('功能')
            base_.click_word('梳妆盒')
            base_.click_word('使用')
            base_.click_word('全部使用')
            base_.click_word('首页')
            return 1
    else:
        base_.click_word('首页')
        return 0


def fang_zhu(base_):
    base_.click_word('建筑')
    base_.click_word('后厢房')
    base_.click_word('小薇')
    base_.click_word('放逐')
    base_.click_word('放逐')
    base_.click_word('立刻放逐')
    base_.click_word('首页')


def wan_shan_beauty(base_):
    base_.click_word('建筑')
    base_.click_word('后厢房')
    index = base_.is_text_exit('夹心')
    if index == 1:
        base_.click_word('夹心')
        base_.click_word('教导', 4)
        a = base_.is_text_exit('烈女传残卷0个')
        if a == 0:
            b = base_.is_text_exit('烈女传秘录0个')
            if b == 0:
                base_.click_word('1键', 2)
            else:
                logger.info('没有秘录')
            c = base_.is_text_exit('烈女传秘录0个')
            if c == 0:
                base_.click_word('1键', 2)
            else:
                logger.info('没有秘录')
            base_.click_word('1键', 1)
            d = base_.is_text_exit('烈女传全卷0个')
            if d == 0:
                base_.click_word('1键', 1)
            else:
                base_.click_word('1键')
            index_ = base_.is_text_exit('1200/1200')
            if index_ == 1:
                logger.info('属性已经满级，不能再教导')
                base_.click_word('首页')
                return 1
            else:
                base_.click_word('首页')
                return 0
        else:
            b = base_.is_text_exit('烈女传秘录0个')
            if b == 0:
                base_.click_word('1键', 1)
            else:
                logger.info('没有秘录')
            c = base_.is_text_exit('烈女传秘录0个')
            if c == 0:
                base_.click_word('1键', 1)
            else:
                logger.info('没有秘录')
            base_.click_word('1键')
            d = base_.is_text_exit('烈女传全卷0个')
            if d == 0:
                base_.click_word('1键')
            else:
                logger.info('没有道具')
            index_ = base_.is_text_exit('属性已经满级，不能再教导')
            if index_ == 1:
                logger.info('属性已经满级，不能再教导')
                base_.click_word('首页')
                return 1
            else:
                base_.click_word('首页')
                return 0
    else:
        base_.click_word('首页')
        base_.driver.refresh()
        delay(5)
        wan_shan_beauty(base_)


def main_fuction(base, name, book_mark_list, acc_dict):
    global target_name
    global target_location
    global name_
    while name_ != '结束':
        book_mark = acc_dict[name]
        base.driver.get(book_mark_list[book_mark - 1])
        delay()
        base.click_word(name)
        index = kai_he_zi(base)
        if index == 1:
            shen_dian_jiang_tai(base)
            ben_zhai_shi_bin(base, target_location - 1)
            fang_zhu(base)
            delay_time = qiang_duo_beauty(base, target_name, target_location)
            time_after(delay_time)
            if_ok = wan_shan_beauty(base)
            logger.info(if_ok)
            if if_ok == 1:
                logger.info('当前妞造完毕')
                target_name = base.get_maincity_name()
                logger.info(f'当前寨主{target_name}')
                name_ = '结束'
                return
            else:
                target_location, location_y = base.location_mine()
                target_name = base.get_maincity_name()
                base.click_word('地图')
                base.location_x(target_location)

                if location_y == 9:
                    base.click_word('后页')
                    location_x = target_location + 1
                    for i in range(0, 10):
                        location1 = '&x=' + str(location_x) + '&y=' + str(i)
                        base.select_city(location_x, location1)
                        name_ = zhao_xia_ge_target(base, location_x, i, acc_dict)
                        if name_ != 0:
                            break
                        else:
                            logger.info(f'{location_x}/{i}不是目标')
                            if i == 9:
                                logger.info('检查一下把，本页没找到符合要求的寨主')
                                return
                            else:
                                logger.info('继续下个坐标')
                else:
                    location_y = location_y + 1
                    logger.info(f'location_y = {location_y}')
                    for i in range(location_y, 10):
                        logger.info(f'i = {i}')
                        location1 = '&x=' + str(target_location) + '&y=' + str(i)
                        base.select_city(target_location, location1)
                        name_ = zhao_xia_ge_target(base, target_location, i, acc_dict)
                        if name_ != 0:
                            break
                        else:
                            logger.info(f'{target_location}/{i}不是目标')
                            if i == 9:
                                logger.info('前往下一页')
                                location_x = target_location + 1
                                for j in range(0, 10):
                                    location1 = '&x=' + str(location_x) + '&y=' + str(j)
                                    base.select_city(location_x, location1)
                                    name_ = zhao_xia_ge_target(base, location_x, j, acc_dict)
                                    if name_ != 0:
                                        break
                                    else:
                                        logger.info(f'{location_x}/{j}不是目标')
                                        if j == 9:
                                            logger.info('检查一下把，本页没找到符合要求的寨主')
                                            return
                                        else:
                                            logger.info('继续下个坐标')
                            else:
                                logger.info('继续下个坐标')
                main_fuction(base, name_, book_mark_list, acc_dict)
        else:
            loaction_x, location_y = base.location_mine()
            my_name = base.get_maincity_name()

            base.click_word('地图')
            base.location_x(loaction_x)
            if location_y == 9:
                base.click_word('后页')
                loaction_x = loaction_x + 1
                for i in range(0, 10):
                    location1 = '&x=' + str(loaction_x) + '&y=' + str(i)
                    base.select_city(loaction_x, location1)
                    name_ = zhao_xia_ge_target(base, loaction_x, i, acc_dict)
                    if name_ != 0:
                        break
                    else:
                        logger.info(f'{loaction_x}/{i}不是目标')
                        if i == 9:
                            logger.info('检查一下把，本页没找到符合要求的寨主')
                            return
                        else:
                            logger.info('继续下个坐标')
            else:
                logger.info(f'location_y = {location_y}')
                for i in range(location_y + 1, 10):
                    logger.info(f'i = {i}')
                    location1 = '&x=' + str(loaction_x) + '&y=' + str(i)
                    base.select_city(loaction_x, location1)
                    name_ = zhao_xia_ge_target(base, loaction_x, i, acc_dict)
                    if name_ != 0:
                        break
                    else:
                        logger.info(f'{loaction_x}/{i}不是目标')
                        if i == 9:
                            logger.info('前往下一页')
                            loaction_x = loaction_x + 1
                            for j in range(0, 10):
                                location1 = '&x=' + str(loaction_x) + '&y=' + str(j)
                                base.select_city(loaction_x, location1)
                                name_ = zhao_xia_ge_target(base, loaction_x, j, acc_dict)
                                if name_ != 0:
                                    break
                                else:
                                    logger.info(f'{loaction_x}/{j}不是目标')
                                    if j == 9:
                                        logger.info('检查一下把，本页没找到符合要求的寨主')
                                        return
                                    else:
                                        logger.info('继续下个坐标')
                        else:
                            logger.info('继续下个坐标')
            main_fuction(base, name_, book_mark_list, acc_dict)
    base.driver.quit()
    return


if __name__ == '__main__':
    with open('0-小天使.txt', 'r+') as f:
        shuqian_list = f.readlines()
        f.close()

    # 将xlsx转字典
    path = '25账号位置.xlsx'
    start_row = 2  # 数据开始行数
    number_row = 4385  # 数据个数
    zhanghao_dict = {}
    look_up_table_excel = load_workbook(path)
    look_up_table_all_sheet = look_up_table_excel.get_sheet_names()
    look_up_table_sheet = look_up_table_excel.get_sheet_by_name(look_up_table_all_sheet[0])
    for i in range(start_row, start_row + number_row):
        number = look_up_table_sheet.cell(i, 1).value
        name = look_up_table_sheet.cell(i, 2).value
        zhanghao_dict[number] = name

    base_main = Base()

    # name = '戴和斌'
    # url_number = zhanghao_dict[name]
    # base_main.driver.get(shuqian_list[url_number - 1])
    # base_main.click_word(name)
    # location_x, location_y = base_main.location_mine()
    # ben_zhai_shi_bin(base_main, location_x)
    # kai_he_zi(base_main)
    # fang_zhu(base_main)
    # delay(100)

    city_name = '后汉高'
    main_fuction(base_main, city_name, shuqian_list, zhanghao_dict)
