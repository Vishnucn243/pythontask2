dict1= [{'name':'ann','course':'python','experience':'4'}, {'name':'amal','course':'java','experience':'3'}]
l2= sorted(dict1, key=lambda x: x['experience'])
print(l2) 