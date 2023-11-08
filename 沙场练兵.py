from BasePartDLL import *
import datetime

removestr = 'master.php?t'
tasklist = ['tasks/selectTufei.php?level=5&t','tasks/dailyReward.php?a=9165&t','tasks/randomReward.php?a=7484&t','']


def sha_chang_lian_bing(url_list):
    base = Base()
    base.config(0)
    while True:
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
                base.click_button('10次')
        time_after(350)
    base.driver.quit()


if __name__ == '__main__':
    url = ['http://sh27.caihonger.com/master.php?t=13437594576846656625&u=QUQ4QmJ3SnVVVGRWTkE1a0NqUUhZQUV5Qm00Q2F3PT0_c&k=18210&c=0']
    sha_chang_lian_bing(url)

