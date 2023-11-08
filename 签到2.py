from BasePartDLL import *


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
        'http://sh21.caihonger.com/selectKings.php?u=RHpBTmJsRTVBMlZRTXdGb0R6QlpPbFpwVXpRRFlnPT0_c&t=63298572785305090746',
        'http://sh21.caihonger.com/selectKings.php?c=0&u=RHpBSVpsOHpWREphTzE0MFdtUUhZRkpoQW1vRWJBPT0_c&t=49298097774437635259',    # 5-相见
        'http://sh29.caihonger.com/selectKings.php?u=QUQ4TVlnVnBBbVJiT2x3MkN6VlhNQUV5QjJjRVpnPT0_c&t=50828153549436911439',
        'http://sh29.caihonger.com/selectKings.php?u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&t=61643553276718422733',
        'http://sh31.caihonger.com/selectKings.php?u=RGpFSloxTS9VVGNCWUF0aENUY0VZd1EzQ21JR2J3PT0_c&t=13437594576846656625',
        'http://sh31.caihonger.com/selectKings.php?u=QnpnQWJsUTRWRElCWUFsakN6VUNaUUl4QUdoWFB3PT0_c&t=73357735097901042776&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QVQ1ZlBBTnJCbUJRTXdsZ0RqRlNNUUk5QTJRRFlnPT0_c&t=63298572785305090746&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QXp3TFpRVnBEMmxiT2dCcUR6RlVNMUpoVURBS2FnPT0_c&t=46474044554666572643&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=RGpFQWFBZHVEMnhUTVExaFdtRUNZd0F5Vmo0RFpRPT0_c&t=62256098960617125657&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=VTJ3QWFGSTdWRGRXTkFGdFdtRlVOUU14Vno5U053PT0_c&t=58788822260315899553&c=0&t=58788822260315899553&u=VTJ3QWFGSTdWRGRXTkFGdFdtRlVOUU14Vno5U053PT0_c&k=1119&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QXp3SllWNDNVakVDWUFwbURqVlNNd1EyQ21JRllRPT0_c&t=51640123345572052114&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QmprQWFBQnBWalVIWlZvMkNqRlVOUVUzVmo0R1pRPT0_c&t=44890266147756239107&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=VldvQWFBQnBCR2RXTkFCc0NUSlhObFprQm00Rlp3PT0_c&t=30036761497506828158&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QXp3TVpGUTlBR01IWlFCc1hHZFJNRkpnQTJzRlpBPT0_c&t=51959919074412943167&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=RHpCYU1nUnRVakZhT0ZzM1hXWlRNZ014VkR3SFp3PT0_c&t=66599823577042819715&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QkRzUFoxVThCV1pYTlF0bkRUWUNZMVprQzJJS1l3PT0_c&t=39802592168217782288&c=0',
    ]
    with open(r'E:\红颜\anser.json') as f:
        data = json.load(f)
    qian_dao(urlList)