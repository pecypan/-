from BasePartDLL import *


def zhao_mu(url_):
    base = Base()
    base.driver.get(url_)
    base.click_word('武将')
    base.click_word('选将')
    for i in range(0, 999):
        base.select_man('声望型')
        a = base.select_man('谋略型')
        if a == 'yes':
            print('武将已经满了')
            break
        else:
            base.click_word('选将')


# time.sleep(100)

if __name__ == '__main__':
    url = 'http://sh27.caihonger.com/master.php?t=42881253145003717798&u=QlRvS1pGUTRBV2NHWjFvd0FENVZNbEpoQTJzQWFRPT0_c' \
          '&k=17959&c=8 '
    zhao_mu(url)
