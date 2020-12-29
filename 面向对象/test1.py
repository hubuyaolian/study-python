# coding = utf-8
# @time : 2020/11/25 4:21 下午
# @Autbut : 黄洋
# @Email : 383505002@qq.com
# @File : test1.py
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 31.75},
    {'name': 'HPQ', 'shares': 350, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
print(heapq.nlargest(10,list2, key=lambda x: (x['price'],x['shares'])))
#print(heapq.nlargest(2, list2, key=lambda x: x['shares']))