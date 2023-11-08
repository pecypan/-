from BasePartDLL import *




def ABC(base):
	a = 1
	while True:
		# for i in range()
		base.click_word('一键')
		base.click_word('返回')
		index2 = base.is_text_exit('速建')
		if index2 == 1:
			base.click_word('速建')
			while True:
				index = base.is_text_exit('继续')
				if index == 1:
					base.click_word('速建')
				else:
					base.click_word('返回')
					break
		else:
			index3 = base.is_text_exit('升')
			if index3 == 1:
				base.click_word('首页')
				base.click_word('联盟')
				base.click_word('联盟科技')
				base.click_word('资源生产')
				base.driver.find_element(By.XPATH, "//input[@id='captive']").send_keys(100000)
				base.click_button('确定')
				base.click_word('首页')
				base.click_word('建筑')
				ABC(base)
			else:
				base.driver.quit()
				a = 0
				break
		if a == 0:
			break
				


base_ = Base()
# for index in range(0, 10)
base_.driver.get('http://sh21.caihonger.com/master.php?a=9162&t=84015268046561712278&u=QVZVUFBGSjBBMk1BWUZveENEaFpQMVJpQVdRRFlGVmdWbVVIUFZCZw_c_c&k=67362&c=11')
delay()
base_.click_word('建筑')
ABC(base_)