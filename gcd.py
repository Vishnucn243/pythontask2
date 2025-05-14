def fun(a, b):
    if b == 0:
        return a
    return fun(b,a % b)

print(fun(50,25)) 