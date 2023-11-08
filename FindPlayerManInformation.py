from BasePartDLL import *
import csv


def man_information(url_):
    base = Base()
    base.driver.get(url_)
    delay()
    base.click_word('排行')
    base.click_word('武将')
    base.click_word('统御')
    man_information_dict = base.locate_a('Man', 10)
    with open('latest_man_information2.csv', 'w') as f:
        writer = csv.writer(f)
        for k, v in man_information_dict.items():
            writer.writerow([k, v])


if __name__ == '__main__':
    url = 'http://sh27.caihonger.com/master.php?a=5375&t=46474044554666572643&u' \
          '=QnpnSloxYzdWREpVTlFwZ0FENEFad013QW1JSFp3PT0_c&k=19572&c=0'
    man_information(url)
