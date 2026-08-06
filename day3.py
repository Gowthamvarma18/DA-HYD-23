#Numeric datatype --> int,float,complex, along with boolean

#Input formating --->Accepting input from the user --> input()

#Accepting integer input from user
#by default input() accepts any input -->
#int(input()) --> will accept only integers
'''
age = int(input('enter the age:'))
print(age)
print(type(age))

#float(input()) -->accepts integer,float values
price = float(input('enter the price:'))
print(price)
print(type(price))


#Accepting string input from user

name = input('enter the name:')
print(name)
print(type(name))


#Accept ground of values

a = input().split() #by default split() has space
print(a)

#space seperated values
a = input().split() #now you enter spaces in output
print(a)

#comma seperated values
a = input('enter the values:').split(',')
print (a)
print(type(a))


#List of integers
marks =list( map(int,input('enetr the values').split(',')))
print(marks)
print(type(marks))


#Now we want to accept 2 values from user
age,salary = map(int,input('enter the values').split(','))
print(age)
print(salary)

#Single input --> int(input())
#two inputs -->a,b = map(int,input().split(','))
#any number result as list  --> a = list(map(int,input().split(',')))


#Float  of integers
marks = list(map(float,input('enter the values').split(',')))
print(marks)

#group of float values
age,salary = map(float,input('enter the values').split(','))
print(age)
print(salary)


#Accepting input from user  ---> int,float --> input formating

#Operating --> operators perform operations between values (operands)
#7 types  -->Arthematic,Assignments,Comparision (Relationship)
#Membership,Identity,Logical,Bitwise


#Arthematic Operations --->Arthematic Operations
#+,-,*,/
print(5+3)
print(5-3)
print(5*3)
print(6/2) #Float value
#Floor Division (Integer division) -->returns quotient
print(6//2)
#Modulus -->divisible rules -->returns remainder
print(6%2)
#power (exponential)
print(5**3)


#Task-->Accept integer input as length,breadth -->find the area of rectangle
#Area = length * breadth

length,breadth=map(int,input('enterv the value').split(','))
area = length * breadth
print(area)


#Assignments operators -->assign the values
# = , += ,-=
a = 45
print(a)
#update the value of a
a = a + 5 #a+= 5
print(a)
b = 35
b += a #b = b + a
print(b)

b -= 5
print(b)

#Task : *=,/=,//=,%=,**= workout


#Comparision Operators -->we compare the values -->boolean
# == (equal to ) , !=(not equal to) , < (less than) , >(greater than)
# <= (less than or equal to) >= (greater than or equal to)

age = 25
print(age == 25) #returns Boolean output
print(age !=35)
print(age <=35)
print(age >=35)
print(age >35)
print(age <35)

print(-5 < -1)


#Membership operators --> in,not in
#it check for the existance of an object in collection

marks = [56,75,45,85]
print(35 in marks)
#print(35 in 355) #TypeError

print(25 not in marks)
print('code' in 'codegnan')
print('$' in 'abc$frg')


#Logical operators  --> logical decision making -->and,or,not
#and -->all conditions to be satisfied
#or --> any one condition to be stisfied

a = (25 in [25,45,65]) and 45 < 56
print(a)
b = 45 > 56 or 25 <= 45
print(b)
c = not(True)
print(c)


#Identity Operators --> check for identity of an object --> id()

a = 35
b = 35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)
'''

a = [1,2,3,4,5]
print(id(a))
c  = a
print(id(c))
print(c is a)
b = [1,3,4,2,5]
print(id(b))
