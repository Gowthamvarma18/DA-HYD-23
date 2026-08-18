#Studet Marks Manager
'''
marks = []

for i in range(3):
    mark = int(input('Enter the marks:',))
    marks.append(mark)

print('Original marks:',marks)

marks.insert(0,90)
print(marks)

marks.extend([75,85])
print(marks)

if 75 in marks :
    marks.remove(75)
    print(marks)


removed_mark = marks.pop()
print("Removed final mark:", removed_mark)

print('Final list marks:',marks)
print(len(marks))
'''

#Number List Analyser
'''
numbers = [20,10,30,20,40,20]

numbers.sort()
print('Ascending order:',numbers)

numbers.reverse()
print('Descending order:',numbers)

search_number = int(input('Enter the number:'))
if search_number in numbers:
    print('Number Found')
    print('Count:',numbers.count(search_number))
    print('Index:',numbers.index(search_number))
else:
    print('Number not found')

print('Largest value:',max(numbers))
print('Smallest value:',min(numbers))
print('Total:',sum(numbers))
'''
#Even and Odd Number Separator
'''
numbers = [10,15,20,25,30,35]
even = []
odd = []
for number in numbers:
    if number %2 == 0:
        even.append(number)
    else:
        odd.append(number)
print('Even number:',even)
print('Odd number:',odd)
print("First three values:", numbers[:3])
print("Last three values:", numbers[-3:])
backup = numbers.copy()
numbers.clear()
print("Original list after clear():", numbers)
print("Backup list:", backup)
'''

#Unique Name Manager
'''
names = ["Asha", "Rahul", "Asha", "John", "Rahul"]
unique_names = set(names)
unique_names.add("Meera")
unique_names.update(["Arun", "Priya"])
if "John" in unique_names:
    unique_names.remove("John")
unique_names.discard("David")
print("Unique student names:")

for name in unique_names:
    print(name)
'''

#Course student Comparision

apython_students={'Asha','Rahul','John','Meera'}
da_students={'Rahul','Meera','Arun'}
a=python_students.union(da_students)
b=python_students.intersection(da_students)
c=python_students.difference(da_students)
d=python_students.symmetric_difference(da_students)
print('All Students:')
for i in a:
    print(i)
print('Students have both courses:')
for j in b:
    print(j)
print('Only Python:') 
for k in c:
    print(k)
print('Only one course:')
for m in d:
    print(m)
    
print("\nDA is subset of Python:", da_students.issubset(python_students))
if da_students.issubset(python_students):
    print("All DA students are also Python students")
else:
    print("All DA students are not Python students")

print("Python is superset of DA:", python_students.issuperset(da_students))
if python_students.issuperset(da_students):
    print("Python contains all DA students")
else:
    print("Python does not contain all DA students")

print("Both sets are disjoint:", python_students.isdisjoint(da_students))
if python_students.isdisjoint(da_students):
    print("There are no common students")
else:
    print("There are common students in both courses")

    
















                    
