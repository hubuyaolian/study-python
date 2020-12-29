class Person(object):
    """方法链小sample"""

    def name(self, value):
        self.name = value
        return self # 返回实例对象自己才能再调用实例对象的方法。

    def work(self, value):
        self.working = value
        return self

    def introduce(self):
        print("你好, 我的名字:", self.name, ",我的工作:", ",教初学者学会编程!")

person = Person()
person.name("黄哥")
person.introduce()