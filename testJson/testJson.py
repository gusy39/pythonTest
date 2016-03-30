#coding:utf-8
__author__ = 'gusy'
import json
import MySQLdb
import MySQLdb.cursors
import datetime
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
##获取数据库连接spider
def getSpiderConn():
    return MySQLdb.connect(
        host='192.168.2.246',
        user='root',
        passwd='root',
        db='spider',
        port=3306,
        charset="utf8",
        cursorclass = MySQLdb.cursors.DictCursor
    )

##获取数据库连接ecmoho_data
def getDataConn():
    return MySQLdb.connect(
        host='192.168.2.246',
        user='root',
        passwd='root',
        db='ecmoho_data',
        port=3306,
        charset="utf8",
        cursorclass = MySQLdb.cursors.DictCursor
    )
##读取文件内容
def getFileJson(account,accountType,startDate,endDate):
    fileurl=r''.join(['e:\www\spiderapi\spiderhtml\\tb_sjmf\\',account,'\\',startDate,'_',endDate,'-'+accountType+'\\',account,'-sjmf-'+accountType+'.json'])
    file_object = open(fileurl)
    try:
        all_the_text = file_object.read().decode("utf-8")
        fileJson=json.loads(all_the_text)
    finally:
        file_object.close()
    return fileJson
##插入数据库操作
def insertEcmohoData(tableName,dataDict):
    try:
        connData=getDataConn()
        curData=connData.cursor()
        keyStr=''
        valueStr=''
        for key,value in dataDict.iteritems():
            keyStr=keyStr+key+","
            value1=""
            if(value==None or value==""):
                value1=""
            else:
                value1=value
            valueStr=valueStr+"'"+str(value1)+"',"
        insertSql="insert into "+tableName+"("+keyStr[0:len(keyStr)-1]+") values ("+valueStr[0:len(valueStr)-1]+")"
        print insertSql
        curData.execute(insertSql)
        connData.commit()
        curData.close()
        connData.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return "error"
    return
##获取spider信息
def getSpiderMap(account):
    try:
        connSpider=getSpiderConn()
        curSpider=connSpider.cursor()
        curSpider.execute("SELECT * from spider_account_sjmf where account='"+account+"'")
        info=curSpider.fetchone()
        curSpider.close()
        connSpider.close()
        return info
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
         return "error"
