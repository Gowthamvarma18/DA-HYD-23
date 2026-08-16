'''
List,Tuples...
'''
#List -->Mutabla,Ordered,Heterogenous

#index(),count(),copy(),sort(),reverse()
'''
details =['Codegnan',7,2018,'Hyderbad']

print(len(details))
print(details.index(7))
print(details.index('Codegnan'))
details.extend([7,21,45,21])
print(details)
print(details.index(21))         #it returns first occurance
print(details.index(21,6))
#print(details.index('python'))         #ValueError

print(details.count(21))
print(details.count('python'))#it returns 0 as we dont have it

'''
#Copy() -->shallow copy of the given collection
'''
data = ['Codegnan','Saketh','45','java']
new = data.copy()
print(new)
print(type(new))
print(len(data))


new[2] = 'Agentic AI'
print(new)
print(data)

data.append('[Saketh,Gowtham,raj]')
print(data)
print(new)

data.extend([1,2,3,4])
print(data)

data = [1,4,5,[21,34,45],23]
print(data)
new = data.copy()
print(new)

new[3][2] = 'Agents' #Whenever we make changes in nested list original will also be effected
print(new)
print(data)

new[1] = 'Python'
print(new)
print(data)


marks = [14,24,-45,27,35]
print(marks)
#print(marks.sort()) #return None
#print(marks) #returns in ascending order
#marks.sort(reverse = True)#returns in descending order....
#print(marks)
marks.insert(2,'Code')
#marks.sort()
#reverse() --> returns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])
'''

#type(),len(),max(),min(),print()
'''
print(sorted('codegnan'))#returns list in ascending order
#print(sorted(['code','23','34','45'])#raise Error
'''

#Tuples --> Tuples are Indexed,Orderd,Heterogenous,Immutable collection
#dimensions,coordinates,database records,we prefer () for tuple notation
'''
a = ()
print(type(a))
print(len(a))


dimensions = 1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))
'''
#Operations -->Indexing,Slicing,Striding,Membership,Merging,Repetition

courses = ('PFS','JFS',('DA','DS'),'Agentic AI',[100,6,61])
'''
print(courses)
print(len(courses))

print(courses[-2][-2::])
#courses[2] = 23 Tuples are Immutable
courses[-1].append('Codegnan') #we can make any modification inside list
print(courses)

#Created a Nested tuple as above and work on Slicing,Striding and List Function
print('PFS' in courses) #Membership
d = courses * 2 #repetition
print(d)
e = courses + (2,3,4,5) #merging
print(e)
'''

#Tuples Immutable -->count(),index()
'''
print(courses.index('Agentic AI')) #returns first occurancy
print(courses)
print(courses.count('Agents'))

#print(coures.sort()) #AttributeError -->sort() is in Lists not in Tuples

print(sorted(courses[-1]))
#print(sorted(courses)) #as we have mixed types

#TypeCasting
d = tuple(sorted((23,12,3,4,5)))
print(d)
'''
#accept group of integers space separated
'''
a,b = map(int,input('Enter the values').split())
print(a,b)

a = tuple(map(int,input('Enter the values').split(',')))
print (a)

print('9+4')
#eval() function can take any kind of input
print(eval('9+4'))

a = eval(input('Enter a list')) #in this case u can exactly enter data as list
print(a)
print(type(a))
'''
#Task:Take a user input as string,do this in two ways..
'''
1) give the count of each repeating charcter
Test case 1: programming

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is repeating 2 times
index = [1,4]
g is repeating 2 times
index = [3,10]
m is repeating 2 times
index = [6,7]
'''
























