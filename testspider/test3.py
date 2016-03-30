#coding=utf-8
__author__ = 'meidejing'

##解析html注释部分
def testHtml():
    from bs4 import BeautifulSoup
    markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
    soup = BeautifulSoup(markup,'lxml')
    comment = soup.b.string
    print comment
    print type(comment)
    return
testHtml()








