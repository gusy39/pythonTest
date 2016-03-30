# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
	test1 = Test(name='w3cschool.cc')
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>")
def testdbGet(request):
	response = ""
	response1 = ""
	list=Test.objects.all();
	response2 = Test.objects.filter(id=1)
	response3= Test.objects.get(id=1)
	Test.objects.order_by('name')[0:2]	

	Test.objects.order_by("id")
	Test.objects.filter(name="w3cschool.cc").order_by("id")

	for var in list:
		response1 +=var.name+" "
		pass
	response=response1
	return HttpResponse("<p>"+response+"</p>")	