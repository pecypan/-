from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime


def zi_dong_deng_lu(url_):
    base = Base()
    base.driver.get(url_)
    delay()
    while True:
        base.click_word('刷新')
        time_after(30)
        page_source = str(base.driver.page_source)
        # 定义匹配的正则表达式
        pattern = r'警讯'
        # 进行匹配
        match = re.search(pattern, page_source)
        # 如果匹配成功，则输出匹配的结果
        if match:
            i = 'yes'
        else:
            i = 'no'
        if i == 'yes':
            base.click_word('警讯')
            base.click_word('虎')
            base.click_word('小屁孩')
            base.click_word('虎1')
            base.click_word('出兵')
            base.click_button('全', '连环马', '1')
            base.select_mode_of_battle('歼灭')
            base.click_button('出征')
            base.click_button('普通出征')
            time_after(300)
        else:
            continue



if __name__ == '__main__':
    url = 'http://sh27.caihonger.com/master.php?t=42881253145003717798&u=QlRvS1pGUTRBV2NHWjFvd0FENVZNbEpoQTJzQWFRPT0_c&k=17959&c=1'
    zi_dong_deng_lu(url)
