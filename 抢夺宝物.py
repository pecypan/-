from BasePartDLL import *
from mettingBeauty import *
import datetime


removestr = 'master.php?t'
tasklist = ['tasks/selectBaowu.php?level=5&t','tasks/dailyReward.php?a=9165&t','tasks/randomReward.php?a=7484&t','']

def qiang_duo_bao_wu(url_list):
    base = Base()
    base.config(1)
    times = 10
    for j in range(10):
        metting_city = ['汜轻尘']
        for i in range(len(url_list)):
            print(f'--------------------当前是第{i+1}个号------------------')
            base.driver.get(url_list[i])
            delay()
            main_city = base.get_maincity_name()
            numbers = base.city_number()
            url = base.urltostr(url_list[i])
            url = url.replace(removestr, tasklist[0])
            url = list(url)
            for i in range(numbers):
                url[len(url)-1] = i
                url_need = ''.join(str(x) for x in url)
                base.driver.get(url_need)
                delay(0.3)
                base.lian_bin_jiang()
                base.cq()

                if times == 1:
                    logger.info('times = 1')
                    try:
                        base.click_button('10次')
                    except:
                        base.click_word('首页')
                        logger.info('ToDay have been battled!')
                elif times == 10:
                    logger.info('times = 10')
                    base.click_button('1次')
                    logger.info('1')
                else:
                    logger.info('Error times, pls check!')
            if main_city in metting_city:
                metting(base)
        # time_after(0)
    base.driver.quit()


if __name__ == '__main__':
    urlList = [ 
            'http://sh27.caihonger.com/master.php?t=4700&t=72005776136166818801&u'
                '=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=18359&c=0',               # 龙怀歌
            'http://sh27.caihonger.com/master.php?t=9236&t=72005776136166818801&u'
                '=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=18243&c=0',               # 韩
            'http://sh27.caihonger.com/master.php?t=2490&t=1644045681&u'
                '=VW1nS1pGRTlWVFpUUFFCcFhHUUZZQU0z&k=8&c=0',                                # 汝修君
            'http://sh27.caihonger.com/master.php?t=30464090271541595146&u'
                '=VVJ0ZlFGVkdVVEVIWlE5bUFEMVNPUWc0VmpRQ2F3STRCakJUWWc9PQ_c_c&k=702&c=0',    # 长孙
            'http://sh21.caihonger.com/master.php?t=2215&t=49298097774437635259&u'
                '=RHpBSVpsOHpWREphTzE0MFdtUUhZRkpoQW1vRWJBPT0_c&k=63400&c=0',               # 小天使11
            'http://sh27.caihonger.com/master.php?t=9714&t=72005776136166818801&u'
                '=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=19818&c=0',               # 一二三
            'http://sh27.caihonger.com/master.php?t=6092&t=1656428277&u'
                '=QnpnQWFGYytEbW9GWlYwMUFERlROUU05QzI5Uk0xWW5VU2s9&k=442&c=0',              # 茶凉
            'http://sh27.caihonger.com/master.php?t=2404&t=81466666722801424776&u'
                '=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92041&c=0',               # 愚人众
            'http://sh27.caihonger.com/master.php?t=7531&t=81466666722801424776&u'
                '=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92036&c=0',               # 界徐盛


           ]
    qiang_duo_bao_wu(urlList)



   
