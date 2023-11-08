from BasePartDLL import *
import os, datetime

stringFa = '&armyType=attack'
stringFb = '&armyType=defend'
stringFA = '&level=3&armyType=attack&side=song'
stringFB = '&level=3&armyType=defend&side=song'
removestr = 'master.php?t'
tasklist = ['union/unionwarapply.php?t','tasks/fightThiefApply.php?t']

def tiger_wujiang(base, city_listE):
	for i in range(3):
		urlE = base.driver.current_url
		urlE_list = list(urlE)
		urlE_list[len(urlE_list) - 1] = city_listE[i]
		print(urlE_list)
		urlE = ''.join(i for i in urlE_list)
		base.driver.get(urlE)
		delay(0.35)
		base.click_word('任务')
		base.click_word('打老虎')
		textE = base.is_text_exit('报名第')
		if textE == 1:
			base.click_word('名武将')
			a = base.xuan_ze_wujiang('_')
			if a == 1:
				base.click_button('报名')
				base.click_word('首页')
			else:
				print('武将失踪了，请查找武将')
				base.click_word('首页')
		else:
			break

def beat_tiger(base, name):
	if name == '汜轻尘':
		city_listE = ['0', '4', '10']
		tiger_wujiang(base, city_listE)
	if name == '相见不如怀念√':
		city_listE = ['0', '3', '4']
		tiger_wujiang(base, city_listE)
		



def zheng_tao(url_list, number):
	base = Base()
	base.config(1)
	for url in url_list:
		urlC = url.replace(removestr, tasklist[1]) + stringFA
		urlD = url.replace(removestr, tasklist[1]) + stringFB
		base.driver.get(urlD)
		base.cq(1)
		delay(0.3)
		try:
			base.click_button('报名')
		except:
			print('报了D')
		base.driver.get(urlC)
		base.cq()
		delay(0.3)
		try:
			base.click_button('报名')
		except:
			print('报了C')

		if number == 2 or number == 6:
			urlA = url.replace(removestr, tasklist[0]) + stringFa
			urlB = url.replace(removestr, tasklist[0]) + stringFb
			base.driver.get(urlB)
			base.cq(1)
			delay(0.3)
			try:
				base.click_button('报名')
			except:
				print('报了B')
			base.driver.get(urlA)
			base.cq()
			delay(0.3)
			try:
				base.click_button('报名')
			except:
				print('报了A')
		base.click_word('首页')
		name = base.get_maincity_name()
		if name == '汜轻尘' or name == '相见不如怀念√':
			beat_tiger(base, name)
	base.driver.quit()



if __name__ == '__main__':
	urlList = [
		'http://sh27.caihonger.com/master.php?t=72005776136166818801&u='
			'Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=17959&c=1',  				# 汜轻尘
		'http://sh21.caihonger.com/master.php?t=8587&t=49298097774437635259&u='
			'RHpBSVpsOHpWREphTzE0MFdtUUhZRkpoQW1vRWJBPT0_c&k=307721&c=0',				# 小天使25
		'http://sh27.caihonger.com/master.php?t=11355471497717507354&u='
			'QkRzT1lnVnBBR2RWTkF4blhXVlhNUWMwVVRBRll3PT0_c&k=18409&c=2', 				# 北凉
		'http://sh27.caihonger.com/master.php?t=81466666722801424776&u='
			'QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=19572&c=1', 				# 甘雨
		'http://sh21.caihonger.com/master.php?t=1689&t=49298097774437635259&u='
			'RHpBSVpsOHpWREphTzE0MFdtUUhZRkpoQW1vRWJBPT0_c&k=291543&c=0',				# 相见
		'http://sh21.caihonger.com/master.php?t=49298097774437635259&u='
			'RHpBSVpsOHpWREphTzE0MFdtUUhZRkpoQW1vRWJBPT0_c&k=63400&c=0', 				# 小天使21
		'http://sh21.caihonger.com/master.php?t=8611&t=95133861564797375083&u='
			'QjNBTVAxRThCMlpRTlFGdEREUlFNUUEwQlcwPQ_c_c&k=290406&c=0', 					# 玫瑰
		'http://sh27.caihonger.com/master.php?t=30464090271541595146&u='
			'VVJ0ZlFGVkdVVEVIWlE5bUFEMVNPUWc0VmpRQ2F3STRCakJUWWc9PQ_c_c&k=43&c=2', 		# 夏末
		'http://sh21.caihonger.com/master.php?t=4019&t=30464090271541595146&u='
			'QkU0SUYxZEVWallCWTFvekRERllNd0l5VXpFRmJBNDBBalFCTUE9PQ_c_c&k=291519&c=0',  # 哎哎哎
		'https://sh27.caihonger.com/master.php?t=64384226349493964270&u='
			'QVc1ZE53UmpCV1ZhT2dsZ1dXZ0NZUWsyQzJnRlpRUSs_c&k=473&c=0', 					# 路过
		'http://sh27.caihonger.com/master.php?t=8280&t=72005776136166818801&u='
			'Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=17980&c=0', 				# 生来一身傲骨
		'http://sh27.hongyanshuihu.com/master.php?t=1627094978&u=QlhFUFBGWnd'
			'BR0FDWUF0aUNEWUFZQUk5VURGV05BRTE_c&k=436&c=1', 							# 罗妞
		'http://sh27.caihonger.com/master.php?t=4963&t=78006833175635470737&u='
			'QlZFUEkxVmdCR1JVTkF0Z0RUMVNORkprQldBS2FRRTBWbVVDT0FROQ_c_c&k=353&c=0', 	# 争锋
		'http://sh27.caihonger.com/master.php?t=1656428277&u='
			'QnpnQWFGYytEbW9GWlYwMUFERlROUU05QzI5Uk0xWW5VU2s9&k=442&c=0', 				# 茶凉
		'http://sh27.caihonger.com/master.php?t=6851&t=72005776136166818801&u='
			'Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=18210&c=0',				# 岂可
		'http://sh27.caihonger.com/master.php?t=7812&t=72005776136166818801&u='
			'Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=19818&c=0',                # 一二三
		'http://sh27.caihonger.com/master.php?t=5605&t=72005776136166818801&u='
			'Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=18243&c=0',				# 韩恺翮
		'http://sh27.caihonger.com/master.php?t=3746&t=72005776136166818801&u='
			'Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=18359&c=0',				# 龙怀歌
	]
	now = datetime.datetime.now()
	str1 = now.weekday()
	zheng_tao(urlList, str1 + 1)
	# os.system('python 签到.py')