def fun(l):
    if len(l)<2:
        print('not possible')
    l.sort()
    return max(l[0]*l[1],l[-1]*l[-2])
l2=[200,20,40,-20,-30]
print(fun(l2))  