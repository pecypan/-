from BasePartDLL import *

yijian = '&type=onekey'
removestr = 'master.php?t'
tasklist = ['resource/resourceautobuild.php?t','building/buildingList.php?a&t','tasks/randomReward.php?a=7484&t','']


def sheng_jian_zhu(num, base, index, url):
    for i in range(num):
        url = list(url)
        url[len(url)-1] = i
        url_need = ''.join(str(x) for x in url)
        base.driver.get(url_need)
        delay(0.35)
        page_source = str(base.driver.page_source)
        patt = r'→'
        patter = re.compile(patt)
        result = patter.findall(page_source)
        if len(result) >= 2:
            logger.info('不需要升级!')
            continue
        url2 = url_need.replace(removestr, tasklist[0]) + yijian
        base.driver.get(url2)
        delay(0.35)
        base.click_word('返回')
        base.shen_zi_yuan()
        url3 = url_need.replace(removestr, tasklist[1])
        base.driver.get(url3)
        delay(0.35)
        level1 = base.jian_zhu_level('军　营')
        level2 = base.jian_zhu_level('聚义厅')
        logger.info(f'No:{index + 1}军营等级 ==> {level1}')
        logger.info(f'No:{index + 1}聚义厅等级 ==> {level2}')
        if level2 < 15 or level1 < 15:
            continue
        level3 = base.jian_zhu_level('集　市')
        if level3 < 10:
            base.locate_a('0', 'jishi.php?')
            base.click_word('升级')
            continue
        level_cangku = base.jian_zhu_level('仓　库')
        level_liangku = base.jian_zhu_level('粮　库')
        if level_cangku <= level_liangku <= 15:
            base.locate_a('0', 'cangku.php?')
            base.click_word('升级')
            continue
        elif level_liangku < level_cangku <= 15:
            base.locate_a('0', 'liangku.php?')
            base.click_word('升级')
            continue
        level_xuanxiulang = base.jian_zhu_level('选秀廊')
        if level_xuanxiulang < 15:
            base.locate_a('0', '../beauty/selectbeauty.php?t=')
            base.click_word('升级')
            continue
        level_houxiangfang = base.jian_zhu_level('后厢房')
        if level_houxiangfang < 15:
            base.locate_a('0', '../beauty/viewbeauty.php?')
            base.click_word('升级')
            continue
        level_dianjiangtai = base.jian_zhu_level('点将台')
        if level_dianjiangtai < 15:
            base.locate_a('0', 'dianjiangtai.php?')
            base.click_word('升级')
            continue
        level_dijiao = base.jian_zhu_level('地　窖')
        if level_dijiao < 15:
            base.locate_a('0', 'dijiao.php?')
            base.click_word('升级')
            continue
        level_zhaiqiang = base.jian_zhu_level('寨　墙')
        if level_zhaiqiang < 15:
            base.locate_a('0', 'zhaiqiang.php?')
            base.click_word('升级')
            continue
        base.click_word('一键')

            
def up_resource(url_):
    base = Base()
    base.config(1)
    base.driver.get(url_)
    delay()
    city_list = base.locate_a('all')
    index = 1
    for city in city_list:
        base.click_word(city)
        base.click_word('建筑')
        page_source = str(base.driver.page_source)
        pattern1 = r'仓　库</a>\s*(\d+)'
        pattern2 = r'粮　库</a>\s*(\d+)'
        match1 = re.search(pattern1, page_source)
        # logger.info(match1)
        match2 = re.search(pattern2, page_source)
        # logger.info(match2)
        if match1:
            if match2:
                level1 = int(match1.group(1))
                level2 = int(match2.group(1))
                logger.info(f'No:{index}仓库等级 ==> {level1}')
                logger.info(f'No:{index}粮库等级 ==> {level2}')
                if level2 < level1 < 20:
                    # base.locate_a('0', 'cangku.php?')
                    base.locate_a('0', 'liangku.php?')
                    base.click_word('升级')

                    base.click_word('首页')
                    num = int(base.city_number())
                    logger.info(f'当前有{num}寨')
                    if num == 1:
                        base.click_word('首页')
                        base.click_word('系统')
                        base.click_word('切换')
                        pass
                    else:
                        base.click_word('首页')
                        base.click_word('系统')
                        base.click_word('切换')
                        pass
                        # sheng_jian_zhu(num, base)

                elif level1 <= level2 and level1 < 20:
                    base.locate_a('0', 'cangku.php?')
                    base.click_word('升级')

                    base.click_word('首页')
                    num = int(base.city_number())
                    logger.info(f'当前有{num}寨')
                    if num == 1:
                        base.click_word('首页')
                        base.click_word('系统')
                        base.click_word('切换')
                        pass
                    else:
                        base.click_word('首页')
                        base.click_word('系统')
                        base.click_word('切换')
                        pass
                        # sheng_jian_zhu(num, base)
                else:
                    page_source = str(base.driver.page_source)
                    pattern1 = r'军　营</a>\s*(\d+)'
                    pattern2 = r'聚义厅</a>\s*(\d+)'
                    match1 = re.search(pattern1, page_source)
                    match2 = re.search(pattern2, page_source)
                    if match1:
                        if match2:
                            level1 = int(match1.group(1))
                            level2 = int(match2.group(1))
                            logger.info(f'No:{index}军营等级 ==> {level1}')
                            logger.info(f'No:{index}聚义厅等级 ==> {level2}')
                            if level1 < 3:
                                # base.locate_a('0', 'cangku.php?')
                                base.locate_a('0', 'junying.php?')
                                base.click_word('升级')

                                base.click_word('首页')
                                num = int(base.city_number())
                                logger.info(f'当前有{num}寨')
                                if num == 1:
                                    base.click_word('首页')
                                    base.click_word('系统')
                                    base.click_word('切换')
                                    pass
                                else:
                                    base.click_word('首页')
                                    base.click_word('系统')
                                    base.click_word('切换')
                                    pass
                                    # sheng_jian_zhu(num, base)
                            elif level1 < 15:
                                base.locate_a('0', 'junying.php?')
                                base.click_word('升级')

                            elif level2 < 2:
                                base.locate_a('0', 'juyiting.php?')
                                base.click_word('升级')

                                base.click_word('首页')
                                num = int(base.city_number())
                                logger.info(f'当前有{num}寨')
                                if num == 1:
                                    base.click_word('首页')
                                    base.click_word('系统')
                                    base.click_word('切换')
                                    pass
                                else:
                                    sheng_jian_zhu(num, base)

        index = index + 1
    


if __name__ == '__main__':
    url = 'http://sh27.caihonger.com/selectKings.php?c=0&u=RGxwZmMxOXFVakpUTTFzd0NEaFhNVlJpQ204RlpsWmpBakZRYWxKcg_c_c&t=13832862066228872509'
    # list_A = ['d20']
    # list_P = ['720712']
    while True:
        time_delay = up_resource(url)
        time_after(360)
