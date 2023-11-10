from BasePartDLL import *
import json

removestr = 'master.php?a'
tasklist = ['tasks/selectBaowu.php?level=5&t','tasks/dailyReward.php?a=9165&t','tasks/randomReward.php?a=7484&t','building/buildingList.php?a=1789','tasks/dailyTest.php?a']

def dati(base):
    text3 = base.is_text_exit('今天您已答过题，明天再来吧')
    if text3 == 1:
        return 0
    page_source = str(base.driver.page_source)
    pattern = r'问题：(.+)？'
    match = re.search(pattern, page_source)
    if match:
        matching = match.group(1)
        print(matching)
    else:
        return 0
    if matching in data:
        print('yes')
        word = data[matching]
        base.click_word(word)
        text1 = base.is_text_exit('答对了')
        if text1 == 1:
            pass
        else:
            base.driver.quit()
    else:
        print('no')
        delay(1000)
    text2 = base.is_text_exit('您答对了')
    if text2 == 1:
        return 0


def qian_dao(url_):
    base = Base()
    base.config(1)
    j = 1
    for url in url_:
        logger.debug(f'----------{j}----------')
        base.driver.get(url)
        delay()
        city_list = base.locate_a('all')
        for city in city_list:
            base.click_word(city)
            mainurl = base.driver.current_url
            # base.click_word('任务')
            # base.click_word('签到')
            # try:
            #     base.click_word('签到')
            # except:
            #     pass
            qiandaourl = mainurl.replace(removestr, tasklist[1])
            base.driver.get(qiandaourl)
            delay(0.3)
            choujiangurl = mainurl.replace(removestr, tasklist[2])
            base.driver.get(choujiangurl)
            delay(0.3)
            # datiurl = mainurl.replace(removestr, tasklist[4])
            # base.driver.get(datiurl)
            # delay(0.3)
            # while True:
            #     index22 = dati(base)
            #     if index22 == 0:
            #         break
            base.driver.get(url)
            delay(0.3)
        j = j + 1


if __name__ == '__main__':
    urlList = [
        'http://sh27.caihonger.com/selectKings.php?u=VXljTU5GZHNVVEZiTlY0NUNqcFRNUWc4VmpWUk1BPT0_c&t'
            '=32080335616043506375',    # 小猪
        'http://sh27.caihonger.com/selectKings.php?u=QTJGYWJnY3VEanBVTWc1cEREMENhUWsrQ21sUU1nVTJWRFJYT1ZVMA_c_c&t'
            '=27584735866379183154',    # 画颜卿
        'http://sh31.caihonger.com/selectKings.php?u=QTBrQkhsRkNBV0ZYTlFCcFdtZFRPRkppQkdZR2J3ODFVbVJUWWc9PQ_c_c&t'
            '=30464090271541595146',    # 0-大郎
        'http://sh27.caihonger.com/selectKings.php?c=0&u=QVZVQU0xVnpEMjlWTlY0MURqNERaVkprQTJaWE5GRmtBVElBT2djNg_c_c&t'
            '=85226957694941849938',    # 1-回归
        'http://sh27.caihonger.com/selectKings.php?c=0&u=VW1nS1pGRTlWVFpUUFFCcFhHUUZZQU0z&t=1644045681',
                                        # 2-汝
        'http://sh27.caihonger.com/selectKings.php?c=0&u=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&t'
            '=72005776136166818801',    # 3-汜
        'https://sh27.caihonger.com/selectKings.php?u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&t'
            '=81466666722801424776',    # 4-甘雨
        'http://sh27.caihonger.com/selectKings.php?c=0&u=QlZFUEkxVmdCR1JVTkF0Z0RUMVNORkprQldBS2FRRTBWbVVDT0FROQ_c_c&t'
            '=78006833175635470737',    # 6-争
        'http://sh27.caihonger.com/selectKings.php?u=VVJ0ZlFGVkdVVEVIWlE5bUFEMVNPUWc0VmpRQ2F3STRCakJUWWc9PQ_c_c&t'
            '=30464090271541595146',    # 7-夏未尽♀花己落 
        'http://sh27.caihonger.com/selectKings.php?u=QkRzT1lnVnBBR2RWTkF4blhXVlhNUWMwVVRBRll3PT0_c&t'
            '=11355471497717507354&c=0',# 8-北凉
        'http://sh27.caihonger.com/selectKings.php?u=QnpnQWFGYytEbW9GWlYwMUFERlROUU05QzI5Uk0xWW5VU2s9&t'
            '=1656428277',              # 9-茶凉
        'https://sh27.caihonger.com/selectKings.php?c=0&u=QVQ0SVpsNHlWVE5UTWw0MFhtQUhZRlJuVkR4WFB3PT0_c&t=49298097774437635259',
        'http://sh27.caihonger.com/selectKings.php?c=0&u=VldvQWFBVnNVVElHWkFCc1dtRlhOZ0F5Qm04QmFBPT0_c&t=39802592168217782288',
        'http://sh27.caihonger.com/selectKings.php?c=0&u=VW0wS1lnVnNWalZUTVF4Z0REZFlPVlprVXpzQllRPT0_c&t=66599823577042819715',
        'http://sh27.caihonger.com/selectKings.php?u=QWowQllnTnJWVE1DWVY0M1dXWURZRlJyQzJ3QllBPT0_c&t=63298572785305090746',
        'http://sh27.caihonger.com/selectKings.php?c=0&u=RGpFT1pnSnJWVFpWTndwbUFUcFVOVlJtQW1wWE1RPT0_c&t=62256098960617125657',
        'http://sh27.caihonger.com/selectKings.php?c=0&u=QlRwYU1sQTVBMkFCWTEweENETlNNd014Vno5Vk1BPT0_c&t=58788822260315899553',
        'http://sh27.caihonger.com/selectKings.php?c=0&u=QVQ1Y05GODJCV1phT0E1aUNqRlJNQUF5Q21JSFl3PT0_c&t=51640123345572052114',
        'http://sh27.caihonger.com/selectKings.php?c=0&u=RHpBSllWTTZBR05VTmx3d0FUb0NZMUpnQjI5UU13PT0_c&t=44890266147756239107',
        'http://sh27.caihonger.com/selectKings.php?c=0&u=QnpnSVlBQnBVekJUTVZ3d1dtRUVaUWs3Qm00Q1lBPT0_c&t=30036761497506828158',
        'http://sh27.caihonger.com/selectKings.php?c=0&u=VW0xWU1BTnFCMlJYTlFCc0FEdFVOUUV6VkR3RFlnPT0_c&t=51959919074412943167',
    ]
    with open(r'E:\红颜\anser.json') as f:
        data = json.load(f)
    qian_dao(urlList)