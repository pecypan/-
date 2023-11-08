from BasePartDLL import *
import datetime


def lue_duo_zi_yuan(url_):
    base = Base()
    for url in url_:
        base.driver.get(url_)
        # base.driver.implicitly_wait(15)
        delay(0.5)
        time_list = []
        delay_time = 0

        base.click_word('地图')
        base.click_word('一二三四|男')
        base.click_word('待到繁花落尽')
        base.click_word('出兵')
        try:
            base.click_button('全', '游骑兵')
            base.select_mode_of_battle('劫掠')
            base.click_button('出征')
            marching_time = base.get_page_time()
            path_time = del_path_time(marching_time) * 2
            time_list.append(path_time)
            base.click_button('普通出征')
        except:
            logger.error('出兵失败！')
        base.click_word('资源')
        base.click_word('一键建造资源')
        base.click_word('首页')
        logger.info('city 1 pass, continue')

        base.click_word('蜀郡张松')
        base.click_word('⑧')
        base.click_word('地图')
        base.click_word('梁礼邈|男')
        base.click_word('新的山寨')
        base.click_word('出兵')
        try:
            base.click_button('全', '游骑兵')
            base.select_mode_of_battle('劫掠')
            base.click_button('出征')
            marching_time = base.get_page_time()
            path_time = del_path_time(marching_time) * 2
            time_list.append(path_time)
            base.click_button('普通出征')
        except:
            logger.error('出兵失败！')
        base.click_word('资源')
        base.click_word('一键建造资源')
        base.click_word('首页')
        logger.info('city 2 pass, continue')

        base.click_word('蜀郡张松')
        base.click_word('⑨')
        base.click_word('地图')
        base.click_word('辛利扬|男')
        base.click_word('新的山寨')
        base.click_word('出兵')
        try:
            base.click_button('全', '游骑兵')
            base.select_mode_of_battle('劫掠')
            base.click_button('出征')
            marching_time = base.get_page_time()
            path_time = del_path_time(marching_time) * 2
            time_list.append(path_time)
            base.click_button('普通出征')
        except:
            logger.error('出兵失败！')
        base.click_word('资源')
        base.click_word('一键建造资源')
        base.click_word('首页')
        logger.info('city 3 pass, continue')

        base.click_word('蜀郡张松')
        base.click_word('⑩')
        base.click_word('地图')
        base.click_word('麹自彤|男')
        base.click_word('新的山寨')
        base.click_word('出兵')
        try:
            base.click_button('全', '游骑兵')
            base.select_mode_of_battle('劫掠')
            base.click_button('出征')
            marching_time = base.get_page_time()
            path_time = del_path_time(marching_time) * 2
            time_list.append(path_time)
            base.click_button('普通出征')
        except:
            logger.error('出兵失败！')
        base.click_word('资源')
        base.click_word('一键建造资源')
        base.click_word('首页')
        logger.info('city 4 pass, continue')

        base.click_word('蜀郡张松')
        base.click_word('④')
        base.click_word('地图')
        base.click_word('寂寞')
        # base.click_word('新的山寨')
        base.click_word('出兵')
        try:
            base.click_button('全', '游骑兵')
            base.select_mode_of_battle('劫掠')
            base.click_button('出征')
            marching_time = base.get_page_time()
            path_time = del_path_time(marching_time) * 2
            time_list.append(path_time)
            base.click_button('普通出征')
        except:
            logger.error('出兵失败！')
        base.click_word('资源')
        base.click_word('一键建造资源')
        logger.info('city 5 pass, continue')

        if len(time_list) <= 0:
            logger.error('time_list is an empty sequence')
        else:
            delay_time = max(time_list)
            logger.info(f'max_delay_time: {delay_time}s', delay_time)
    base.driver.quit()
    return delay_time


if __name__ == '__main__':
    url = 
    while True:
        StartTime = datetime.datetime.now()
        DelayTime = lue_duo_zi_yuan(url)
        EndTime = datetime.datetime.now()
        NeedTime_ = str(EndTime - StartTime)
        NeedTime = del_path_time(NeedTime_)
        logger.info(f'Need Time: {NeedTime}s', NeedTime)
        NeedDelayTime = DelayTime - 15
        if NeedDelayTime > 0:
            time_after(NeedDelayTime)
        else:
            continue
