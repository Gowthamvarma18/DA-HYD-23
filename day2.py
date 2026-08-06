'''
Tokens ---> Named memory location,its a placholder for data
#Rules are to be followed
'''
#MultiAssignment of Variables
'''
name,age,place='Gowtham Varma',22,'Bhimavaram'
print(name,age,place,)
print(name,age,place,sep=',')
print(name,age,place,sep='------->')


#a,b = 2,4,5 #ValueError as too many values to unpack
#Reassigning variables

name='Gowtham varma'
a,b = 2,4.5
print(a,b,sep=',')
a,b=b,a #Swapping
print(a,b,sep=',')


#a,b = b,c #NameError as c is not defined
#print(a,b)

#Deleting the variables -->del
#del a
#print(a)
#del a,b
#print(a,b)

#Punctuators -->ArithmeticError [](Lists),(tuples),{}(Dict,sets)
name = 'Gowtham varma';age = 22;course = 'Data_Analysis'
print(name,age,course,sep=',')

#Datatypes -->Numeric (int,float,complex),boolean,None
           #--->Sequences --->Lists,Tuples,Sets,Strings,Frozensets,mapping(dict)


#Numeric type-->int,float,complex

#int datatype --> quantity,age..
age=22
print(age)
print(type(age)) #type --> returns the datatype of object

print(type(234))

#quantity = 03 #it is not allowed
#print(quantity)

#float datatype --> temp,salary,price
price = 750.24;discount = 2.5
print(price,discount,sep=',')
print(type(price))

#complex -->combination of real and img
i2 = 4
data = 5 + i2
print(data)

data = 5+2j #j is imag representation
print(data)
print(type(data))

#Boolean --> True / false

valid = True
print(type(valid))

#error = false
#print(type(error))

#TypeCasting --> Converting one type to another type
#Python by default follows Implict type (we need not mention the datatype)

#We will go for Explict Conversation

#Every built-in datatype is a built-in function
int,float,complex,bool

#Typecasting of --> int -->float,complex,bool

age = 35
print(type(age))
b= float(age)
print(b)
c= complex(age)
print(c)
d= bool(age)
print(d)
e=bool(0)
print(e)


#float --> Typecasting

weight= 68.5
print(type(weight))
b = int(weight)
print(b)
c = complex(weight)
print(c)
d = bool(weight)
print(d)


#complex  ---> Typecasting
hr=7+8j
print(hr)
print(type(hr))
#b = int(hr) #TypeError
#print(hr)
#c = float(hr)
#print(c)
d = bool(hr)
print(d)
print(type(hr))


e = int(float(bool(60)))
print(e)
'''
f = 49+3.5+56+5j+True
print(f)

