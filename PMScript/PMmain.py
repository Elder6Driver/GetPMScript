# coding:utf8

from bs4 import BeautifulSoup
import urllib.request

if __name__ == "__main__":
    #这里暂时以石家庄为例子，获取石家庄的信息
    url = "http://www.pm25.com/city/shijiazhuang.html"
    response = urllib.request.urlopen(url)
    #使用beautifulsoup来解析这个url中的内容
    soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
    #找到这个class
    node = soup.find('span',class_='cbol_nongdu_num_1')
    #打印出里面的内容
    print(node.get_text())

