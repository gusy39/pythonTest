#coding=utf-8
__author__ = 'meidejing'
import test
def index(a,b):
    return a+b
def cc():
    test.test()
    print index(3,5)
cc()

class Student(object):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age
l=Student("","")
l.setAge(9)
l.setName("1212")
print  l.getName(),l.getAge()









