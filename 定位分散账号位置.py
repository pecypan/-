from BasePartDLL import *

def locate_weizhi(url_list):
	base = Base()
	index = 1
	for url in url_list:
		logger.info(f'----------第{index}个书签----------')
		base.driver.get(url)
		delay()
		city_list = base.locate_a('all')
		for city in city_list:
			base.click_word(city)
			name = base.get_maincity_name()
			location_x, location_y = base.location_mine()
			list_record = name + '(' + str(location_x) + '/' + str(location_y) + ')' + '-->' + str(index)
			with open('分散账号位置.txt', 'a+') as f:
				f.writelines(list_record)
				f.writelines('\n')
				f.close()
			base.driver.back()
		index = index + 1
	base.driver.quit()





if __name__ == '__main__':
	with open('0-小天使.txt', 'r+') as f:
		a = f.readlines()
		f.close()
	locate_weizhi(a)
