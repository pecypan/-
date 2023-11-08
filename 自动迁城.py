from BasePartDLL import *

Location = 36044 # 起始区


# Location = 1
removestr = 'master.php?a'
tasklist = ['tasks/selectBaowu.php?level=5&t','tasks/dailyReward.php?a=9165&t','tasks/randomReward.php?a=7484&t','']

def read_csv2list():
    try:
        file = open(r'E:\红颜\AccAndPassWord.csv', 'r', encoding="gbk")  # 读取以utf-8
        context = file.read()  # 读取成str
        list_result = context.split("\n")  # 以回车符\n分割成单独的行
        # 每一行的各个元素是以【,】分割的，因此可以
        length = len(list_result)
        for i in range(length):
            list_result[i] = list_result[i].split(",")
        return list_result
    except Exception:
        print("文件读取转换失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close()  # 操作完成一定要关闭


def zi_dong_qian_chen(url_list):
    base = Base()
    base.config(0)
    for index in range(0, 2):
        logger.info(f'==========当前是第{index + 1}个书签===========')
        base.driver.get(url_list[index])
        delay()
        base.click_word('系统')
        base.click_word('切换')
        mainurl2 = base.driver.current_url
        city_list = base.locate_a('all')
        global Location
        for i in range(0, len(city_list)):
            base.click_word(city_list[i])
            mainurl = base.driver.current_url
            numbers = base.city_number()
            url = list(mainurl)
            for i in range(numbers):
                url[len(url)-1] = i
                url_need = ''.join(str(x) for x in url)
                base.driver.get(url_need)
                delay(0.3)
                print(f'{i+1}')
                base.click_word('地图')
                base.location_x(Location)
                a = base.del_hills(Location)
                if a == 'yes':
                    logger.info('迁寨成功!')
                else:
                    while a != 'yes':
                        Location = a
                        base.location_x(Location)
                        a = base.del_hills(Location)
            base.driver.get(mainurl2)
    base.driver.quit()

if __name__ == '__main__':
    # with open(r'E:\红颜\21服\小熊熊.txt', 'r+') as f:
    #     Url_list = f.readlines()
    #     # logger.info(Url_list)
    #     f.close()
    Url_list = [
        'http://sh31.caihonger.com/selectKings.php?u=RGpFQWFBZHVEMnhUTVExaFdtRUNZd0F5Vmo0RFpRPT0_c&t=62256098960617125657&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=VTJ3QWFGSTdWRGRXTkFGdFdtRlVOUU14Vno5U053PT0_c&t=58788822260315899553&c=0&t=58788822260315899553&u=VTJ3QWFGSTdWRGRXTkFGdFdtRlVOUU14Vno5U053PT0_c&k=1119&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QXp3SllWNDNVakVDWUFwbURqVlNNd1EyQ21JRllRPT0_c&t=51640123345572052114&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QmprQWFBQnBWalVIWlZvMkNqRlVOUVUzVmo0R1pRPT0_c&t=44890266147756239107&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=VldvQWFBQnBCR2RXTkFCc0NUSlhObFprQm00Rlp3PT0_c&t=30036761497506828158&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QXp3TVpGUTlBR01IWlFCc1hHZFJNRkpnQTJzRlpBPT0_c&t=51959919074412943167&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=RHpCYU1nUnRVakZhT0ZzM1hXWlRNZ014VkR3SFp3PT0_c&t=66599823577042819715&c=0',
        'http://sh31.caihonger.com/selectKings.php?u=QkRzUFoxVThCV1pYTlF0bkRUWUNZMVprQzJJS1l3PT0_c&t=39802592168217782288&c=0',
    ]
    zi_dong_qian_chen(Url_list)