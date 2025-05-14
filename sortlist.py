def fun(l):
    return sorted(l,key=lambda x:x[1])

l=[('abhi',2),('amal',7),('athul',5)]
print(fun(l))