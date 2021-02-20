def fun3():
    try:
        x=[1,2,3]
        raise
        return x.append(6)
    except Exception:
        x.append(4)
        return x+[34]
    finally:
        x.append(5)
        print("fun3 finally")
        return x+[23]
wh = fun3()
print(wh)