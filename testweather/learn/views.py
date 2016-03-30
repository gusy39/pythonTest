#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import MySQLdb
import MySQLdb.cursors
import json
##获取数据库连接
def getConn():
    return MySQLdb.connect(
        host='192.168.2.41',
        user='root',
        passwd='root',
        db='test1',
        port=3306,
        charset="utf8",
        cursorclass = MySQLdb.cursors.DictCursor
    )
def index(request):
    return render(request,'index.html')
##数据库查询(获取当前数据)
def query(request,type):
    # 获取当前日期格式化
    # ticks =datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    # print  ticks
    try:
        conn=getConn()
        cur=conn.cursor()
        querysql=""
        ##获取城市Pm数据
        if type=="getPm":
            querysql="SELECT pid,rank,cityname,AQI,airquality,primarypollution,pm25,pm10,co,no2,o3_1,o3_8,so2 " \
                     " from citypminfo where log_at=(SELECT  log_at from citypminfo ORDER BY pid DESC LIMIT 0,1 )  ORDER by pm25 DESC "
        ##获取省天气情况
        elif type=="getPWeather":
            querysql="SELECT p.pwid,py.ename,p.pyName,p.cityname,p.stateDetailed,p.tem1,p.tem2,p.windState"\
                     " from provinceweatherinfo p,pynameconvert py " \
                     " WHERE p.pyName=py.pyname and py.pytype='1' and log_at=(SELECT  log_at from provinceweatherinfo ORDER BY pwid DESC LIMIT 0,1 )"
        ##获取城市天气情况
        elif type=="getCWeather":
            querysql="SELECT  cw.cityX,cw.cityY,py.ename,cw.centername,cw.pyname,cw.stateDetailed,cw.tem1,cw.tem2,cw.temnow,cw.windState,cw.windDir,cw.windPower,cw.time,cw.propyname " \
                     " from cityweatherinfo cw,pynameconvert py " \
                     " WHERE cw.pyname=py.pyname AND cw.propyname=py.propyname and py.pytype='2'  and log_at=(SELECT  log_at from cityweatherinfo ORDER BY cwid DESC LIMIT 0,1 )"
        else:
            return u'参数传递错误'
        a=cur.execute(querysql)
        # print a
        info=cur.fetchmany(a)
            # print data
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return HttpResponse(u"查询失败")
    callback = type
    httpres=HttpResponse(json.dumps(info,ensure_ascii=False,indent=2))
    httpres['Access-Control-Allow-Origin'] = '*'
    # return HttpResponse(json.dumps(info,ensure_ascii=False,indent=2))
    # httpres=HttpResponse('%s(%s)' % (callback,json.dumps(info,ensure_ascii=False,indent=2)))
    # httpres['Access-Control-Allow-Origin'] = '*'
    return httpres
    # return JsonResponse(data)

##数据库查询(获取历史详细数据)
##requestCity="广州"
##requestdate="2016-03-16"
def queryDetail(request,type,requestCity,requestdate):
    # 获取当前日期格式化
    # ticks =datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    # print  ticks
    try:
        conn= getConn()
        cur=conn.cursor()
        querysql=""
        ##获取城市Pm数据
        if type=="getPm":
            querysql="SELECT pid,rank,cityname,AQI,airquality,primarypollution,pm25,pm10,co,no2,o3_1,o3_8,so2 " \
                     " from citypminfo " \
                     "WHERE cityname= '"+requestCity+"' and log_at=(select log_at from citypminfo where DATE_FORMAT(log_at,'%Y-%m-%d')='"+requestdate+"' ORDER BY pid DESC LIMIT 0,1)"

        ##获取城市天气情况
        elif type=="getCWeather":
            querysql="SELECT  cw.cityX,cw.cityY,py.ename,cw.centername,cw.pyname,cw.stateDetailed,cw.tem1,cw.tem2,cw.temnow,cw.windState,cw.windDir,cw.windPower,cw.time,cw.propyname " \
                     " from cityweatherinfo cw,pynameconvert py" \
                     "  WHERE cw.pyname=py.pyname AND cw.propyname=py.propyname  and (py.pytype='2' OR py.propyname in('shanghai','chongqing','beijing','tianjing') ) AND  cw.cityname='"+requestCity+"'  and log_at=(SELECT  log_at from cityweatherinfo where DATE_FORMAT(log_at,'%Y-%m-%d')='"+requestdate+"' ORDER BY cwid DESC LIMIT 0,1 )"
        else:
            return u'参数传递错误'
        a=cur.execute(querysql)
        # print a
        info=cur.fetchmany(a)
        # print data
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return HttpResponse(u"查询失败")
    callback = type
    httpres=HttpResponse(json.dumps(info,ensure_ascii=False,indent=2))
    httpres['Access-Control-Allow-Origin'] = '*'
    # return HttpResponse(json.dumps(info,ensure_ascii=False,indent=2))
    # httpres=HttpResponse('%s(%s)' % (callback,json.dumps(info,ensure_ascii=False,indent=2)))
    # httpres['Access-Control-Allow-Origin'] = '*'
    return httpres
    # return JsonResponse(data)