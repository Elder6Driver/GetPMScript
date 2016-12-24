# coding:utf8

from bs4 import BeautifulSoup
import urllib.request
import threading
import queue

class PMManager(object):
    #默认构造的时候放入url
    def __init__(self,urlstring):
        self.urlstring = urlstring
        self.qu = queue.Queue()

    def GetQue(self):
        li = list()
        while not self.qu.empty():
            li.append(self.qu.get())
        # 打印出里面的内容
        return li

    def GetParam(self):
        url = self.urlstring
        response = urllib.request.urlopen(url)
        # 使用beautifulsoup来解析这个url中的内容
        soup = BeautifulSoup(response, 'html.parser', from_encoding='utf-8')
        # 找到这个class
        node = soup.find('span', class_='cbol_nongdu_num_1')
        # 把内容放入队列中
        self.qu.put(node.get_text())
        #print(node.get_text())
        #return node.get_text()

    def ThreadFunction(self):
        t = threading.Thread(target= self.GetParam())
        t.start()


if __name__ == "__main__":
    url = "http://www.pm25.com/city/shijiazhuang.html"
    pm = PMManager(url)
    pm.ThreadFunction()
    li = pm.GetQue()
    for item in li:
        print(item)





