import re

def fun(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

print(fun("extractemail.txt"))