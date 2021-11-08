# def adder(x):
#     def wrapper(y):
#         return x + y
#     return wrapper
# adder5 = adder(5)
# print(adder5(adder5(6)))
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
items = [1, 10, 7, 4, 5, 9]
print(sum(items))