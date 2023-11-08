import re, sys, json, requests, base64, time, random, csv, threading, func_timeout, os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from loguru import logger
from tqdm import tqdm
from openpyxl import load_workbook
from func_timeout import func_set_timeout, FunctionTimedOut
from urllib.parse import urlparse, urlunparse, urljoin
from PIL import Image

# logger.add(sys.stdout,
#             format= "<green>{time:YYYY-MM-DD HH:mm:ss:SSS}</green> | "  # 颜色>时间
#                     "<cyan>{module}</cyan>.<cyan>{function}</cyan>"  # 模块名.方法名
#                     "<cyan>[{line}]</cyan> | "  # 行号
#                     "<level>{level}[{thread.name}]</level>： "  # 等级 # 线程名
#                     "<level>{message}</level>",  # 日志内容
#                      )



def delay(*args):
    # delay_list = [0.35]
    if len(args) <= 0:
        # time.sleep(random.choice(delay_list))
        time.sleep(0.35)
    else:
        time.sleep(args[0])


class Base:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images': 2}
        self.options.add_experimental_option('prefs',prefs)
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--no-sandbox")
        # chrome.implicitly_wait(5)


        # 忽略证书错误
        self.options.add_argument('--ignore-certificate-errors')
        # 忽略 Bluetooth: bluetooth_adapter_winrt.cc:1075 Getting Default Adapter failed. 错误
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 忽略 DevTools listening on ws://127.0.0.1... 提示
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])


    def config(self, flag):
        if flag == 1:
            self.driver = webdriver.Chrome(chrome_options=self.options)
            self.driver.minimize_window()
        elif flag == 0:
            self.options.add_argument("--headless")
            self.options.add_argument("--disable-gpu")
            self.driver = webdriver.Chrome(chrome_options=self.options)

    # 点击文字
    @func_set_timeout(20)
    def click_word2(self, word_str, *args):
        click_str = "//a[contains(text(),'" + word_str + "')]"
        if len(args) <= 0:
            try:
                self.driver.find_element(By.XPATH, click_str).click()
                logger.info(f'ClickedWord：{word_str}')
                delay()
                return 1
            except NoSuchElementException:
                self.driver.refresh()
                delay()
                return 0
        else:
            try:
                self.driver.find_elements(By.XPATH, click_str)[args[0]].click()
                logger.info(f'ClickedWord：{word_str}')
                delay()
                return 1
            except NoSuchElementException:
                base.driver.refresh()
                return 0


    def click_word(self, word_str, *args):
        if len(args) > 0:
            num = args[0]
            try:
                index = self.click_word2(word_str, num)
                if index == 1:
                    pass
                else:
                    index2 = self.click_word2(word_str, num)
                    if index2 == 0:
                        logger.info(f'点击文字{word_str}失败!')
            except FunctionTimedOut as e:
                logger.info(e)
                self.driver.back()
                logger.info('刷新页面')
                delay()
                self.click_word2(word_str, num)
        else:
            try:
                index = self.click_word2(word_str)
                if index == 1:
                    pass
                else:
                    index2 = self.click_word2(word_str)
                    if index2 == 0:
                        logger.info(f'点击文字{word_str}失败!')
            except FunctionTimedOut as e:
                logger.info(e)
                self.driver.back()
                delay()
                logger.info('刷新页面')
                self.click_word2(word_str)



    # 点击按钮
    @func_set_timeout(20)
    def click_button2(self, button_str, *args):
        soldier_type = ['moped', 'tiger', 'heavy', 'infantry', 'crossbow', 'marines', 'punching', 'catapult', 'scout', 'sapper']
        if button_str == '出兵':
            self.driver.find_element(By.LINK_TEXT, button_str).click()
            logger.info('点击按钮--出兵')

        elif button_str == '出征':
            self.driver.find_element(By.NAME, 'submit').click()
            logger.info('点击按钮--出征')

        elif button_str == '普通出征':
            self.driver.find_element(By.NAME, 'submit').click()
            logger.info('点击按钮--普通出征')

        elif button_str == '1次':
            self.driver.find_element(By.XPATH, '//input[@value="1次"]').click()
            logger.info('点击按钮--1次')

        elif button_str == '10次':
            try:
                self.driver.find_element(By.XPATH, '//input[@value="10次"]').click()
                delay()
                return
            except:
                pass
            try:
                self.driver.find_element(By.XPATH, '//input[@value="9次"]').click()
                delay()
                return
            except:
                pass
            try:
                self.driver.find_element(By.XPATH, '//input[@value="8次"]').click()
                delay()
                return
            except:
                pass
            try:
                self.driver.find_element(By.XPATH, '//input[@value="7次"]').click()
                delay()
                return
            except:
                pass
            try:
                self.driver.find_element(By.XPATH, '//input[@value="6次"]').click()
                delay()
                return
            except:
                pass
            try:
                self.driver.find_element(By.XPATH, '//input[@value="5次"]').click()
                delay()
                return
            except:
                pass
            try:
                self.driver.find_element(By.XPATH, '//input[@value="4次"]').click()
                delay()
                return
            except:
                pass
            try:
                self.driver.find_element(By.XPATH, '//input[@value="3次"]').click()
                delay()
                return
            except:
                pass
            try:
                self.driver.find_element(By.XPATH, '//input[@value="2次"]').click()
                delay()
                return
            except:
                pass
            try:
                self.driver.find_element(By.XPATH, '//input[@value="1次"]').click()
                delay()
                return
            except:
                pass

        elif button_str == '全':
            if args[0] == '游骑兵':
                if len(args) == 1:
                    self.driver.find_element(By.XPATH,
                                             '//input[@id="moped"]/following-sibling::input[@type="button"]').click()
                elif len(args) == 2:
                    soldiers = self.driver.find_element(By.ID, soldier_type[0])
                    soldiers.send_keys(args[1])
                else:
                    logger.error('ERROR arges, pls check!')

            elif args[0] == '连环马':
                if len(args) == 1:
                    self.driver.find_element(By.XPATH,
                                             '//input[@id="tiger"]/following-sibling::input[@type="button"]').click()
                elif len(args) == 2:
                    soldiers = self.driver.find_element(By.ID, soldier_type[1])
                    soldiers.send_keys(args[1])
                else:
                    logger.error('ERROR arges, pls check!')

            elif args[0] == '金枪手':
                if len(args) == 1:
                    self.driver.find_element(By.XPATH,
                                             '//input[@id="heavy"]/following-sibling::input[@type="button"]').click()
                elif len(args) == 2:
                    soldiers = self.driver.find_element(By.ID, soldier_type[2])
                    soldiers.send_keys(args[1])
                else:
                    logger.error('ERROR arges, pls check!')

            elif args[0] == '短刀手':
                if len(args) == 1:
                    self.driver.find_element(By.XPATH,
                                             '//input[@id="infantry"]/following-sibling::input[@type="button"]').click()
                elif len(args) == 2:
                    soldiers = self.driver.find_element(By.ID, soldier_type[3])
                    soldiers.send_keys(args[1])
                else:
                    logger.error('ERROR arges, pls check!')

            elif args[0] == '弓箭手':
                if len(args) == 1:
                    self.driver.find_element(By.XPATH,
                                             '//input[@id="crossbow"]/following-sibling::input[@type="button"]').click()
                elif len(args) == 2:
                    soldiers = self.driver.find_element(By.ID, soldier_type[4])
                    soldiers.send_keys(args[1])
                else:
                    logger.error('ERROR arges, pls check!')

            elif args[0] == '长枪兵':
                if len(args) == 1:
                    self.driver.find_element(By.XPATH,
                                             '//input[@id="marines"]/following-sibling::input[@type="button"]').click()
                elif len(args) == 2:
                    soldiers = self.driver.find_element(By.ID, soldier_type[5])
                    soldiers.send_keys(args[1])
                else:
                    logger.error('ERROR arges, pls check!')

            elif args[0] == '撞城槌':
                if len(args) == 1:
                    self.driver.find_element(By.XPATH,
                                             '//input[@id="punching"]/following-sibling::input[@type="button"]').click()
                elif len(args) == 2:
                    soldiers = self.driver.find_element(By.ID, soldier_type[6])
                    soldiers.send_keys(args[1])
                else:
                    logger.error('ERROR arges, pls check!')

            elif args[0] == '轰天雷':
                if len(args) == 1:
                    self.driver.find_element(By.XPATH,
                                             '//input[@id="catapult"]/following-sibling::input[@type="button"]').click()
                elif len(args) == 2:
                    soldiers = self.driver.find_element(By.ID, soldier_type[7])
                    soldiers.send_keys(args[1])
                else:
                    logger.error('ERROR2: arges error, pls check!')

            elif args[0] == '探马':
                if len(args) == 1:
                    self.driver.find_element(By.XPATH,
                                             '//input[@id="scout"]/following-sibling::input[@type="button"]').click()
                elif len(args) == 2:
                    soldiers = self.driver.find_element(By.ID, soldier_type[8])
                    soldiers.send_keys(args[1])
                else:
                    logger.error('ERROR2: arges error, pls check!')

            elif args[0] == '工匠手':
                if len(args) == 1:
                    self.driver.find_element(By.XPATH,
                                             '//input[@id="sapper"]/following-sibling::input[@type="button"]').click()
                elif len(args) == 2:
                    soldiers = self.driver.find_element(By.ID, soldier_type[9])
                    soldiers.send_keys(args[1])
                else:
                    logger.error('ERROR2: arges error, pls check!')
            logger.info('点击按钮--全')

        elif button_str == '移动':
            self.driver.find_element(By.XPATH, '//input[@value="移动"]').click()
            logger.info('点击按钮--移动')

        elif button_str == '迁寨':
            self.driver.find_element(By.XPATH, "//input[@value='迁寨']").click()
            logger.info('点击按钮--迁寨')
            
        elif button_str == '查':
            self.driver.find_element(By.XPATH, "//input[@value='查']").click()
            logger.info('点击按钮--查')

        elif button_str == '确定':
            self.driver.find_element(By.XPATH, "//input[@value='确定']").click()
            logger.info('点击按钮--确定')

        elif button_str == '发送':
            self.driver.find_element(By.XPATH, "//input[@value='发送']").click()
            logger.info('点击按钮--发送')

        elif button_str == '清除':
            self.driver.find_element(By.XPATH, "//input[@value='清除']").click()
            logger.info('点击按钮--清除')

        elif button_str == '使用':
            self.driver.find_element(By.XPATH, "//input[@value='使用']").click()
            logger.info('点击按钮--使用')

        elif button_str == '买给自己':
            self.driver.find_element(By.XPATH, "//input[@value='买给自己']").click()
            logger.info('点击按钮--买给自己')

        elif button_str == '报名':
            self.driver.find_element(By.XPATH, "//input[@value='报名']").click()
            logger.info('点击按钮--报名')
                
        else:
            logger.error('ERROR1: arges error, pls check!')
        delay()

    def click_button(self, button_str, *args):
        try:
            index = self.click_button2(button_str, *args)
        except FunctionTimedOut as e:
            logger.info(e)
            self.driver.back()
            logger.info('刷新页面')
            self.click_button2(button_str, *args)

    # # 输入兵种数量
    # def SoldierNumbers(driver, Soldiers, type):
    # 	# 填写出兵数量
    # 	soldiers = driver.find_element(By.ID, type)
    # 	soldiers.send_keys(Soldiers)

    def select_mode_of_battle(self, attack_type):
        select_a = self.driver.find_element(By.XPATH, '//select[@name="wartype"]')
        select = Select(select_a)
        if attack_type == '歼灭':
            select.select_by_value('1')
        elif attack_type == '增援':
            select.select_by_value('2')
        elif attack_type == '劫掠':
            select.select_by_value('3')
        elif attack_type == '侦察':
            select.select_by_value('4')
        else:
            logger.error('ERROR3: args error, pls check!')

    # 获取并处理时间
    def get_page_time(self):
        # 获取时间
        page_source = str(self.driver.page_source)
        # 定义匹配的正则表达式
        pattern = r'行军时间\s+(\d+:\d+:\d+)'

        # 进行匹配
        match = re.search(pattern, page_source)

        # 如果匹配成功，则输出匹配的结果
        if match:
            marching_time = match.group(1)
            logger.info(f'marching_path_time:{marching_time}', marching_time)
            return marching_time
        else:
            logger.error("未匹配到结果")

    def select_city(self, location_x, location):
        self.location_x(location_x)
        location = '//a[contains(@href, "' + location + '")]'
        logger.info(location)
        self.driver.find_element(By.XPATH, location).click()
        delay()

    # 定位
    def location_x(self, location_x):
        try:
            self.driver.find_element(By.XPATH, '//input[@name="x"]').send_keys(location_x)
            self.click_button('移动')
            delay()
        except NoSuchElementException:
            self.driver.refresh()
            self.driver.find_element(By.XPATH, '//input[@name="x"]').send_keys(location_x)
            delay()
            self.click_button('移动')

    def location_name(self, name_str):
        try:
            self.driver.find_element(By.XPATH, '//input[@name="kingname"]').send_keys(name_str)
            self.click_button('查')
        except NoSuchElementException:
            self.driver.refresh()
            self.driver.find_element(By.XPATH, '//input[@name="kingname"]').send_keys(name_str)
            self.click_button('查')

    def select_man(self, man_type):
        if_ready = self.if_man_ready()
        if if_ready == 'yes':
            return 'yes'
        else:
            man_type = '//a[contains(text(),"' + man_type + '")]'
            # manType = '//a[contains(text(), "声望型")]'
            for i in range(0, 3):
                try:
                    element = self.driver.find_element(By.XPATH, man_type)
                    parent_element = element.find_element(By.XPATH, '..')
                    child_elements = parent_element.find_elements(By.XPATH, '*')
                    current_index = child_elements.index(element)
                    previous_element = child_elements[current_index - 2]
                    previous_element.click()
                    delay()
                    logger.info('成功招募一个')
                    self.click_word('返回')
                    delay()
                    if_ready = self.if_man_ready()
                    if if_ready == 'yes':
                        return 'yes'
                    else:
                        continue
                except NoSuchElementException:
                    logger.info('没有了')
        return 'no'

    def if_man_ready(self):
        # 查找页面中是否包含指定文字
        # try:
        # 	element = self.driver.find_element(By.XPATH, "//*[contains(text(), '使用招贤榜选将可立即刷出新武将,每天零点系统也会自动刷出新武将')]")
        # 	return 'yes'
        # except NoSuchElementException:
        # 	return 'no'
        # 获取行军时间
        page_source = str(self.driver.page_source)
        # 定义匹配的正则表达式
        pattern = r'已有武将30个,还可招募0个.'

        # 进行匹配
        match = re.search(pattern, page_source)

        # 如果匹配成功，则输出匹配的结果
        if match:
            return 'yes'
        else:
            return 'no'

    def select_beauties(self):
        # star_level = '★★★★★★' # 设置需要查找的星级
        # star_level2 = '★★★★★'
        try:
            link = self.driver.find_element(By.XPATH, "//text()[contains(., '星级:★★★★★ ')]/following-sibling::a")
            link.click()
            delay()
            logger.info('招募到五星妞')
        except NoSuchElementException:
            try:
                link = self.driver.find_element(By.XPATH, "//text()[contains(., '星级:★★★★★★ ')]/following-sibling::a")
                link.click()
                delay()
                logger.info('招募到六星妞')
            except NoSuchElementException:
                # print('本页没有5、6星美女！')
                return 'no'

    def if_beauty_ready(self):
        page_source = str(self.driver.page_source)
        # 定义匹配的正则表达式
        pattern = r'还可容纳0人'

        # 进行匹配
        match = re.search(pattern, page_source)

        # 如果匹配成功，则输出匹配的结果
        if match:
            return 'yes'
        else:
            return 'no'

    # 找文字节点后的链接，变向验证本页是否有该文本节点
    def find_text(self):
        try:
            self.driver.find_element(By.XPATH,
                                     "//text()[contains(., '还可容纳0人')]/following-sibling::a")
            return 'yes'
        except NoSuchElementException:
            return 'no'

    def select_which_man_battle(self, value):
        which_man = self.driver.find_element(By.XPATH, "//select[@name='generalid']")
        select = Select(which_man)
        try:
            select.select_by_value(value)
        except NoSuchElementException:
            logger.error('错误？')

    # 定位链接元素
    def locate_a(self, element_type, *args):
        if element_type == 'LINK_TEXT':
            try:
                links = self.driver.find_elements(By.LINK_TEXT, args[0])
                return len(links)
            except NoSuchElementException:
                return 0

        elif element_type == 'PARTIAL_LINK_TEXT':
            try:
                links = self.driver.find_elements(By.PARTIAL_LINK_TEXT, args[0])
                return links
            except NoSuchElementException:
                logger.error('locate_a error!')
                return 0

        elif element_type == 'all':
            city_list = []
            links = self.driver.find_elements(By.XPATH, "//a[starts-with(@href,'selectKings.php')]")
            logger.info(f'该账号小号数量：{len(links)}')
            for link in links:
                city_name = link.text
                city_list.append(city_name)
            return city_list

        elif element_type == '0':
            links = "//a[starts-with(@href,'" + args[0] + "')]"
            self.driver.find_element(By.XPATH, links).click()
            delay()

            # elif element_type == 'CHECK':
            city_information_dir = {}
            # index = 0
            # # 处理坐标
            # string = str(self.driver.page_source)
            # pattern = r"规模：\d+\((\d+),\d+\)"
            # city_location_list = re.findall(pattern, string)
            # logger.info(city_location_list)
            #
            # need_str = "//a[starts-with(@href,'" + args[0] + "')]"
            # links = self.driver.find_elements(By.XPATH, need_str)
            # for link in links:
            #     city_name = link.text
            #     city_information_dir[city_name] = city_location_list[index]
            #     index = index + 1
            # logger.info(city_information_dir)
            # f = open('xixi.csv', mode='a', encoding='utf-8', newline='')
            # csv_writer.writerow(city_information_dir)

        elif element_type == 'Man':
            man_list = []
            man_information_dict = {}
            index = 1
            for j in range(0, args[0]):
                print('----------', j + 1, '----------')
                page_source = str(self.driver.page_source)
                matches = re.findall(r'\d+\.\d+%', page_source)
                for i in range(0, 10):
                    print(i + 1)
                    link = self.driver.find_elements(By.XPATH, "//a[starts-with(@href,'getgeneralinfo.php?')]")[i]
                    man_name = link.text
                    man_name_list = [man_name + ' | ' + matches[i]]
                    link.click()
                    time.sleep(0.35)
                    city_name = self.driver.find_element(By.XPATH, "//a[starts-with(@href,'getkinginfo.php?')]").text
                    if city_name in man_information_dict:
                        man_information_dict[city_name].append(man_name_list[0])
                    else:
                        man_information_dict[city_name] = man_name_list
                    time.sleep(0.35)

                    self.driver.back()
                    index = index + 1
                self.driver.find_element(By.XPATH, "//input[@name='pageno']").send_keys(j + 2)
                self.click_button('确定')
            return man_information_dict
        elif element_type == '山寨':
            str_ = "//a[contains(@href,'" + args[0] + "')]"
            self.driver.find_element(By.XPATH, str_).click()
            delay()

    def in_put(self, type_str, *args):
        if type_str == 'player':
            self.driver.find_element(By.XPATH, "//input[@name='kingname']").send_keys(args[0])

        elif type_str == 'man':
            self.driver.find_element(By.XPATH, "//input[@name='generalname']").send_keys(args[0])

        elif type_str == 'beauties':
            self.driver.find_element(By.XPATH, "//input[@name='beautyname']").send_keys(args[0])

    def del_player_information(self, city_str):
        city_names_list = []
        city_information_dict = {}
        index = 0
        # 处理免战时间

        # 处理坐标
        string = str(self.driver.page_source)
        pattern = r"\((\d+),\d+\)"
        matches = re.findall(pattern, string)

        links = self.driver.find_elements(By.XPATH, "//a[starts-with(@href,'../map/mapgetonemap.php?')]")
        for i in range(0, len(links)):
            city_name = city_str + ' | ' + links[i].text
            city_names_list.append(city_name)
            # temp_city_name_list = [matches[index]]
            temp_city_name_list = matches[index]
            links[i].click()

            s = str(self.driver.page_source)
            match = re.search(r'免战到期:(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', s)
            if match:
                # wall_lsit = [match.group()]
                wall_lsit = match.group()
            else:
                # wall_lsit = ['0000-00-00 00:00:00']
                wall_lsit = '0000-00-00 00:00:00'
            self.driver.back()
            delay()
            index = index + 1
            # city_information_dict[city_name] = temp_city_name_list
            city_information_dict[city_name] = wall_lsit
        logger.info(city_information_dict)
        return city_information_dict

    def del_hills(self, location_x):
        # logger.info('513')
        links = self.driver.find_elements(By.XPATH, "//a[starts-with(@href,'mapgetonemap.php?t=')]")
        logger.info(len(links))
        for i in range(0, 8):
            if links[i].text == links[i + 1].text == links[i + 2].text == '荒山':
                logger.info(f'location:{location_x}, {i}')
                links[i + 1].click()
                delay()
                self.click_word('迁寨')
                self.click_button('迁寨')
                self.click_word('首页')
                self.click_word('系统')
                self.click_word('切换好汉')
                return 'yes'
        text_1 = links[9].text
        if text_1 == '荒山':
            self.location_x(location_x + 1)
            links = self.driver.find_elements(By.XPATH, "//a[starts-with(@href,'mapgetonemap.php?t=')]")
            text_2 = links[0].text
            text_3 = links[1].text
            if text_2 == text_3 == '荒山':
                links[0].click()
                delay()
                self.click_word('迁寨')
                self.click_button('迁寨')
                self.click_word('首页')
                self.click_word('系统')
                self.click_word('切换好汉')
                return 'yes'
        return location_x + 1

    # 选择服务器
    def select_sh(self, index):
        self.driver.find_elements(By.XPATH, "//a[starts-with(@href,'http://sh')]")[index - 1].click()

    # 输入账号密码
    def input_acc_pass(self, lista, listp):
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(lista)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(listp)

    # 定位自己的坐标
    def location_mine(self):
        page_source = str(self.driver.page_source)
        pattern = r'坐标:(\d+)\|(\d)'
        match = re.search(pattern, page_source)
        if match:
            coord1 = int(match.group(1))
            coord2 = int(match.group(2))
            logger.info(f'本城坐标:{coord1}/{coord2}')
            return coord1, coord2

    def find_battled_cities(self):
        links = self.driver.find_elements(By.XPATH, "//a[starts-with(@href,'mapgetonemap.php?t')]")
        # location_hills = 0
        # for link in links:
        #     if link.text == '荒山':
        #         location_hills = location_hills + 1

        len_link = len(links)
        logger.info(len_link)
        if len_link == 0:
            return
        else:
            for i in range(0, len_link):
                links = self.driver.find_elements(By.XPATH, "//a[starts-with(@href,'mapgetonemap.php?t')]")
                if links[i].text != '荒山' and links[i].text != '贫木县' and links[i].text != '贫铁县' and links[i].text != '贫粮县' and links[i].text != '贫石县' and links[i].text != '中粮铁县' and links[i].text != '中粮石县' and links[i].text != '中粮木县' and links[i].text != '富粮县':
                    links[i].click()
                    delay()
                    page_source = str(self.driver.page_source)
                    match = re.search(r'\d{2}-\d{2}', page_source)
                    if match:
                        date = match.group()
                        if date == '04-29':
                            page_source2 = str(self.driver.page_source)
                            match2 = re.search(r'\d+/\d+', page_source2)
                            if match2:
                                date2 = match2.group()
                                with open('被打的城坐标.txt', 'a+') as f:
                                    f.write(date2)
                                    f.write('\n')
                        self.driver.back()
                        delay()
                    else:
                        logger.info('不是城市')
                        self.driver.back()
                        delay()
        # logger.info(location_hills)
        # return location_hills

    # 查看分寨数量
    def city_number(self):
        self.locate_a('0', 'getowninfo.php?t=')
        page_source = str(self.driver.page_source)
        self.click_word('首页')
        pattern = r'\d+(?=寨)'
        match = re.search(pattern, page_source)
        if match:
            num = int(match.group())
            return num

    # 查看士兵数量

    # 出兵
    def chu_bin(self, time_list):
        self.click_word('新的')
        self.click_word('出兵')
        try:
            self.click_button('全', '游骑兵')
            self.select_mode_of_battle('劫掠')
            self.click_button('出征')
            marching_time = self.get_page_time()
            path_time = del_path_time(marching_time) * 2
            time_list.append(path_time)
            self.click_button('普通出征')
        except:
            logger.error('出兵失败！')
            self.click_word('首页')
        self.click_word('资源')
        self.click_word('一键建造资源')
        self.click_word('首页')

    # 获取寨主名
    def get_maincity_name(self):
        link = self.driver.find_element(By.XPATH, "//a[starts-with(@href,'getowninfo.php?')]")
        name_ = link.text
        logger.info(f'当前寨主{name_}')
        return name_

    # 判断文字是否存在 
    def is_text_exit(self, text):
        page_source = str(self.driver.page_source)
        pattern = text
        match = re.search(pattern, page_source)
        if match:
            logger.info(f'发现{text}')
            return 1
        else:
            logger.info(f'未发现{text}')
            return 0

    # 判断本寨士兵数量 
    def shi_bin_num(self):
        page_source = str(self.driver.page_source)
        pattern = r'本寨士兵</a>:(\d+)'
        match = re.search(pattern, page_source)
        if match:
            numbers = int(match.group(1))
            logger.info(f'本寨有士兵: {numbers}')
            # logger.info('successful')
            return numbers
        else:
            logger.error('ERROR, pls check')

    # 判断资源数量
    def resource_num(self, resource_type):
        page_source = str(self.driver.page_source)
        pattern = resource_type + r':-?(\d+)'
        logger.info(pattern)
        match = re.search(pattern, page_source)
        if match:
            numbers = int(match.group(1))
            logger.info(f'当前寨子{resource_type}剩余: {numbers}')
            return numbers
        else:
            logger.info(f'匹配{resource_type}数量失败！')
            logger.error('==========ERROR==========ERRROR==========')
            page_source = str(self.driver.page_source)
            logger.debug(page_source)
            logger.error('==========ERROR==========ERRROR==========')
            delay(100000)
            return -100

    # 判断城寨规模
    def city_gui_mo(self):
        page_source = str(self.driver.page_source)
        pattern = r'规模：(\d+)'
        match = re.search(pattern, page_source)
        if match:
            numbers = int(match.group(1))
            logger.info(f'目标山寨规模: {numbers}')
            # logger.info('successful')
            return numbers
        else:
            logger.error('ERROR, pls check')


    # 判断建筑等级
    def jian_zhu_level(self, type_jian_zhu):
        page_source = str(self.driver.page_source)
        pattern = type_jian_zhu + r'</a>\s*(\d+)'
        match = re.search(pattern, page_source)
        if match:
            level = int(match.group(1))
            logger.info(f'{type_jian_zhu}的等级为{level}')
            return level
        else:
            logger.info('匹配等级失败，请检查')
            return -1

    def xuan_ze_wujiang(self, partStr):
        a = base.driver.find_element(By.XPATH, "//select[@id='generalid']")
        select = Select(a)
        options = select.options
        for option in options:
            if partStr in option.text:
                option.click()
                break

    def yan_zhen(self):
        if os.path.exists('image.png'):
            os.remove('image.png')
            print('删除成功')
        else:
            print('未发现文件')
        self.driver.save_screenshot('E:/image/image.png') # 截取整个DOC
        ce = self.driver.find_element_by_id("captcha_img")  # 具体的id要用F12自行查看
        left = ce.location['x']
        top = ce.location['y']
        right = ce.size['width'] + left
        height = ce.size['height'] + top
        im = Image.open("E:/image/image.png")
        img = im.crop((left, top, right, height))
        img.save('image.png')  # 这里就是截取到的验证码图片
        view = YdmVerify()
        passStr = view.shibie('image.png')
        print(passStr)
        self.driver.find_element(By.XPATH, "//input[@name='authcode']").send_keys(passStr)
        
    def shen_zi_yuan(self):
        page_source = str(self.driver.page_source)
        pattern = r'(\d+)级'
        match = re.findall(pattern, page_source)
        if match:
            logger.info('True')
        else:
            print('Wrong')
        index = 0
        minN = int(match[0])
        for i in range(1, len(match)):
            if int(match[i]) < minN:
                index = i
                minN = int(match[i])
            else:
                pass
        self.click_word('升', index)




