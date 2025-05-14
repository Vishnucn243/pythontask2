def fun(l):
    return [x if x>=0 else 0 for x in l]

l=[5,-77,8,-44]
print(fun(l)) 