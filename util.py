count = 0
for i in students :
    if i['grade'] == 'A':
        print(i['name'])
        count +=1 
print(count)