##产品数据插入
def jsonInsertproduceSql(account,accountType,startDate,endDate):
    info=getSpiderMap(account)
    fileJson=getFileJson(account,accountType,startDate,endDate)
    for valueItem in fileJson:
        tradeType=valueItem.get('tradeType')
        clevel=valueItem.get('clevel')
        for valueB in valueItem.get('data'):
            bname=valueB.get('bname')
            for valueP in valueB.get('bdata'):
                pname=valueP.get('pname')
                for value in valueP.get('pdata')[0]:
                     saveData={
                        "accountId":info.get('id'),
                        "f0": value.get('f0'),
                        "f1": value.get('f1'),
                        "f2": value.get('f2'),
                        "f3": value.get('f3'),
                        "f4": value.get('f4'),
                        "f5": value.get('f5'),
                        "f6": value.get('f6'),
                        "f7": value.get('f7'),
                        "f8": value.get('f8'),
                        "f9": value.get('f9'),
                        "f10": value.get('f10'),
                        "f11": value.get('f11'),
                        "f12": value.get('f12'),
                        "f13": value.get('f13'),
                        "f14": value.get('f14'),
                        "f15": value.get('f15'),
                        "f16": value.get('f16'),
                        "clevel": clevel,
                        "tradeType":tradeType,
                        "brand":bname,
                        "produce":pname,
                        "createdate":datetime.datetime.now().strftime('%Y-%m-%d'),
                        "create_at":value.get('f0')[0:4]+"-"+value.get('f0')[4:6]+"-"+value.get('f0')[6:8],
                        "log_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                     insertEcmohoData('t_tb_sjmf_'+accountType,saveData)
    return
##品牌数据插入
def jsonInsertbrandSql(account,accountType,startDate,endDate):
    info=getSpiderMap(account)
    fileJson=getFileJson(account,accountType,startDate,endDate)
    for valueItem in fileJson:
        tradeType=valueItem.get('tradeType')
        clevel=valueItem.get('clevel')
        for valueB in valueItem.get('data'):
            bname=valueB.get('bname')
            for value in valueB.get('bdata')[0]:
                saveData={
                    "accountId":info.get('id'),
                    "f0": value.get('f0'),
                    "f1": value.get('f1'),
                    "f2": value.get('f2'),
                    "f3": value.get('f3'),
                    "f4": value.get('f4'),
                    "f5": value.get('f5'),
                    "f6": value.get('f6'),
                    "f7": value.get('f7'),
                    "f8": value.get('f8'),
                    "f9": value.get('f9'),
                    "f10": value.get('f10'),
                    "f11": value.get('f11'),
                    "f12": value.get('f12'),
                    "f13": value.get('f13'),
                    "f14": value.get('f14'),
                    "f15": value.get('f15'),
                    "f16": value.get('f16'),
                    "clevel": clevel,
                    "tradeType":tradeType,
                    "brand":bname,
                    "createdate":datetime.datetime.now().strftime('%Y-%m-%d'),
                    "create_at":value.get('f0')[0:4]+"-"+value.get('f0')[4:6]+"-"+value.get('f0')[6:8],
                    "log_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                insertEcmohoData('t_tb_sjmf_'+accountType,saveData)
    return
##行业数据插入
def jsonInsertTradeSql(account,accountType,startDate,endDate):
    info=getSpiderMap(account)
    fileJson=getFileJson(account,accountType,startDate,endDate)
    for valueItem in fileJson:
        tradeType=valueItem.get('tradeType')
        clevel=valueItem.get('clevel')
        for value in valueItem.get('data')[0]:
            saveData={
                "accountId":info.get('id'),
                "f0": value.get('f0'),
                "f1": value.get('f1'),
                "f2": value.get('f2'),
                "f3": value.get('f3'),
                "f4": value.get('f4'),
                "f5": value.get('f5'),
                "f6": value.get('f6'),
                "f7": value.get('f7'),
                "f8": value.get('f8'),
                "f9": value.get('f9'),
                "f10": value.get('f10'),
                "f11": value.get('f11'),
                "f12": value.get('f12'),
                "clevel": clevel,
                "tradeType":tradeType,
                "createdate":datetime.datetime.now().strftime('%Y-%m-%d'),
                "create_at":value.get('f0')[0:4]+"-"+value.get('f0')[4:6]+"-"+value.get('f0')[6:8],
                "log_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            insertEcmohoData('t_tb_sjmf_'+accountType,saveData)
    return





##雷允上品牌淘宝
jsonInsertbrandSql('sycm-lys','brand_taobao','2013-09-01','2014-01-01')
jsonInsertbrandSql('sycm-lys','brand_taobao','2014-01-02','2014-12-31')
jsonInsertbrandSql('sycm-lys','brand_taobao','2015-01-01','2015-10-20')
jsonInsertbrandSql('sycm-lys','brand_taobao','2015-10-21','2015-10-30')

##雷允上品牌天猫
jsonInsertbrandSql('sycm-lys','brand_tmall','2013-09-01','2014-09-30')
jsonInsertbrandSql('sycm-lys','brand_tmall','2014-10-01','2015-10-20')
jsonInsertbrandSql('sycm-lys','brand_tmall','2015-10-21','2015-10-30')

##哈药行业淘宝
jsonInsertbrandSql('sycm-hy','brand_taobao','2013-09-01','2014-01-01')
jsonInsertbrandSql('sycm-hy','brand_taobao','2014-01-02','2014-07-01')
jsonInsertbrandSql('sycm-hy','brand_taobao','2014-07-02','2014-12-31')
jsonInsertbrandSql('sycm-hy','brand_taobao','2015-01-01','2015-05-31')
jsonInsertbrandSql('sycm-hy','brand_taobao','2015-06-01','2015-10-20')
jsonInsertbrandSql('sycm-hy','brand_taobao','2015-10-21','2015-10-30')
##哈药行业天猫
jsonInsertbrandSql('sycm-hy','brand_tmall','2013-09-01','2014-09-30')
jsonInsertbrandSql('sycm-hy','brand_tmall','2014-10-01','2015-10-20')
jsonInsertbrandSql('sycm-hy','brand_tmall','2015-10-21','2015-10-30')


