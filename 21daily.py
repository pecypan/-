from BasePartDLL import *

yijian = '&type=onekey'
removestr = 'master.php?a'
tasklist = ['resource/resourceautobuild.php?t','building/buildingautobuild.php?t','tasks/randomReward.php?a=7484&t','army/zhaobing.php?soldierType=infantry&']


def kai_hui_yuan(url_list):
	base = Base()
	for index in range(33, len(url_list)):
		logger.info(f'----------{index + 1}----------')
		base.driver.get(url_list[index])
		delay()
		base.click_word('进入', 2)
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


def zhao_bin(urlList):
	base = Base()
	base.config(1)
	for i in range(len(urlList)):
		print(f'------------------------------{i + 1}-----------------------------')
		base.driver.get(urlList[i])
		delay()
		base.click_word('进入',2)
		city_list = base.locate_a('all')
		for city in city_list:
			base.click_word(city)
			urlcurt = base.driver.current_url
			url1 = urlcurt.replace(removestr, tasklist[3])
			base.driver.get(url1)
			delay(0.35)
			base.click_word('最大招募')
			base.driver.get(urlList[i])


def qian_dao(url_list):
	base = Base()
	base.config(1)
	for index in range(0, len(url_list)):
		logger.info(f'----------{index + 1}----------')
		base.driver.get(url_list[index])
		delay()
		base.click_word('进入', 2)
		city_list = base.locate_a('all')
		for city in city_list:
			base.click_word(city)
			# base.click_word('任务')
			# base.click_word('领取日')
			# base.click_word('任务')
			# base.click_word('抽奖')
			# base.driver.back()
			# base.driver.back()
			# base.driver.back()
			# base.driver.back()
			# base.driver.back()
			base.click_word('状态')
			try:
				base.click_word('屏蔽播报', 1)
			except:
				base.click_word('首页')
				base.click_word('系统')
				base.click_word('切换')
				continue
			base.driver.back()
			base.driver.back()
			base.driver.back()


	base.driver.quit()



if __name__ == '__main__':
	with open('21服/21服小号书签1.txt', 'r+') as f:
		a = f.readlines()
		f.close()
	print(len(a))
	qian_dao(a) #签到
	# zhao_bin(a) #招兵
	# kai_hui_yuan(a)