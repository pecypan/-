from BasePartDLL import *

def auto_la_zi(url):
	base = Base()
	base.config(1)
	base.driver.get(url)
	delay()
	base.locate_a('0', 'getowninfo.php?t=')
	city_names = []
	links = base.driver.find_elements(By.XPATH, "//a[starts-with(@href,'master.php?t=')]")
	for link in links:
		city_name = link.text
		if city_name == '返回首页':
			pass
		else:
			city_names.append(city_name)
	for city in city_names:
		base.click_word(city)
		numb = base.resource_num('粮')
		if numb < 5000000:
			base.click_word('地图')
			





		base.locate_a('0', 'getowninfo.php?t=')



if __name__ == "__main__":
	urlList = 'http://sh27.caihonger.com/master.php?a=6846&t=30615312449625969544&u=QWtnT0VWNU5CV1ZVTmx3MVhHRUZiZ0F3QkdZTFlsWnNWV05UWWc9PQ_c_c&k=43&c=0'
	auto_la_zi(urlList)