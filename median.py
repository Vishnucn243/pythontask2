def fun(l):
    l2= sorted(l)
    n = len(l2)
    if n % 2 == 0:
        return (l2[n//2 - 1] + l2[n//2]) / 2
    return l2[n//2]

print(fun([5,6,7,8,9,10,11])) 
print(fun([10,20,30,40]))  