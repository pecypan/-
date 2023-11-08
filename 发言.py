from BasePartDLL import *


def qian_dao(url_):
    base = Base()
    base.config(1)
    index = 1
    for url in url_:
        logger.debug(f'----------{index}----------')
        base.driver.get(url)
        base.click_word('进入', 3)
        delay()
        city_list = base.locate_a('all')
        for city in city_list:
            base.click_word(city)
            base.click_word('聊天')
            base.click_button('清除')
            a = base.driver.find_element(By.XPATH, '//textarea[@id="body"]').send_keys('清屏，小学生赶紧离开。。')
            base.click_button('发送')
            for i in range(0, 3):
                base.driver.back()
        index = index + 1
    base.driver.quit()


if __name__ == '__main__':
    urlList = [
        'http://sh27.caihonger.com/selectKings.php?u=VkdzSllWWS9VakZRTWdoa0NETUZaQWc2QjI1UU9RPT0_c&t'
        '=39802592168217782288',  # 1
        'http://sh27.caihonger.com/selectKings.php?c=0&u=VVc0TFkxNDNBR05WTjF3d1htVlRNbEZqVmo0TGF3PT0_c&t'
        '=66599823577042819715',  # 2
        'http://sh27.caihonger.com/selectKings.php?c=0&u=VW0xWU1BTnFCMlJYTlFCc0FEdFVOUUV6VkR3RFlnPT0_c&t'
        '=51959919074412943167',  # 3
        'http://sh27.caihonger.com/selectKings.php?c=0&u=QnpnSVlBQnBVekJUTVZ3d1dtRUVaUWs3Qm00Q1lBPT0_c&t'
        '=30036761497506828158',  # 4
        'http://sh27.caihonger.com/selectKings.php?c=0&u=RHpBSllWTTZBR05VTmx3d0FUb0NZMUpnQjI5UU13PT0_c&t'
        '=44890266147756239107',  # 5
        'http://sh27.caihonger.com/selectKings.php?c=0&u=QVQ1Y05GODJCV1phT0E1aUNqRlJNQUF5Q21JSFl3PT0_c&t'
        '=51640123345572052114',  # 6
        'http://sh27.caihonger.com/selectKings.php?c=0&u=QlRwYU1sQTVBMkFCWTEweENETlNNd014Vno5Vk1BPT0_c&t'
        '=58788822260315899553',  # 7
        'http://sh27.caihonger.com/selectKings.php?c=0&u=RGpFT1pnSnJWVFpWTndwbUFUcFVOVlJtQW1wWE1RPT0_c&t'
        '=62256098960617125657'  # 8
    ]
    qian_dao(urlList)

# base = Base()
# base.config(1)
# base.driver.get('http://sh31.caihonger.com/tasks/assignName1.php?a=5988&t=33268223951312239404&u=VkQ0QmFBQnBVenM9&k=2468&c=0')
# base.click_word('任务')
# base.click_word('就叫')
# base.click_word('领取奖励')
# base.click_word('领取奖励')
# base.click_word('任务')
# base.click_word('任务')
# base.click_word('点击')
# base.click_word('领取奖励')
# base.click_word('领取奖励')
# base.click_word('任务')
# base.click_word('任务')
# base.click_word('升级')
# base.click_word('领取奖励')
# base.click_word('领取奖励')
# base.click_word('任务')
# base.click_word('任务')
# base.click_word('攻打')
# base.click_word('领取奖励')
# base.click_word('领取奖励')
# base.click_word('进入')
# base.click_button('发送')
# base.click_word('进入')
# base.click_word('状态')
# base.click_word('屏蔽播报')
# base.click_word('返回')
# base.click_word('屏蔽播报')
# base.click_word('返回')
# base.click_word('屏蔽播报')
# base.click_word('首页')
# base.click_word('任务')
# base.click_word('签到')
# for i in range(7):
#     base.click_word('签')
# base.click_word('首页')
# base.click_word('店铺')
# base.click_word('后页')
# base.click_word('宝珠袋')
# base.driver.find_element(By.XPATH, "//input[@name='buycount']").clear()
# base.driver.find_element(By.XPATH, "//input[@name='buycount']").send_keys(668)
# base.click_button('买给自己')
# base.click_word('返回')
# base.driver.find_element(By.XPATH, "//input[@name='buycount']").clear()
# base.driver.find_element(By.XPATH, "//input[@name='buycount']").send_keys(999)
# base.click_button('买给自己')
# base.click_word('使用')
# base.driver.find_element(By.XPATH, "//input[@name='usecount']").send_keys(16)
# delay()
# while True:
#     base.click_button('使用')
#     index = base.is_text_exit('错误')
#     if index == 1:
#         base.click_word('全部使用')
#         break
#     else:
#         pass

base.driver.quit()