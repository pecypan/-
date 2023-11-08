from BasePartDLL import *








if __name__ == '__main__':
    with open('29服.txt', 'r+') as f:
        a = f.readlines()
        f.close()
    for url in a:
        p = '{"脚本类型":"进入网址","进入网址":"' + url + '"}'
        with open('29书签.txt', 'a+') as f:
            f.writelines(p)
            f.writelines('\n')
            f.close()
   