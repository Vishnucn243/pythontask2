def fun(list1):
    list2= []
    for i in list1:
        if type(i)==list:
            list2+=fun(i)
        else:
            list2+=[i]
    return list2
l1= [[0,9],8,7,[8,[4,1]]]
print(fun(l1)) 