def fun(base,exp):
    result=1
    for _ in range(exp):
        result*=base
    return result

print(fun(2,2)) 