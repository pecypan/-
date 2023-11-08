from BasePartDLL import *
import os
import datetime

yijian = '&type=onekey'
removestr = 'master.php?a'
tasklist = ['resource/resourceautobuild.php?t','building/buildingautobuild.php?t','tasks/randomReward.php?a=7484&t','army/zhaobing.php?soldierType=infantry&', 'tasks/dailyReward.php?a=9165&t', 'tasks/randomReward.php?a=7484&t']


def zeng_yuan(base_, flag, location_, location__):
	location_2 = '&x=' + str(location_) + '&y=' + str(location__)
	# base_.click_word('首页')
	location_x, location_y = base_.location_mine()
	if location_x == location_ and location_y == location__:
		logger.info('不能增援本寨！')
		base_.click_word('首页')
		base_.click_word('系统')
		base_.click_word('切换')
		flag = 1
		return flag, location_, location__
	base_.click_word('武将')
	base_.click_word('选将')
	base_.click_word('招募')
	base_.click_word('首页')
	base_.click_word('地图')
	base_.select_city(location_, location_2)
	base_.click_word('出兵')
	try:
		base_.click_button('全', '短刀手')
		base_.select_mode_of_battle('增援')
		base_.click_button('出征')
	except:
		base_.click_word('首页')
	try:
		base_.click_button('普通出征')
		a = base_.is_text_exit('美女')
		logger.info(f'----------{a}----------')
		if a == 1:
			logger.info('未限制')
			base_.click_word('系统')
			base_.click_word('切换好汉')
			flag = 1
			return flag, location_, location__
		elif a == 0:
			time_ = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			logger.info('被限制')
			base_.click_word('首页')
			location_, location__ = base_.location_mine()
			location_in = str(location_) + '|' + str(location__) + '==>>time:' + str(time_)
			logger.info(location_in)
			with open('29_location.txt', 'a+') as f:
				f.write(location_in)
				f.write('\n')
				f.close()
			zeng_yuan(base_, flag, location_, location__)
			flag = 1
	except:
		base_.click_word('首页')
		base_.click_word('系统')
		base_.click_word('切换好汉')
	return flag, location_, location__


def jun_gong(url_list):
	flag_location = 0
	location = 0
	location_y = 0
	base = Base()
	base.config(1)
	for index in range(76, 95):
		logger.info(f'----------{index + 1}----------')
		base.driver.get(url_list[index])
		delay()
		city_list = base.locate_a('all')
		for city in city_list:
			base.click_word(city)
			numbers = base.shi_bin_num()
			if numbers < 1000:
				base.driver.back()
			else:
				if flag_location == 0:
					time_ = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					location, location_y = base.location_mine()
					location_in = str(location) + '|' + str(location_y) + '==>>time:' + str(time_)
					with open('29_location.txt', 'a+') as f:
						f.write(location_in)
						f.write('\n')
						f.close()
					flag_location, location, location_y = zeng_yuan(base,flag_location, location, location_y)
				else:
					logger.info(f'location = {location}, location_y = {location_y}')
					flag_location, location, location_y = zeng_yuan(base,flag_location, location, location_y)





def kai_hui_yuan(url_list):
	base = Base()
	for index in range(33, len(url_list)):
		logger.info(f'----------{index}----------')
		base.driver.get(url_list[index])
		delay()
		city_list = base.locate_a('all')
		for city in city_list:
			base.click_word(city)
			# base.click_word('状态')
			# base.click_word('新手牌')
			# base.click_word('单个使用')
			# base.click_word('首页')
			base.click_word('资源')
			base.click_word('一键')
			for i in range(0, 3):
				base.driver.back()
	base.driver.quit()


def zhao_bin(url_list):
	base = Base()
	base.config(1)
	for index in range(0, len(url_list)):
		logger.info(f'----------{index + 1}----------')
		base.driver.get(url_list[index])
		delay()
		base.click_word('进入',2)
		city_list = base.locate_a('all')
		url = base.driver.current_url
		for city in city_list:
			base.click_word(city)
			url1 = base.driver.current_url
			url2 = url1.replace(removestr, tasklist[3])
			base.driver.get(url2)
			delay(0.35)
			base.click_word('最大招募')
			base.driver.get(url)

def qian_dao(url_list):
	base = Base()
	base.config(1)
	for index in range(0, len(url_list)):
		logger.info(f'----------{index + 1}----------')
		base.driver.get(url_list[index])
		delay()
		city_list = base.locate_a('all')
		for city in city_list:
			base.click_word(city)
			base.click_word('任务')
			base.click_word('领取日')
			base.click_word('任务')
			base.click_word('抽奖')
			base.driver.back()
			base.driver.back()
			base.driver.back()
			base.driver.back()
			base.driver.back()


	base.driver.quit()


def gai_ming(url_list):
	base = Base()
	for index in range(59, len(url_list)):
		logger.info(f'----------{index + 1}----------')
		base.driver.get(url_list[index])
		delay()
		base.click_word('进入',2)
		city_list = base.locate_a('all')
		for city in city_list:
			base.click_word(city)
			base.locate_a('0', 'getowninfo.php?t=')
			base.click_word('改名')
			base.driver.find_element(By.XPATH, '//input[@name="cityname"]').send_keys('九门小号')
			base.click_button('确定')
			base.click_word('首页')
			base.click_word('系统')
			base.click_word('切换')

	base.driver.quit()




				


if __name__ == '__main__':
	with open('21服/21服小号书签1.txt', 'r+') as f:
		a = f.readlines()
		f.close()
	# qian_dao(a) #签到
	zhao_bin(a) #招兵
	# kai_hui_yuan(a)
	# gai_ming(a)
	# jun_gong(a)