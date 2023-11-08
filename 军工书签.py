from BasePartDLL import *


def fun(url_list):
	base = Base()
	base.config(1)
	flag = 0
	for index in range(80, 100):
		logger.info(f'==========当前是第{index + 1}个书签==========')
		base.driver.get(url_list[index])
		delay()
		base.click_word('进入',2)
		city_list = base.locate_a('all')
		for city in city_list:
			base.click_word(city)
			location, location_y = base.location_mine()
			# if location < 40000:
			numbers = base.shi_bin_num()
			if numbers > 30000:
				# base.click_word('任务')
				# base.click_word('领取日')
				# base.click_word('首页')
				base.click_word('武将')
				base.click_word('选将')
				base.click_word('招募')
				base.click_word('首页')
				base.click_word('地图')
				base.location_x(20052)
				base.click_word('夜静春山空')
				base.click_word('出兵')
				# base.select_mode_of_battle('增援')
				base.click_button('全', '弓箭手')
				base.click_button('出征')
				base.click_button('普通出征')
				y = base.is_text_exit('限制')
				if y == 0:
					flag = flag + 1
					base.click_word('系统')
					base.click_word('切换')
				else:
					logger.info('出兵被限制')
					logger.info(f'总行军数:{flag}')
					base.driver.quit()
					return

			else:
				base.click_word('系统')
				base.click_word('切换好汉')
			# else:
			# 	base.click_word('系统')
			# 	base.click_word('切换好汉')







if __name__ == '__main__':

	# 25
	with open(r'E:\红颜\21服\21服小号书签.txt', 'r+') as f:
		Url_list = f.readlines()
		# logger.info(Url_list)
		f.close()

	fun(Url_list)

