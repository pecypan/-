from BasePartDLL import *
import datetime

removestr = 'master.php?t'
tasklist = ['tasks/selectBaowu.php?level=5&t','tasks/dailyReward.php?a=9165&t','tasks/randomReward.php?a=7484&t','building/dianjiangtai.php?a=2218&t','combat/dispatch.php?t']


def tou_shi(url_, main_city_name, city_name_list, location):
    base = Base()
    base.config(1)
    base.driver.get(url_)
    delay()
    while True:
        for i in range(0, len(city_name_list)):
            base.click_word(main_city_name)
            base.click_word(city_name_list[i])
            mainurl = base.driver.current_url
            url2 = mainurl.replace(removestr, tasklist[4])
            url2 = url2 + location[0]
            base.driver.get(url2)
            delay(0.3)
            # gui_mo = base.city_gui_mo()
            # if gui_mo != 0:
            base.click_word('出兵')
            try:
                base.click_button('全', '连环马', '10000')
            except:
                logger.info('1 | 1')
            try:
                base.click_button('全', '轰天雷', '2000')
            except:
                logger.info('1 | 2')
            try:
                base.click_button('全', '撞城槌')
            except:
                logger.info('1 | 3')
            try:
                base.click_button('全', '游骑兵', '400')
            except:
                logger.info('1 | 4')
            base.click_button('出征')
            try:
                base.click_button('普通出征')
                map_exit = base.locate_a('LINK_TEXT', '地图')
                if map_exit == 0:
                    logger.info('出征失败！')
                    base.click_word('首页')
                logger.debug(f'----------第{i + 1}目标行军：1----------')
            except:
                logger.info('士兵或武将有误！')
                base.click_word('首页')
                continue
            # else:
            #     logger.info(f'目标{i + 1}规模已为0')
            #     base.click_word('首页')
            #     continue
            for x in range(0, 28):
                base.driver.back()
                base.driver.back()
                base.driver.refresh()
                try:
                    base.click_button('全', '轰天雷', '2000')
                except:
                    logger.info(f'{x} | 1')
                try:
                    base.click_button('全', '连环马', '10000')
                except:
                    logger.info(f'{x} | 2')
                try:
                    base.click_button('全', '游骑兵', '400')
                except:
                    logger.info('1 | 2')
                base.click_button('出征')
                try:
                    base.click_button('普通出征')
                    map_exit = base.locate_a('LINK_TEXT', '地图')
                    if map_exit == 0:
                        logger.info('出征失败！')
                        base.click_word('首页')
                        break
                    logger.debug(f'----------第{i + 1}目标行军：{x + 2}----------')
                except:
                    logger.info('没有武将或没有士兵！')
                    base.click_word('首页')
                    break
    base.driver.quit()


if __name__ == '__main__':
    # url = 'http://sh27.caihonger.com/master.php?t=13437594576846656625&u=QUQ4QmJ3SnVVVGRWTkE1a0NqUUhZQUV5Qm00Q2F3PT0_c&k=18210&c=3'
    # location = ['&x=39680&y=0']
    # mainCity = '岂可'
    # cityName = ['④','⑤','⑥','⑦','⑧','⑨','⑩','①①','①②','①③']

    # url = 'http://sh27.caihonger.com/master.php?t=11355471497717507354&u=QkRzT1lnVnBBR2RWTkF4blhXVlhNUWMwVVRBRll3PT0_c&k=18409&c=2'
    # location = ['&x=45625&y=5']
    # mainCity = '北凉'
    # cityName = ['白羽轻骑']

    # url = 'http://sh27.caihonger.com/master.php?a=3421&t=45737610323678038196&u=VkdzTFpRQnZVanRhTzFrL0NEQlJOUWMzVURGUU9BPT0_c&k=88259&c=0'
    # location = ['&x=45141&y=4']   
    # mainCity = '残城碎梦'
    # cityName = ['虚度年华时光']

    # url = 'http://sh21.caihonger.com/master.php?t=73357735097901042776&u=QVQ1YU5GVTVBbVJUTWdCcUN6VUhZQU13QjI4R2JnPT0_c&k=63400&c=2'
    # location = ['&x=45446&y=2']
    # mainCity = '日向小天使'
    # cityName = ['③'] 

    url = 'http://sh21.hongyanshuihu.com/master.php?a=3456&t=1577844003&u=QVd4YWRWQnNVM0ZTTkExaERUWT0_c&k=52&c=0'
    location = ['&x=11747&y=8']
    mainCity = '飞雨'
    cityName = ['勿扰']

    # url = 'http://sh27.caihonger.com/master.php?t=1644045681&u=VW1nS1pGRTlWVFpUUFFCcFhHUUZZQU0z&k=8&c=10'
    # location = ['&x=4290&y=4']
    # mainCity = '汝修君'
    # cityName = ['①①']

    # url = 'http://sh21.caihonger.com/master.php?a=9411&t=84015268046561712278&u=QVZVUFBGSjBBMk1BWUZveENEaFpQMVJpQVdRRFlGVmdWbVVIUFZCZw_c_c&k=72&c=12'
    # location = ['&x=850&y=6']
    # mainCity = '天地不仁'
    # cityName = ['平凡度日']

    tou_shi(url, mainCity, cityName, location)
