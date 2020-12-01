# coding = utf-8
# @time : 2020/11/25 4:21 下午
# @Autbut : 黄洋
# @Email : 383505002@qq.com
# @File : test1.py

class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")