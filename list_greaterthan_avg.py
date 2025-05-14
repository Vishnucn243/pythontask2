def fun(l):
    avg=sum(l)/len(l)
    return sum(1 for i in l if i>avg)

l=[10,20,30]
print(fun(l)) 