'''
Sequences --> Strings,Lists,Tuples,Sets
Mapping -->Dictionary
'''

#Lists --> Collection of heterogenous elements(items)
#List -->Indexed,Ordered,Mutable,Heterogenous,we use [] to store the data
'''
marks = [35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
'''
#Operations : Indexing,Slicing,Striding,Membership,Merging,Repetition

#Nested Lists --> A list inside another list

names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
'''
print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type(names[0]))
print(names[0][:4]) #it returns code
print(names[0][4:])

#get the output as cdga
print(names[0][::2])
names[0] = names[0][::-1]
print(names)
'''
'''
print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexing,Slicing -->Mutable
names[2] = 'Python'
print(names)
#By indexing if we change of elements,length of collection will remain same
names[4] = ['Codegnan','PFS','JFS','DA','AAA','DS']
print(names)
print(len(names))
print(names[3][1:3])
print(names[4][0])
print(names[4][0][4:])

names[2:4] = 'Abhiram','Sai','Saketh','Sairam'
print(names)

#In Slicing whatever elements u pass as per the logic length keeps on increasing

#o/p as follows :
#['Codegnan',25,'Abhiram','Python','Saketh','Java','DA23',34]
print(names[2:6])
print(names[3:6:2])
names [3:6:2] = 'Python','Java'
print(names)
'''


#Create a nested list with strings,lists and work on Indexing,Slicing,Striding
#added advantage if u could add string functions also to it
#Lists Function -->append(),insert(),extend(),pop(),remove(),clear()
#index(),count(),sort(),reverse()
'''
names = ['Codegnan','Saketh']
#append() -->inserts single element to the end of the list
names.append('data')
print(names)
#names.append('analysis','agents')#TypeError
names.append(['analysis','agent'])
#print(names)
#append() will alwys increment the length of list by 1
#print(names[3])
#print(names[3].append('chatgpt')# it returns None as append is applicable on list not print
#print(names)
print(names)
'''
#extend() -->inserts multiple elements to the end of list
'''
names.extend('analysis')#string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,76,44,55])
print(names)
#names.extend(35,45) TypeError
#print(names)

names.insert(1,'Python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b,]) #SyntaxError
#print(names)
names.insert(-1,'AAA')
print(names)
'''
#pop(),remove(),clear()
#pop() by default last,else give index
print(names.pop())
print(names)
names.pop(2)
print(names)

#remove() we can remove a specific value
names.extend([23,14,15])
print(names)

names.remove(14)
print(names)
#names>remove(14) #it raises ValueError
del names[1:3] #del keyword will apply permanent changes
print(names)
names.clear() #clear() will remove all elements and return empty list
print(names)


data = ['codegnan','saketh','python','java']#input
#output should be as follows
'''
0 : codegnan
1 : saketh
2 : python
3 : java
'''
for obj in data:
    print(data.index(obj),':',obj)


for obj in range(len(data)):
    print(obj,':',data[obj])












