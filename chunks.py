def fun(l,n):
    return [l[i:i+n] for i in range(0,len(l),n)]

l= [5,6,7,12,34,56,78]
print(fun(l,3)) 
