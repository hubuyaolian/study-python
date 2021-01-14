# coding = utf-8
# @time : 2020/11/25 4:21 下午
# @Autbut : 黄洋
# @Email : 383505002@qq.com
# @File : test1.py
coordinate = []
for x in range(1, 54):
    for y in range(7, 54):
        tmp = {}
        tmp["x"] = x
        tmp["y"] = y
        print(tmp)
        coordinate.append(tmp)

with open("海口坐标.txt", 'w', encoding='utf-8') as f:
    f.write(str(coordinate).replace("\'","\""))