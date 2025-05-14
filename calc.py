def fun(a,b,opr):
    if opr=='+':
        return a+b
    elif opr=='-':
        return a-b
    elif opr=='*':
        return a*b
    elif opr=='/':
        return a/b if b!=0 else "zero div error"
    else:
        return "invalid"
    
a=int(input('enter the value1 '))
b=int(input('enter the value2 '))
opr=input('Enter the operator')
print(fun(a,b,opr)) 
