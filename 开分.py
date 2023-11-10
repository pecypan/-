from BasePartDLL import *
from 自动迁城 import read_csv2list
def kai_fen_hao(url, list_a, list_p):
	base = Base()
	base.config(1)
	base.driver.get(url)
	delay()
    # 登录
	for i in range(8, 20):
		logger.info(f'-----------------------------账号：{list_a[i]}__密码：{list_p[i]}--------------------------------')
		base.input_acc_pass(list_a[i], list_p[i])
		base.click_button('确定')
        # 选择区服
		base.select_sh(6)
		base.click_word('创建')
		for i in range(0, 20):
			base.yan_zhen()
			base.click_button('确定')
			index = base.is_text_exit('已达到上限')
			if index == 1:
				base.click_word('返回')
				base.click_word('重新登录')
				break
			index2 = base.is_text_exit('请输入4位验证码')
			index3 = base.is_text_exit('验证码输入错误')
			if index2 == 1 or index3 == 1:
				continue
			base.driver.back()
			base.driver.refresh()

	base.driver.quit()

def kai_fen(base):
	x, y = base.location_mine()
	base.click_word('地图')
	base.location_x(x + 60)
	links = base.driver.find_elements(By.XPATH, "//a[starts-with(@href,'mapgetonemap.php?')]")
	i = 0
	for link in links:
		if link.text == '荒山':
			i = i + 1
	print(i)
	for j in range(i):
		base.click_word('荒山', j)
		page_source2 = str(base.driver.page_source)
		match2 = re.search(r'\d+/\d+', page_source2)
		if match2:
			date2 = match2.group() + '\n'
			with open('fenzhai.txt', 'r') as f:
				list_location = f.readlines()
				if date2 in list_location:
					base.driver.back()
					delay()
					continue
		try:
			base.click_word('建造分寨')
		except:
			base.driver.back()
			continue
		index = base.is_text_exit('需要有3名')
		index2 = base.is_text_exit('15级')
		index3 = base.is_text_exit('已经')
		if index == 1 or index2 == 1 or index3 == 1:
			base.click_word('首页')
			base.click_word('系统')
			base.click_word('切换')
			break
		while True:
			base.yan_zhen()
			base.click_button('确定')
			index1 = base.is_text_exit('请输入4位验证码')
			index2 = base.is_text_exit('验证码输入错误')
			index3 = base.is_text_exit('3名工匠手已经派出')
			if index3 == 1:
				base.click_word('首页')
				base.click_word('系统')
				base.click_word('切换')
				with open('fenzhai.txt', 'a+') as f:
					f.write(date2)
					delay()
				break
			if index1 == 1 or index2 == 1:
				base.driver.back()
				base.driver.refresh()
		break



def kai_fen_zhai(url, list_a, list_p):
	base = Base()
	base.config(1)
	base.driver.get(url)
	delay()
    # 登录
	for i in range(100, 110):
		logger.info(f'-----------------------------账号：{list_a[i]}__密码：{list_p[i]}--------------------------------')
		base.input_acc_pass(list_a[i], list_p[i])
		base.click_button('确定')
        # 选择区服
		base.select_sh(6)
		city_list = base.locate_a('all')
		for city in city_list:
			base.click_word(city)
			# base.click_word('招兵')
			# index = base.is_text_exit('剩余时间')
			# if index == 1:
			# 	base.driver.back()
			# 	base.driver.back()
			# 	continue
			# base.click_word('首页')
			num = base.city_number()
			if num >= 2:
				base.click_word('系统')
				base.click_word('切换好汉')
				continue
			# base.click_word('宝箱')
			# base.click_word('资源')
			# base.click_word('资源箱')
			# base.click_word('使用')
			# base.driver.find_element(By.XPATH, "//input[@name='usecount']").send_keys(2)
			# base.click_word('使用')
			# base.click_word('首页')
			# # base.click_word('建筑')
			# # index4 = base.is_text_exit('速建')
			# # if index4 == 1:
			# # 	for i in range(3):
			# # 		base.click_word('速建')
			# # base.click_word('返回')
			# # base.click_word('建筑')
			# # level1 = base.jian_zhu_level('军　营')
			# # level2 = base.jian_zhu_level('聚义厅')
			# # i = 15 - level2
			# # if i >= 1:
			# # 	base.click_word('聚义厅')
			# # 	for j in range(i):
			# # 		base.click_word('升级')
			# # 		base.click_word('速建')
			# # 		base.click_word('返回')
			# # 	base.click_word('建筑')
			# # i = 15 - level1
			# # if i >= 1:
			# # 	base.click_word('军　营')
			# # 	for j in range(i):
			# # 		base.click_word('升级')
			# # 		base.click_word('速建')
			# # 		base.click_word('返回')
			# # 	base.click_word('首页')
			# base.click_word('首页')
			# base.click_word('招兵')
			# base.click_word('(建寨)工匠手')
			# for j in range(10):
			# 	base.driver.find_element(By.XPATH, "//input[@name='s_num']").send_keys(10)
			# 	base.yan_zhen()
			# 	base.click_button('确定')
			# 	index = base.is_text_exit('正在招募')
			# 	if index == 1:
			# 		break
			# 	else:
			# 		base.driver.back()
			# 		base.driver.refresh()

			kai_fen(base)
			# base.click_word('首页')
			# base.click_word('系统')
			# base.click_word('切换好汉')
		base.click_word('重新登录')


if __name__ == "__main__":
    list_AandP = read_csv2list()
    list_A = []
    list_P = []
    for i in range(0, 300):
        list_A.append(list_AandP[i][0])
        list_P.append(list_AandP[i][1])
    Url = 'http://sh.caihonger.com/login.php'
    # kai_fen_hao(Url, list_A, list_P)
    kai_fen_zhai(Url, list_A, list_P)
    # with open('fenzhai.txt', 'r+') as f:
    	# a = f.readlines()
    	# print(a)


# base = Base()
# base.config(1)
# base.driver.get('http://sh30.caihonger.com/selectKings.php?c=0&u=QkRzSVpsSStBMlZiT2dwZ1hXTlFOMU5nQjI4QmFBPT0_c&t=13437594576846656625')
# base.click_word('创建')
# for i in range(0, 10):
# 	base.yan_zhen()
# 	base.click_button('确定')
# 	index = base.is_text_exit('10个')
# 	if index == 1:
# 		break
# 	base.driver.back()
# 	base.driver.refresh()
# delay(100)
