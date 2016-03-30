#coding:utf-8
from django.http import HttpResponse
from django.http import JsonResponse
import MySQLdb
import json
import datetime

##请求测试
def index(request):
    return HttpResponse(u"测试!")
#数据库插入测试
def  add(request):
	name=request.GET['name']
	age=request.GET['age']
	try:
		conn=MySQLdb.connect(
			host='192.168.2.178',
			user='root',
			passwd='root',
			db='test1',
			port=3306,
			charset="utf8"
			)
		cur=conn.cursor()
		l=(name,age)
		print l
		cur.execute('insert into test values(%s,%s)',l)
		conn.commit()
		cur.close()
		conn.close()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	return HttpResponse(u"添加成功!")
	pass
#数据库更新测试
def update(request):
	name=request.GET['name']
	age=request.GET['age']
	try:
		conn=MySQLdb.connect(
			host='192.168.2.178',
			user='root',
			passwd='root',
			db='test1',
			port=3306,
			charset="utf8")
		cur=conn.cursor()
		l=(age,name)
		cur.execute('update test set age = %s where name =%s',l)
		conn.commit()
		cur.close()
		conn.close()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return u"更新失败"
	return HttpResponse(u"更新成功!")
	pass
##数据库查询测试
def query(request):
    # 获取当前日期格式化
    # ticks =datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    # print  ticks
    try:
        conn=MySQLdb.connect(
            host='192.168.2.178',
            user='root',
            passwd='root',
            db='test1',
            port=3306,
            charset="utf8"
        )
        cur=conn.cursor()
        a=cur.execute("select * from test")
        # print a
        info=cur.fetchmany(a)
        desc=cur.description
        print desc
        for i in desc:
            print i[0]
        # print desc[0][0],desc[1][0]
        data=[]
        for r in info:
            datarow={}
            datarow["name"]=r[0]
            datarow["age"]=r[1]
            data.append(datarow)
            # print data
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return HttpResponse(u"查询失败")
    return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))
    # return JsonResponse(data)

##python操作ftp测试
def testftp(request):
    from ftplib import FTP
    ftp=FTP()
    ip='192.168.1.245'
    port= 21
    timeout = 30
    username='tb_sycm'
    password='1234'
    ftp.connect(ip,port,timeout)
    ftp.login(username,password)
    # print ftp.getwelcome()
    ftp.cwd("spiderhtml")

    list = ftp.nlst()
    # 获得目录列表
    for name in list:
        print name



    # file_object=open('test1.html')
    # try:
    #     all_the_text = file_object.read()
    #     print all_the_text
    # finally:
    #     file_object.close()
    return HttpResponse(json.dumps(list))


