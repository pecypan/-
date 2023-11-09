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
            metting(base)
    base.driver.quit()


if __name__ == '__main__':
    urlList = [
    'http://sh31.caihonger.com/master.php?t=30464090271541595146&u=QTBrQkhsRkNBV0ZYTlFCcFdtZFRPRkppQkdZR2J3ODFVbVJUWWc9PQ_c_c&k=158&c=0',    # 武大郎
    'http://sh21.caihonger.com/master.php?t=2142&t=85226957694941849938&u=QWxZS09WTjFCV1ZWTlFGcURqNEFaZ2svVVRSU01RUXhWMlJkWndZNw_c_c&k=8&c=0',# 风
    'http://sh21.caihonger.com/master.php?t=6469&t=78006833175635470737&u=VkFBSUpGQmxBMk1CWVZveFcydFlQbFJpQkdGUU13QTFWbVVGUHdROQ_c_c&k=1249&c=0',# 梦
    'http://sh21.caihonger.com/master.php?t=63298572785305090746&u=RHpBTmJsRTVBMlZRTXdGb0R6QlpPbFpwVXpRRFlnPT0_c&k=290188&c=0',# 1-尘心 21
    'http://sh21.caihonger.com/master.php?t=7259&t=49298097774437635259&u=RHpBSVpsOHpWREphTzE0MFdtUUhZRkpoQW1vRWJBPT0_c&k=291543&c=0',# 3-相见不如怀念 25
    'http://sh21.caihonger.com/master.php?t=5680&t=49298097774437635259&u=RHpBSVpsOHpWREphTzE0MFdtUUhZRkpoQW1vRWJBPT0_c&k=307721&c=0',# 4-日向小天使 25
    'http://sh21.caihonger.com/master.php?t=8611&t=95133861564797375083&u=QjNBTVAxRThCMlpRTlFGdEREUlFNUUEwQlcwPQ_c_c&k=290406&c=0',# 5-玫瑰赠于你 25
    'http://sh21.caihonger.com/master.php?t=8991&t=30464090271541595146&u=QWtnQUgxWkZEbTRHWkFGb0FEMVJPZ0V4QkdaUU9RODFBRFpkYkE9PQ_c_c&k=291519&c=0', # 12-唉唉唉唉唉唉 25
           ]
 
    qiang_duo_bao_wu(urlList)

   
