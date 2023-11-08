from BasePartDLL import *


def metting_son(base_):
    base_.click_word('建筑')
    base_.click_word('后厢房')

    page_source = str(base_.driver.page_source)
    pattern1 = r'1/(\d+)'
    match1 = re.search(pattern1, page_source)
    if match1:
        numbers = int(match1.group(1))
        logger.info(f'共有{numbers}页')
    for index in range(numbers):
        try:
            links = base_.driver.find_elements(By.XPATH, "//a[starts-with(@href,'meetbeauty.php?')]")
            for link in range(len(links)):
                base_.click_word('召见')
                base_.click_word('召见')
                base_.click_word('继续召见')
                base_.driver.back()
                base_.driver.back()
                base_.driver.refresh()
                delay()
        except:
            base_.click_word('后页')
        base_.click_word('后页')


def metting(base):
        main_name = base.get_maincity_name()
        base.click_word(main_name)
        city_names = []
        links = base.driver.find_elements(By.XPATH, "//a[starts-with(@href,'master.php?t=')]")
        for link in links:
            city_name = link.text
            if city_name == '返回首页':
                pass
            else:
                city_names.append(city_name)
        base.click_word('返回首页')
        logger.info(f'该城主有{len(city_names)}个分寨')
        for city in city_names:
            base.click_word(main_name)
            base.click_word(city)
            metting_son(base)
            base.click_word('首页')


if __name__ == '__main__':
    urlList = [
        # 'http://sh27.caihonger.com/master.php?t=13437594576846656625&u=QUQ4QmJ3SnVVVGRWTkE1a0NqUUhZQUV5Qm00Q2F3PT0_c&k=17959&c=14',
        'http://sh27.caihonger.com/master.php?a=8392&t=13437594576846656625&u=QUQ4QmJ3SnVVVGRWTkE1a0NqUUhZQUV5Qm00Q2F3PT0_c&k=17959&c=0'
        ]
    main_base = Base()
    main_base.config(1)
    for url in urlList:
        main_base.driver.get(url)
        delay()
        metting(main_base)
    main_base.driver.quit()
        

