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
            if level2 < level1 <= 20:
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

            elif level1 <= level2 < 20:
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
        'http://sh29.caihonger.com/master.php?t=2291&t=50828153549436911439&u=QUQ4TVlnVnBBbVJiT2x3MkN6VlhNQUV5QjJjRVpnPT0_c&k=6764&c=0',
        'http://sh29.caihonger.com/master.php?t=8705&t=50828153549436911439&u=QUQ4TVlnVnBBbVJiT2x3MkN6VlhNQUV5QjJjRVpnPT0_c&k=6766&c=0',
        'http://sh29.caihonger.com/master.php?t=9578&t=50828153549436911439&u=QUQ4TVlnVnBBbVJiT2x3MkN6VlhNQUV5QjJjRVpnPT0_c&k=6767&c=0',
        'http://sh29.caihonger.com/master.php?t=2217&t=50828153549436911439&u=QUQ4TVlnVnBBbVJiT2x3MkN6VlhNQUV5QjJjRVpnPT0_c&k=6768&c=0',
        'http://sh29.caihonger.com/master.php?t=5988&t=50828153549436911439&u=QUQ4TVlnVnBBbVJiT2x3MkN6VlhNQUV5QjJjRVpnPT0_c&k=6769&c=0',
        'http://sh29.caihonger.com/master.php?t=9465&t=50828153549436911439&u=QUQ4TVlnVnBBbVJiT2x3MkN6VlhNQUV5QjJjRVpnPT0_c&k=6770&c=0',
        'http://sh29.caihonger.com/master.php?t=1402&t=50828153549436911439&u=QUQ4TVlnVnBBbVJiT2x3MkN6VlhNQUV5QjJjRVpnPT0_c&k=6771&c=0',
        'http://sh29.caihonger.com/master.php?t=4356&t=50828153549436911439&u=QUQ4TVlnVnBBbVJiT2x3MkN6VlhNQUV5QjJjRVpnPT0_c&k=6772&c=0',
        'http://sh29.caihonger.com/master.php?t=3730&t=50828153549436911439&u=QUQ4TVlnVnBBbVJiT2x3MkN6VlhNQUV5QjJjRVpnPT0_c&k=6773&c=0',
        'http://sh29.caihonger.com/master.php?t=9958&t=50828153549436911439&u=QUQ4TVlnVnBBbVJiT2x3MkN6VlhNQUV5QjJjRVpnPT0_c&k=6774&c=0',
        'http://sh29.caihonger.com/master.php?t=7059&t=61643553276718422733&u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&k=6765&c=0',
        'http://sh29.caihonger.com/master.php?t=7372&t=61643553276718422733&u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&k=6775&c=0',
        'http://sh29.caihonger.com/master.php?t=3328&t=61643553276718422733&u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&k=6776&c=0',
        'http://sh29.caihonger.com/master.php?t=9893&t=61643553276718422733&u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&k=6777&c=0',
        'http://sh29.caihonger.com/master.php?t=2113&t=61643553276718422733&u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&k=6778&c=0',
        'http://sh29.caihonger.com/master.php?t=1911&t=61643553276718422733&u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&k=6779&c=0',
        'http://sh29.caihonger.com/master.php?t=1502&t=61643553276718422733&u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&k=6780&c=0',
        'http://sh29.caihonger.com/master.php?t=6929&t=61643553276718422733&u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&k=6781&c=0',
        'http://sh29.caihonger.com/master.php?t=3242&t=61643553276718422733&u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&k=6782&c=0',
        'http://sh29.caihonger.com/master.php?t=2577&t=61643553276718422733&u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&k=6783&c=0',
        'http://sh29.caihonger.com/master.php?t=1928&t=61643553276718422733&u=VTJ3QWJsOHpBV2RiT2wwM0NqUllQd0F6VXpNRFlBPT0_c&k=6784&c=0'
        ]

    up_resource(url)
