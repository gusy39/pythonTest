import urllib
import urllib2
def test():
    url = "https://bda.sycm.taobao.com/decorate/getGeneralTrend.json?_t=1448865360211&appType=undefined&ctoken=null&dateRange=2015-10-31%7C2015-11-29&dateType=recent30&endDate=2015-11-29&objId=112350981&objId2=112350981&spmb=shop/index_2126668391_112350981&startDate=2015-10-31&type=0&_=1448865360213"
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
        'referer':'https://zxfx.sycm.taobao.com/index.htm',
        'cookie':'thw=cn; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; ali_ab=58.246.199.94.1448846980255.5; v=0; _tb_token_=SXv7p5nsux1EUH1; uc1=tmb=1&cookie14=UoWzUaLJe6gg%2BA%3D%3D&existShop=true&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=UIHiLt3xSard&tag=0&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; uc3=nk2=2nGsOue2UMJtNeIZXKM%3D&id2=UUkM8Vl4yqhMOg%3D%3D&vt3=F8dAScAbVHxi%2BkMQ7e4%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTQ0ODg2NTM1OA%3D%3D; lgc=%5Cu54C8%5Cu836F%5Cu5B98%5Cu65B9%5Cu65D7%5Cu8230%5Cu5E97; tracknick=%5Cu54C8%5Cu836F%5Cu5B98%5Cu65B9%5Cu65D7%5Cu8230%5Cu5E97; sg=%E5%BA%971c; cookie2=2cf3463a82c80cbaac9f9d649f199d42; mt=np=&ci=4_1; cookie1=AQchDxXzcpXQUH6ssR84Jtda7tJMMt0UQ7oviJCqLBY%3D; unb=2126668391; skt=62c7b3fd11f1c2c4; t=9e2dd6f125f811ad65e1a90538b3716e; _cc_=Vq8l%2BKCLiw%3D%3D; tg=0; _l_g_=Ug%3D%3D; _nk_=%5Cu54C8%5Cu836F%5Cu5B98%5Cu65B9%5Cu65D7%5Cu8230%5Cu5E97; cookie17=UUkM8Vl4yqhMOg%3D%3D; l=Av7-AZznzfJ1lyaN2HdM6oL-zhpBOsK5; _uacm_ac_s_tp_=1; _uacm_ac_s_ti_=%B9%FE%D2%A9%B9%D9%B7%BD%C6%EC%BD%A2%B5%EA; _uacm_ac_s_id_=112350981; _uacm_ac_u_nk_=%B9%FE%D2%A9%B9%D9%B7%BD%C6%EC%BD%A2%B5%EA; isg=D37EC69DA34B6CC37F1C4AC0E0B5D72D',
        'origin':'https://zxfx.sycm.taobao.com',
        }
    request = urllib2.Request(url,None,headers)
    response = urllib2.urlopen(request)
    print response.read()
    return