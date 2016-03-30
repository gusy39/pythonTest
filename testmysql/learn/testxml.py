#coding:utf-8
from django.http import HttpResponse
import MySQLdb
import json
##请求测试
def index(request):
    return HttpResponse(u"测试!")
    #读取xml文件，数据库插入测试
def  testxml(request):
    try:
         import xml.etree.cElementTree as ET
    except ImportError:
         import xml.etree.ElementTree as ET
    import sys

    try:
        tree = ET.parse("E:/country.xml")     #打开xml文档
        #root = ET.fromstring(country_string) #从字符串传递xml
        root = tree.getroot()         #获得root节点
    except Exception, e:
        print "Error:cannot parse file:country.xml."
        sys.exit(1)
    print root.tag, "---", root.attrib
    for child in root:
        print child.tag, "---", child.attrib

    print "*"*10
    print root[0][1].text   #通过下标访问
    print root[0].tag, root[0].text
    print "*"*10

    for country in root.findall('country'): #找到root节点下的所有country节点
        rank = country.find('rank').text   #子节点下节点rank的值
        name = country.get('name')      #子节点下属性name的值
        print name, rank

    #修改xml文件
    for country in root.findall('country'):
        rank = int(country.find('rank').text)
        if rank > 50:
            root.remove(country)
    tree.write('E:/output.xml')

    return HttpResponse(u"添加成功!")
##测试读取配置文件函数
def testIni(request):
    import ConfigParser
    import string, os, sys

    cf = ConfigParser.ConfigParser()

    cf.read("test.text")

    #return all section
    secs = cf.sections()
    print 'sections:', secs

    opts = cf.options("db")
    print 'options:', opts

    kvs = cf.items("db")
    print 'db:', kvs

    #read by type
    db_host = cf.get("db", "db_host")
    db_port = cf.getint("db", "db_port")
    db_user = cf.get("db", "db_user")
    db_pass = cf.get("db", "db_pass")

    #read int
    threads = cf.getint("concurrent", "thread")
    processors = cf.getint("concurrent", "processor")

    print "db_host:", db_host
    print "db_port:", db_port
    print "db_user:", db_user
    print "db_pass:", db_pass

    print "thread:", threads
    print "processor:", processors


    #modify one value and write to file
    cf.set("db", "db_pass", "xgmtest")
    cf.write(open("test.conf", "w"))






