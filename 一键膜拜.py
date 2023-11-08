from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime

removestr = 'master.php?a'
tasklist = ['tasks/daleiWorship.php?t','building/buildingList.php?a&t','tasks/randomReward.php?a=7484&t','']

if __name__ == "__main__":
	base = Base()
	base.config(1)
	
	if os.path.exists(r'F:\红颜\location.txt'):
		os.remove(r'F:\红颜\location.txt')
		logger.info('del successful')
	list_AandP = read_csv2list()
	list_A = []
	list_P = []
	for i in range(0, 300):
		list_A.append(list_AandP[i][0])
		list_P.append(list_AandP[i][1])
	url = 'http://sh.caihonger.com/login.php'



	for i in range(1, 299):
		logger.info(f'-----------------------------账号：{list_A[i]}__密码：{list_P[i]}--------------------------------')
		base.driver.get(url)
		base.input_acc_pass(list_A[i], list_P[i])
		base.click_button('确定')
		base.click_word('进入', 3)
		url3 = base.driver.current_url
		delay()
		citys = base.locate_a('all')
		logger.info('当前账号有{}个分寨子'.format(len(citys)))
		for i in range(0, 11):
			base.click_word(citys[i])
			current_url = base.driver.current_url
			url1 = current_url.replace(removestr, tasklist[0])
			print(url1)
			base.driver.get(url1)
			delay(0.35)
			base.driver.get(url3)
			delay(0.35)
	base.driver.quit()