def fun(l2,k):
    k=k%len(l2)
    return l2[k:]+l2[:k]
l1=[30,40,50,70,90,100]
print(fun(l1,4))