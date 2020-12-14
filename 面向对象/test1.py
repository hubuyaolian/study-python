# coding = utf-8
# @time : 2020/11/25 4:21 下午
# @Autbut : 黄洋
# @Email : 383505002@qq.com
# @File : test1.py

class Man:
    """男人"""
    def __init__(self):
        self.__idea = "Love"

    def setIdea(self, newIdea):
        """不能不爱"""
        if newIdea != "Love":
            print("我只爱你！不要别的……")

    def getIdea(self):
        """看看你到底爱不爱"""
        print("我%s你！" %(self.__idea))

        
m = Man()
m.getIdea()
m.setIdea("Hate")
m.getIdea()
print(m._Man__idea) 