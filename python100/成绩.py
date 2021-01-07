a = 0
b = 1
while True:
    if a <= 6765:
        (a, b) = (b, a + b)
        print(a, end=' ')
    else:
        break