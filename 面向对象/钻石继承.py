class A():
    def __init__(self):
        pass
        
    def hi(self):
        print("I'm A!")
class B(A):
    def __init__(self):
        pass
class C(A):
    def __init__(self):
        pass
    def hi(self):
        print("I'm C!")
class D(B, C):
    def __init__(self):
        pass
fun =  D()
fun.hi()
# print(D.mro())