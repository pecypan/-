from BasePartDLL import *
import pandas as pd
import os


def find_five_farms(url_, page_star, page_end):
    base = Base()
    base.config(1)
    delay()
    base.driver.get(url_)
    delay()
    base.click_word('地图')
    delay()
    base.location_x(page_star)
    num_dir = {}
    for i in range(page_star, page_end + 1):
        logger.info(f'当前是{i}页')
        num1 = base.locate_a('LINK_TEXT', '富粮县')
        num_dir[i] = num1
        base.click_word('后页')
    base.driver.quit()
    return num_dir


if __name__ == '__main__':
    url = 'http://sh21.caihonger.com/master.php?t=63298572785305090746&u=RHpBTmJsRTVBMlZRTXdGb0R6QlpPbFpwVXpRRFlnPT0_c&k=290188&c=0'
    # 起始区
    PageStar = 47001
    # 截至区
    PageEnd = 49999
    numList = []
    numDir = find_five_farms(url, PageStar, PageEnd)
    for i in numDir:
        if i <= PageEnd - 4 and len(numList) >= 1:
            Sum = numDir[i] + numDir[i + 1] + numDir[i + 2] + numDir[i + 3] + numDir[i + 4]
            len2 = len(numList) - 1
            if Sum >= 5 and ((i + 2) - numList[len2]) >= 5:
                j = i + 2
                numList.append(j)
            else:
                continue
        elif i <= PageEnd - 4 and len(numList) < 1:
            Sum = numDir[i] + numDir[i + 1] + numDir[i + 2] + numDir[i + 3] + numDir[i + 4]
            if Sum >= 5:
                j = i + 2
                numList.append(j)
            else:
                continue
        else:
            break

    dataframe = pd.DataFrame(numList)
    FileName = str(PageStar) + '_' + str(PageEnd) + '.xls'
    dataframe.to_excel(FileName, engine='openpyxl')
