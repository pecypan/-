from BasePartDLL import *

def fun1(base):
	base.click_word('状态')
	base.click_word('使用VIP新手牌')
	base.click_word('单个使用')
	base.click_word('首页')
	base.click_word('系统')
	base.click_word('切换好汉')

def fun2(base):
	base.click_word('宝箱')
	base.click_word('资源')
	try:
		base.click_word('资源箱')
		base.click_word('使用')
		base.click_word('单个使用')
	except:
		pass
	base.click_word('首页')
	base.click_word('系统')
	base.click_word('切换好汉')

def up_31(url_list):
	base = Base()
	base.config(1)
	while True:
		for url in url_list:
			base.driver.get(url)
			delay()
			citylist = base.locate_a('all')
			for city in citylist:
				base.click_word(city)
				base.click_word('资源')
				base.click_word('一键')
				base.click_word('首页')
				base.click_word('系统')
				base.click_word('切换好汉')
				# base.click_word('建筑')
				# base.click_word('自动', 9)
				# base.click_word('自动', 9)
				# base.click_word('自动', 9)
				# base.click_word('自动', 9)
				# base.click_word('自动', 9)
				# base.click_word('自动', 9)
				# base.click_word('自动', 9)
				# base.click_word('自动', 9)
				# base.click_word('自动', 9)
				# base.click_word('自动', 9)
				# base.click_word('自动', 9)
				# base.click_word('首页')
				# base.click_word('系统')
				# base.click_word('切换好汉')

if __name__ == "__main__":
	urlList = [
				'http://sh31.caihonger.com/selectKings.php?u=RGpFSloxTS9VVGNCWUF0aENUY0VZd1EzQ21JR2J3PT0_c&t=13437594576846656625',
		        'http://sh31.caihonger.com/selectKings.php?u=QmpsY01nQnNEbWhVTlZzeFdtUUFad0F6QjJkVk5BPT0_c&t=96509222651156453374&c=0',
		        'http://sh31.caihonger.com/selectKings.php?u=QnpnQWJsUTRWRElCWUFsakN6VUNaUUl4QUdoWFB3PT0_c&t=73357735097901042776&c=0',
		        'http://sh31.caihonger.com/selectKings.php?u=QVQ1ZlBBTnJCbUJRTXdsZ0RqRlNNUUk5QTJRRFlnPT0_c&t=63298572785305090746&c=0',
		        'http://sh31.caihonger.com/selectKings.php?u=QXp3TFpRVnBEMmxiT2dCcUR6RlVNMUpoVURBS2FnPT0_c&t=46474044554666572643&c=0',
		        'http://sh31.caihonger.com/selectKings.php?u=RGpFQWFBZHVEMnhUTVExaFdtRUNZd0F5Vmo0RFpRPT0_c&t=62256098960617125657&c=0',
		        'http://sh31.caihonger.com/selectKings.php?u=VTJ3QWFGSTdWRGRXTkFGdFdtRlVOUU14Vno5U053PT0_c&t=58788822260315899553&c=0',
		        'http://sh31.caihonger.com/selectKings.php?u=QXp3SllWNDNVakVDWUFwbURqVlNNd1EyQ21JRllRPT0_c&t=51640123345572052114&c=0',
		        'http://sh31.caihonger.com/selectKings.php?u=QmprQWFBQnBWalVIWlZvMkNqRlVOUVUzVmo0R1pRPT0_c&t=44890266147756239107&c=0',
		        'http://sh31.caihonger.com/selectKings.php?u=VldvQWFBQnBCR2RXTkFCc0NUSlhObFprQm00Rlp3PT0_c&t=30036761497506828158&c=0',
		        'http://sh31.caihonger.com/selectKings.php?u=QXp3TVpGUTlBR01IWlFCc1hHZFJNRkpnQTJzRlpBPT0_c&t=51959919074412943167&c=0',
		        'http://sh31.caihonger.com/selectKings.php?u=RHpCYU1nUnRVakZhT0ZzM1hXWlRNZ014VkR3SFp3PT0_c&t=66599823577042819715&c=0',
		        'http://sh31.caihonger.com/selectKings.php?u=QkRzUFoxVThCV1pYTlF0bkRUWUNZMVprQzJJS1l3PT0_c&t=39802592168217782288&c=0',
	]

	up_31(urlList)