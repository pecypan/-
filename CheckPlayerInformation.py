import os

from BasePartDLL import *
import csv


def check_information(url_, players):
    if os.path.exists(r'E:\红颜水\PlayerInformation\playsInformations.csv'):
        os.remove(r'E:\红颜\PlayerInformation\playsInformations.csv')
    else:
        pass
    base = Base()
    base.config(1)
    base.driver.get(url_)
    delay()
    base.click_word('排行',1)
    for player in players:
        base.in_put('player', player)
        base.click_button('查')
        base.click_word(player)
        player_city_information = base.del_player_information(player)
        logger.info(player_city_information)
        with open(r'E:\红颜\PlayerInformation\playsInformations.csv', 'a+') as f:
            writer = csv.writer(f)
            for k, v in player_city_information.items():
                writer.writerow([k, v])
        base.click_word('返回')


if __name__ == '__main__':
    url = 'http://sh27.caihonger.com/master.php?t=46474044554666572643&u'\
          '=QnpnSloxYzdWREpVTlFwZ0FENEFad013QW1JSFp3PT0_c&k=19572&c=0'
    Players = ['唐寅', '顾线线', '胸小话少表情叼', '青春', '怒翼龙',
               '忆苍年', '小屁孩', '呐呐呐']
    check_information(url, Players)
