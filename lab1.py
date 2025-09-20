grade = ["A", "B", "C", "D", "F"]
print(grade[0])

# print 100 as using 'for'

def foobar(a,b):
    for i in range(a,b+1):
        for j in range(1, 13):
            if(i*j%2 == 0):
                print(f"{i} x {j} = {i * j}")

    print("\n")

# start at 5 to 20

foobar(5, 20)

students = [{'name': 'Mark', 'grade': 'A'},
            {'name': 'John', 'grade': 'A'},
            {'name': 'Kong', 'grade': 'C'},
            {'name': 'Nat', 'grade': 'A'},
            {'name': 'Tuna', 'grade': 'D'}]

count = 0
for i in students :
    if i['grade'] == 'A':
        print(i['name'])
        count +=1 
print(count)