def del_path_time(time_str):
    # 处理行军时间 --<start>--
    _str = time_str
    _str = _str.split(':')
    hour = int(''.join(_str[0]))
    minutes = int(''.join(_str[1]))
    sec = int(float(''.join(_str[2])))
    del_time = hour * 60 * 60 + minutes * 60 + sec
    return del_time


# --<end>--

def time_after(time_num):
    while time_num > 0:
        logger.debug(f'倒计时: {time_num}s')
        delay(1)
        time_num = time_num - 1
    return




class YdmVerify(object):
    _custom_url = "http://api.jfbym.com/api/YmServer/customApi"
    _token = "pHKj4PcSHi3qgMQhq_pUUJ31LXdFBmq3yaDQVhnwK8M"
    _headers = {
        'Content-Type': 'application/json'
    }
    def common_verify(self, image, verify_type="10110"):
        payload = {
            "image": base64.b64encode(image).decode(),
            "token": self._token,
            "type": verify_type
        }
        resp = requests.post(self._custom_url, headers=self._headers, data=json.dumps(payload))
        print(resp.text)
        return resp.json()['data']['data']

    def shibie(self, path):
        with open(path, 'rb') as f:
            image = f.read()
        a = self.common_verify(image, '10110')
        return a




# if __name__ == "__main__":
#     base = Base()
#     base.config(1)
#     base.driver.get('http://sh27.caihonger.com/master.php?a=3951&t=31229326645132041942&u=VVR0ZE0xWTU_c&k=26985&c=0')
#     delay()
#     base.click_word('首页')
#     base.click_word('资源')
#     base.shen_zi_yuan()
#     base.driver.close()
    # delay(40)
    # a = base.jian_zhu_level('仓　库')
    # logger.debug(a)
    # base.driver.quit()
    # base.locate_a('0', '../beauty/selectbeauty.php?t=')
    # delay(100)
