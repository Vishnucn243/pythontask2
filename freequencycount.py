from collections import Counter

def fun(filename):
    with open(filename, 'r') as file:
        words=file.read().split()
    return Counter(words)

print(fun("freequencycount.txt"))