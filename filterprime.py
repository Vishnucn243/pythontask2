def fun(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [0,3,20,43,90,100]
primes = list(filter(fun, numbers))
print(primes) 