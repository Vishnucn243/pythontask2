def common(l1,l2):
    s1=set(l1)  
    s2=set(l2)  
    commonis=s1&s2
    result=list(commonis) 
    return result
l1=[23,6,9,9,0]
l2=[0,9,2]
print(common(l1,l2)) 