from BasePartDLL import *


def yin_qu_mei_nv(url_):
    base = Base()
    base.driver.get(url_)
    delay()
    base.click_word('美女')
    delay()
    if base.if_beauty_ready() == 'yes':
        print('后厢房已满！')
        return
    else:
        for i in range(0, 999):
            base.click_word('选秀')
            delay()
            yes_or_no = base.select_beauties()
            while yes_or_no == 'no':
                base.click_word('选秀')
                yes_or_no = base.select_beauties()
            # base.click_word('进入后厢房')
            base.click_word('进入后厢房')
            if base.if_beauty_ready() == 'yes':
                print('后厢房已满！')
                return
            else:
                continue
            # base.click_word('进入后厢房')
    # time.sleep(100)


if __name__ == '__main__':
    url = 'http://sh27.caihonger.com/master.php?t=42881253145003717798&u' \
          '=QlRvS1pGUTRBV2NHWjFvd0FENVZNbEpoQTJzQWFRPT0_c&k=17959&c=6 '
    yin_qu_mei_nv(url)
