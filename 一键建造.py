from BasePartDLL import *
from mettingBeauty import *
import datetime


yijian = '&type=onekey'
removestr = 'master.php?t'
tasklist = ['resource/resourceautobuild.php?t','building/buildingautobuild.php?t','tasks/randomReward.php?a=7484&t','army/zhaobing.php?soldierType=infantry&']

def jianzhao(url_list):
    base = Base()
    base.config(1)
    for i in range(len(url_list)):
        base.driver.get(url_list[i])
        delay()
        numbers = base.city_number()
        url = list(url_list[i])
        for i in range(numbers):
            url[len(url)-1] = i
            url_need = ''.join(str(x) for x in url)
            url1 = url_need.replace(removestr, tasklist[0]) + yijian
            base.driver.get(url1)
            delay(0.35)
            url2 = url_need.replace(removestr, tasklist[1]) + yijian
            base.driver.get(url2)
            delay(0.35)
    base.driver.quit()

def zhaobin(urlList):
    base = Base()
    base.config(1)
    for i in range(len(urlList)):
        base.driver.get(urlList[i])
        delay()
        numbers = base.city_number()
        url = list(urlList[i])
        for i in range(numbers):
            url[len(url)-1] = i
            url_need = ''.join(str(x) for x in url)
            url1 = url_need.replace(removestr, tasklist[3])
            base.driver.get(url1)
            delay(0.35)
            base.click_word('最大招募')


if __name__ == '__main__':
    urlList1 = [ 
            'http://sh27.caihonger.com/master.php?t=13437594576846656625&u'
                '=QUQ4QmJ3SnVVVGRWTkE1a0NqUUhZQUV5Qm00Q2F3PT0_c&k=18359&c=0',            # 龙怀歌
            'http://sh27.caihonger.com/master.php?t=8423&t=13437594576846656625&u'
                '=QUQ4QmJ3SnVVVGRWTkE1a0NqUUhZQUV5Qm00Q2F3PT0_c&k=18243&c=0',            # 韩
            'http://sh27.caihonger.com/master.php?t=2490&t=1644045681&u'
                '=VW1nS1pGRTlWVFpUUFFCcFhHUUZZQU0z&k=8&c=0',                             # 汝修君
            'http://sh27.caihonger.com/master.php?t=13437594576846656625&u'
                '=QUQ4QmJ3SnVVVGRWTkE1a0NqUUhZQUV5Qm00Q2F3PT0_c&k=19818&c=0',            # 一二三
            'http://sh27.caihonger.com/master.php?t=30464090271541595146&u'
                '=VVJ0ZlFGVkdVVEVIWlE5bUFEMVNPUWc0VmpRQ2F3STRCakJUWWc9PQ_c_c&k=702&c=0', # 长孙
           ]
    urlList2 = [
            'http://sh27.caihonger.com/master.php?t=6354&t=1644045681&u=VW1nS1pGRTlWVFpUUFFCcFhHUUZZQU0z&k=10771&c=0'
    ]       
    # jianzhao(urlList1)
    zhaobin(urlList2)



   
