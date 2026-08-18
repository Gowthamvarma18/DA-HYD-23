'''
Tokens.Datatypes -->Control Flow Statements -->if,elif,else,for,while,break,continue

Procedure Oriented  programming

Functions --> A function is a block of code which performs a specific task
its a reusble group of statements where we define using
def keyword
len()
min()
max()
print()
sorted()
eval()
map()

Advatages --> Code reusability,code maintainability,ease of debuggin
avoiding code duplication,modularity

def fname(parameters):          Function defn
    """Doc String"""            Description
    statements(s).....          Function Body
    ...........
    return value(s).....
fname(args)                     Function Call
'''
#To Perform sum of given objects
'''
def add(a,b):
    """Sum of objects"""
    c= a+b
    return c
print(add(12,3)) #Addition
print(add('code','gnan'))  #Concatenation
print(add([12,5],[12,34])) #Merging
c,d = map(int,input('Enter the values:').split(','))
print(c,d)
print(add(c,d))
  

def add(a,b):
    """Sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34)) #It returns result along with None

name,age,salary = 'Saketh',32,50000
#Usage of return

def details():
    #return name,age,salary
    #return 'Codegnan'
    #return 23+34+45
    return       #It returns None as output 
print(details())

There are 5 types of arguments

---> Positional Arguments
---> Default arguments
---> Keyword arguments
---> variable length arguments(*args)
---> Keyword variable length arguments(**kwargs)
'''
#Positional Arguments --> Number of arguments in function defn should
#match with functional call (order has to be maintained)
#print(len(123,234)) this is as per built in len(obj) will accept one argument
'''
def details(name,place):
    """To store the details"""
    #name = 'Codegnan'
    #place = 'Hyderbad'
    #return name,place
    print(f'Name is {name}')
    print(f'Place is {place}')
#print(details('Saketh','Codegnan'))
#print(details('Sai','Vizag'))
#print(details('Vizag','Sai',32)) #raises TypeError as only 2 arguements
c,d = map(str,input('Enter the values').split(','))
details(c,d)
'''
#Default arguments -->we can make arguments as default but not first arguments as default
'''
#def grocery(item,price=35):
#def grocery(item = 'cheese',price = 100): #we can make all args as default
#def grocery(item='Burger',price): #non default always follows default
    """Usage of default arguments"""
    print(f'The Item is {item} and price is {price}')

grocery('Milk',32)
#grocery(32,'Milk')
grocery('Bread')  #By default we have given price as 35
grocery() #as both item and price as default arguments
'''

#Keywords arguments -->Whenever we want to specify the name of argument
def employee(name,salary,role):
    """Keyword argument usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary}')
employee('Sai',20000,'Admin')
employee(salary=25000,role='Frontdesk',name='Asha')
employee('Akash',25000,'IT','Cognizant')


















