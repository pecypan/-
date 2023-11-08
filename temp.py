from BasePartDLL import *
from mettingBeauty import *
import datetime

removestr = 'master.php?t'
tasklist = ['tasks/selectBaowu.php?level=5&t','tasks/dailyReward.php?a=9165&t','tasks/randomReward.php?a=7484&t','']

def qiang_duo_bao_wu(url_list):
    base = Base()
    base.config(1)
    times = 1
    metting_city = ['汜轻尘']
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
                
           ]
 
    qiang_duo_bao_wu(urlList)

   
