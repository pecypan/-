from BasePartDLL import *
from autoResourse import sheng_jian_zhu

yijian = '&type=onekey'
removestr = 'master.php?t'
tasklist = ['resource/resourceautobuild.php?t','building/buildingList.php?t&t','tasks/randomReward.php?t=7484&t','']

def up_resource(url_list):
    base = Base()
    base.config(0)
    while True:
        for index in range(0, len(url_list)):
            print(f'**********[{index + 1}]**********')
            base.driver.get(url_list[index])
            delay(0.35)
            num = base.city_number()
            if num >= 11:
                url3 = list(url_list[index])
                url3[len(url3)-1] = 1
                url3.append(num-11)
                url3 = ''.join(str(x) for x in url3)
                # print(url3, type(url3))
                base.driver.get(url3)
                delay(0.3)
            else:
                url3 = list(url_list[index])
                url3[len(url3)-1] = num - 1
                url3 = ''.join(str(x) for x in url3)
                # print(url3, type(url3))
                base.driver.get(url3)
                delay(0.3)
            url1 = url3.replace(removestr, tasklist[0]) + yijian
            url2 = url3.replace(removestr, tasklist[1])
            base.driver.get(url1)
            delay(0.35)
            base.click_word('返回')
            base.shen_zi_yuan()
            base.driver.get(url2)
            delay(0.35)
            level1 = base.jian_zhu_level('仓　库')
            level2 = base.jian_zhu_level('粮　库')
            print(f'No:{index + 1}仓库等级 ==> {level1}')
            print(f'No:{index + 1}粮库等级 ==> {level2}')
            if level2 < level1 <= 7:
                base.locate_a('0', 'liangku.php?')
                base.click_word('升级')
                base.click_word('首页')

                # ---------------------------
                # ---------------------------
                num = base.city_number()
                if num <= 1:
                    continue
                print(f'当前有{num}寨')
                base.locate_a('0', 'getowninfo.php?t=')
                sheng_jian_zhu(num, base, index, url_list[index])
                # ---------------------------
                # ---------------------------

            elif level1 <= level2 < 7:
                base.locate_a('0', 'cangku.php?')
                base.click_word('升级')
                base.click_word('首页')
                num = int(base.city_number())
                print(f'当前有{num}寨')
                base.locate_a('0', 'getowninfo.php?t=')
                sheng_jian_zhu(num, base, index, url_list[index])
            else:
                level1 = base.jian_zhu_level('军　营')
                level2 = base.jian_zhu_level('聚义厅')
                print(f'No:{index + 1}军营等级 ==> {level1}')
                print(f'No:{index + 1}聚义厅等级 ==> {level2}')
                if level1 < 15:
                    base.locate_a('0', 'junying.php?')
                    base.click_word('升级')
                    base.click_word('首页')

                    num = int(base.city_number())
                    print(f'当前有{num}寨')
                    base.locate_a('0', 'getowninfo.php?t=')
                    if level1 < 10:
                        sheng_jian_zhu(num, base, index, url_list[index])
                    else:
                        sheng_jian_zhu(num, base, index, url_list[index])

                elif level2 < 15:
                    base.locate_a('0', 'juyiting.php?')
                    base.click_word('升级')
                    base.click_word('首页')
                    num = int(base.city_number())
                    print(f'当前有{num}寨')
                    base.locate_a('0', 'getowninfo.php?t=')
                    sheng_jian_zhu(num, base, index, url_list[index])

                else:
                    base.driver.get(url1)
                    delay(0.35)
                    base.click_word('返回')
                    base.shen_zi_yuan()
                    base.driver.get(url2)
                    delay(0.35)
                    base.locate_a('0', 'jishi.php')
                    base.click_word('升级')
                    base.click_word('首页')
                    num = int(base.city_number())
                    print(f'当前有{num}寨')
                    base.locate_a('0', 'getowninfo.php?t=')
                    sheng_jian_zhu(num, base, index, url_list[index])
        # return
    return


if __name__ == '__main__':
    url = [
        'http://sh27.caihonger.com/master.php?t=72005776136166818801&u=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=92132&c=0'       , # 喻松歆
        'http://sh27.caihonger.com/master.php?t=72005776136166818801&u=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=92133&c=0'       , # 姜辉彦
        'http://sh27.caihonger.com/master.php?t=1644045681&u=VW1nS1pGRTlWVFpUUFFCcFhHUUZZQU0z&k=10768&c=0'                              , # 海尚友
        'http://sh27.caihonger.com/master.php?t=72005776136166818801&u=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=19428&c=0'       , # 于鲲策
        'http://sh27.caihonger.com/master.php?t=6691&t=72005776136166818801&u=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=19429&c=0', # 佟珺玥
        'http://sh27.caihonger.com/master.php?t=72005776136166818801&u=Vm1sY01sVTVCbUFHWjEwM0FUOVVNd0V5VURnSGJnPT0_c&k=92139&c=0'       , # 谯范濮
        'http://sh27.caihonger.com/master.php?t=7051&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92039&c=0', # 郭嘉
        'http://sh27.caihonger.com/master.php?t=8931&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92036&c=0', # 徐盛
        'http://sh27.caihonger.com/master.php?t=2997&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92041&c=0', # 愚人众
        'http://sh27.caihonger.com/master.php?t=3374&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92032&c=0', # 济北相鲍信
        'http://sh27.caihonger.com/master.php?t=1848&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92035&c=0', # 东莱太史慈
        'http://sh27.caihonger.com/master.php?t=4799&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92037&c=0', # 谋黄忠
        'http://sh27.caihonger.com/master.php?t=2140&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92034&c=0', # 北辰之威
        'http://sh27.caihonger.com/master.php?t=9716&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92038&c=0', # 神荀彧
        'http://sh27.caihonger.com/master.php?t=9328&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92040&c=0', # 丘丘人
        'http://sh27.caihonger.com/master.php?t=5243&t=81466666722801424776&u=QVQ0QmJ3SnVWakFIWmd4bURUTlJOZ2s2QzJzRFl3PT0_c&k=92031&c=0', # 蜀郡张松
        'http://sh27.caihonger.com/master.php?t=1644045681&u=VW1nS1pGRTlWVFpUUFFCcFhHUUZZQU0z&k=10770&c=0'                              , # 鞠喆珺
        'http://sh27.caihonger.com/master.php?t=1876&t=1644045681&u=VW1nS1pGRTlWVFpUUFFCcFhHUUZZQU0z&k=10771&c=0'                       , # 夏侯畅松
        'http://sh27.caihonger.com/master.php?t=7257&t=1644045681&u=VW1nS1pGRTlWVFpUUFFCcFhHUUZZQU0z&k=10774&c=0'                       , # 蒯童军
        'http://sh27.caihonger.com/master.php?t=1644045681&u=VW1nS1pGRTlWVFpUUFFCcFhHUUZZQU0z&k=10777&c=0'                              , # 童言顺
        ]


    up_resource(url)
