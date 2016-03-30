#coding:utf-8
__author__ = 'gusy'
import urllib2
import json
import MySQLdb
import MySQLdb.cursors
import datetime
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def getDataConn():
    return MySQLdb.connect(
        host='192.168.2.41',
        user='root',
        passwd='root',
        db='test1',
        port=3306,
        charset="utf8",
        cursorclass = MySQLdb.cursors.DictCursor
    )
def getUrl():
    try:
        conn=getDataConn()
        cur=conn.cursor()
        a=cur.execute("select urlType,url from spiderurl")
        # print a
        info=cur.fetchmany(a)
        print json.dumps(info,ensure_ascii=False,indent=2)
        data={}
        for r in info:
            data[r['urlType']]=r['url']
            # data[r[0]]=r[1]
        # print data
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    return data

def insertData(tableName,dataDict):
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
def getUrlStr(url):
    req = urllib2.Request(url)
    try:
        res=urllib2.urlopen(req,timeout=60)
    except urllib2.HTTPError, e:
        print e.code
        time.sleep(2)
        getUrlStr(url)
    except urllib2.URLError, e:
        print e.reason
        time.sleep(2)
        getUrlStr(url)
    else:
        return res.read()
def getPm():
    returnStr=getUrlStr(getUrl()['pm'])
    nowDateStr=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print  returnStr
    from bs4 import BeautifulSoup
    soup =BeautifulSoup(returnStr,"lxml")
    for trChild in soup.find("table","table").find_all("tr"):
        tdChild=trChild.find_all("td")
        if len(tdChild)>0:
            savedata={
                "rank":tdChild[0].string,
                "cityname":tdChild[1].string,
                "aqi":tdChild[2].string,
                "airquality":tdChild[3].string,
                "primarypollution":tdChild[4].string,
                "pm25":tdChild[5].string,
                "pm10":tdChild[6].string,
                "co":tdChild[7].string,
                "no2":tdChild[8].string,
                "o3_1":tdChild[9].string,
                "o3_8":tdChild[10].string,
                "so2":tdChild[11].string,
                "log_at":nowDateStr
            }
            insertData('citypminfo',savedata)
    return
def getweather():
    weatherurl=getUrl()['weather']
    provinceStr=getUrlStr(weatherurl+"china"+".xml")
    nowDateStr=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print provinceStr
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    try:
        provinceTree=ET.fromstring(provinceStr)    #打开xml文档
        for provinceEle in provinceTree.findall("city"):
            provinceData={
                "quName":provinceEle.get("quName"),
                "pyName":provinceEle.get("pyName"),
                "cityname":provinceEle.get("cityname"),
                "stateDetailed":provinceEle.get("stateDetailed"),
                "tem1":provinceEle.get("tem1"),
                "tem2":provinceEle.get("tem2"),
                "windState":provinceEle.get("windState"),
                "log_at":nowDateStr
            }
            insertData("provinceweatherinfo",provinceData)
            cityStr=getUrlStr(weatherurl+provinceEle.get("pyName")+".xml")
            print cityStr
            cityTree=ET.fromstring(cityStr)
            for cityEle in cityTree.findall("city"):
                cityData={
                    "cityX":cityEle.get("cityX"),
                    "cityY":cityEle.get("cityY"),
                    "cityname":cityEle.get("cityname"),
                    "centername":cityEle.get("centername"),
                    "pyname":cityEle.get("pyName"),
                    "stateDetailed":cityEle.get("stateDetailed"),
                    "tem1":cityEle.get("tem1"),
                    "tem2":cityEle.get("tem2"),
                    "temnow":cityEle.get("temNow"),
                    "windState":cityEle.get("windState"),
                    "windDir":cityEle.get("windDir"),
                    "windPower":cityEle.get("windPower"),
                    "time":cityEle.get("time"),
                    "log_at":nowDateStr,
                    "propyname":provinceEle.get("pyName")
                }
                insertData("cityweatherinfo",cityData)
    except Exception, e:
        print "Error:error proparse xml."
    return
getPm()
getweather()


