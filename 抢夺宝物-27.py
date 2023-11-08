from BasePartDLL import *
from mettingBeauty import *
import datetime

removestr = 'master.php?t'
tasklist = ['tasks/selectBaowu.php?level=5&t','tasks/dailyReward.php?a=9165&t','tasks/randomReward.php?a=7484&t','']

def qiang_duo_bao_wu(url_list):
    base = Base()
    base.config(1)
    times = 1
    metting_city = ['']
    for i in range(len(url_list)):
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
            base.click_word('首页')
            metting(base)
    base.driver.quit()

if __name__ == '__main__':
    urlList = [
    'http://sh27.caihonger.com/master.php?t=3478&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=19572&c=0',# 1-爱甘雨 27
    'http://sh27.caihonger.com/master.php?t=2095&t=72005776136166818801&u=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=17980&c=0',# 2-生来一身傲骨 27
    'http://sh27.caihonger.com/master.php?t=9384&t=72005776136166818801&u=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=18210&c=0',# 3-岂可居于人下 27
    'http://sh27.caihonger.com/master.php?t=3886&t=30464090271541595146&u=VVJ0ZlFGVkdVVEVIWlE5bUFEMVNPUWc0VmpRQ2F3STRCakJUWWc9PQ_c_c&k=43&c=0',# 4-夏未尽♀花己落 27
    'http://sh27.caihonger.com/master.php?t=4252&t=1627094978&u=QTNjQk1sTjFCbVpVTmdoaEN6VUFZQUEvQm1jRVpnWXk_c&k=436&c=0',# 5-罗妞 27
    'http://sh27.caihonger.com/master.php?t=4963&t=78006833175635470737&u=QlZFUEkxVmdCR1JVTkF0Z0RUMVNORkprQldBS2FRRTBWbVVDT0FROQ_c_c&k=353&c=0',# 6-争锋 27
    'http://sh27.caihonger.com/master.php?t=4670&t=30464090271541595146&u=VVJ0ZlFGVkdVVEVIWlE5bUFEMVNPUWc0VmpRQ2F3STRCakJUWWc9PQ_c_c&k=19790&c=0',# 7-花有重开日 27
    'http://sh27.caihonger.com/master.php?t=64384226349493964270&u=QVc1ZE53UmpCV1ZhT2dsZ1dXZ0NZUWsyQzJnRlpRUSs_c&k=473&c=0',# 8-路过 27
    'http://sh27.caihonger.com/master.php?t=11355471497717507354&u=QkRzT1lnVnBBR2RWTkF4blhXVlhNUWMwVVRBRll3PT0_c&k=18409&c=0',# 9-北凉 27
    'http://sh27.caihonger.com/master.php?t=1618&t=72005776136166818801&u=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=17959&c=0',# 10-汜轻尘 27
    'http://sh27.caihonger.com/master.php?t=9850&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92039&c=0',# 11-神郭嘉 27
           ]
 
    qiang_duo_bao_wu(urlList)

   
