# -*- encoding: utf-8 -*-
'''
@File    :   @property使用.py
@Time    :   2021/01/16 14:57:01
@Author  :   huy
@Version :   1.0
@Contact :   383505002@qq.com
'''

# here put the import lib

class Persion:
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        return self.__name+"shhd"
 
    @name.setter#传一个参数
    def nameset(self,new_name):
        self.__name = new_name
    @name.deleter
    def name(self):
        del self.__name
a1 = Persion('jinijin')
print(a1.name)
a1.nameset = '大家'#修改属性值,    如果不适用@name.setter 则不能修改
print(a1.name)
del a1.name
print(a1.name)
