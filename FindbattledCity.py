from BasePartDLL import *


def find_battled_city(url_, location_xmin_, location_Xmax_):
    base = Base()
    base.config(1)
    base.driver.get(url_)
    delay(0.5)
    base.click_word('地图')
    numbs = 0
    for location in range(location_xmin_ - 1, location_Xmax_):
        base.location_x(location)
        logger.info(f'------------{location}----------')
        base.find_battled_cities()
        # numbs = numb + numbs
        # with open('荒山坐标.txt', 'w') as f:
        #     f.write(str(numbs))
        #     f.write('\n')


if __name__ == '__main__':
    url = 'http://sh1.caihonger.com/master.php?t=13437594576846656625&u=QWowS1pBQnNWakJSTUZvd1dtUlNOUUV5Vno4RWJRPT0_c&k=131458&c=0'
    location_Xmin = 21338
    location_Xmax = 25000
    find_battled_city(url, location_Xmin, location_Xmax)
