from BasePartDLL import *
import datetime   

def lue_duo_zi_yuan(url_, city_names_, battle_city_names_):
    base = Base()
    base.config(0)
    try:
        base.driver.get(url_)
        delay()
        time_list = []
        delay_time = 0
        name = base.get_maincity_name()
        logger.debug(f'寨主:{name}')
        for index in range(0, 10):
            logger.info(f'当前分寨：{city_names_[index]}')
            base.click_word(name)
            base.click_word(city_names_[index])
            base.click_word('地图')
            base.click_word(battle_city_names_[index])
            base.chu_bin(time_list)
        
        if len(time_list) <= 0:
            logger.error('time_list is an empty sequence')
        else:
            delay_time = max(time_list)
            logger.info(f'max_delay_time: {delay_time}s', delay_time)
        base.driver.quit()
        return delay_time
    except:
        base.driver.quit()
        return 0


if __name__ == '__main__':
    # logger.add(r'F:\python\红颜水浒\log\RunTime_掠夺资源.log', rotation='500 MB', level='INFO')
    url = 'http://sh27.hongyanshuihu.com/master.php?t=1644045681&u=VVdzSVpsTS9VVEpSUHdoaENqSlJORk5u&k=10771&c=1'
    city_names = ['②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '①①']
    battle_city_names = [ '双悟发|男', '欧阳益简|男', '邴华洁|男', '宗化忠|男', '隆生藻|男', '美|女', '东方珠罡|男', '巫滨慕|男', '谷宇鲲|男', '路延齐|男']
    while True:
        StartTime = datetime.datetime.now()
        DelayTime = lue_duo_zi_yuan(url, city_names, battle_city_names)
        EndTime = datetime.datetime.now()
        NeedTime_ = str(EndTime - StartTime)
        NeedTime = del_path_time(NeedTime_)
        logger.info(f'Need Time: {NeedTime}s', NeedTime)
        # NeedDelayTime = DelayTime - NeedTime + 5
        NeedDelayTime = 126
        if NeedDelayTime > 0:     
            time_after(NeedDelayTime)
        else:
            continue
