from BasePartDLL import *
from 自动迁城 import read_csv2list
import os
import datetime

# Location = 3392 # 252start
# Location = 40744 #裤裆
# Location = 40979
# Location = 42079 #渣风
# 20493,4 小天使 25
# 25946,2 小天使 21
# locationFlist = ['&x=26136&y=8', '&x=28448&y=4', '&x=31090&y=4', '&x=30604&y=2', '&x=27272&y=2', 
# 				 '&x=26877&y=6', '&x=23551&y=3', '&x=23515&y=6', '&x=23834&y=4', '&x=25986&y=3',
# 				 '&x=25252&y=5', '&x=23997&y=3', '&x=23911&y=1', '&x=23925&y=1', '&x=23958&y=1',
# 				 '&x=23405&y=5', '&x=23515&y=6']
# locationFlist = ['&x=25946&y=2', '&x=20493&y=4', '&x=23999&y=3']
locationFlist = ['&x=24299&y=5']
removestr = 'master.php?a'
tasklist = ['tasks/selectBaowu.php?level=5&t','tasks/dailyReward.php?a=9165&t','tasks/randomReward.php?a=7484&t','building/dianjiangtai.php?a=2218&t','combat/dispatch.php?t']
lenlist = 0

def fun(url_):
	base = Base()
	base.config(1)
	delay()
	lenlist = len(locationFlist) - 1
	# 登录
	for i in range(275, len(url_)):
		print(f'-----------------------------------账号：{i+1}-----------------------------------------')
		# 选择区服
		base.driver.get(url_[i])
		delay(0.3)
		base.click_word('进入', 2)
		city_list = base.locate_a('all')
		for city in city_list:
			base.click_word(city)
			mainurl = base.driver.current_url
			number = base.shi_bin_num()
			if number < 50000:
				base.driver.get(url_[i])
				delay(0.3)
				continue
			else:
				number2 = base.resource_num('粮')
				if number2 <= 0:
					url2 = mainurl.replace(removestr, tasklist[1])
					base.driver.get(url2)
					delay(0.3)
				url3 = mainurl.replace(removestr, tasklist[3])
				base.driver.get(url3)
				delay(0.3)
				base.click_word('招募')
				url4 = mainurl.replace(removestr, tasklist[4])
				url4 = url4 + locationFlist[lenlist]
				base.driver.get(url4)
				delay(0.3)
				try:
					base.select_mode_of_battle('增援')
					base.click_button('全', '短刀手')
					# base.click_button('全', '短刀手')
					base.click_button('出征')
					base.click_button('普通出征')
					index = base.is_text_exit('出兵限制说明')
					if index == 1:
						lenlist = lenlist - 1
						if lenlist < 0:
							base.driver.quit()
							print('game over')
							return
						else:
							url4 = mainurl.replace(removestr, tasklist[4])
							url4 = url4 + locationFlist[lenlist]
							base.driver.get(url4)
							delay(0.3)
							try:
								base.select_mode_of_battle('增援')
								base.click_button('全', '短刀手')
								base.click_button('出征')
								base.click_button('普通出征')
								base.driver.get(url_[i])
							except:
								print('error.....................')
								base.driver.quit()
					else:
						base.driver.get(url_[i])
				except:
					base.driver.get(url_[i])


if __name__ == '__main__':
    with open(r'E:\红颜\21服\21服小号书签1.txt', 'r+') as f:
        Url_list = f.readlines()
        f.close()

    # with open('21服/21原来的.txt', 'r+') as f:  #第23个书签
    #   Url_list = f.readlines()
    #   f.close()

    fun(Url_list)
