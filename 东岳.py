from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime

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



	for i in range(5, 10):
		logger.info(f'-----------------------------账号：{list_A[i]}__密码：{list_P[i]}--------------------------------')
		base.driver.get(url)
		base.input_acc_pass(list_A[i], list_P[i])
		base.click_button('确定')
		base.click_word('进入', 3)
		
		delay()
		citys = base.locate_a('all')
		logger.info('当前账号有{}个分寨子'.format(len(citys)))
		for i in range(0, 11):
			base.click_word(citys[i])
			base.click_word('武将')
			base.click_word('选将')
			base.click_word('招募')
			base.click_word('返回')
			base.click_word('招募')
			base.click_word('首页')
			base.click_word('任务')
			base.click_word('东岳')
			base.click_word('报名')
			base.driver.find_element(By.XPATH, '//input[@type="text"]').send_keys(1)
			base.click_button('报名')
			base.click_word('返回')
			base.click_word('报名', 1)
			base.driver.find_element(By.XPATH, '//input[@type="text"]').send_keys(1)
			base.click_button('报名')
			base.click_word('首页')
			base.click_word('系统')
			base.click_word('切换')
	base.driver.close()