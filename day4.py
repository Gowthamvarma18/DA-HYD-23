'''
Identity Operators -->checks the identity  of an object --> id()
'''

'''
a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print(a is c)
print(5 == 5 )


a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
#As we have Lists (Mutable Collections)
#ids whereas values are same 
print(c is a) #output False
print(c == a) #output True
print(a is not c)


#Bitwise Operators --> we perform bitwise operators over operands
#& (and) , | (or),^(XOR),shifting operators (<<,>>)
#Number will be converted to binary format

print(5&3) #both 5 and 3 to be converted binary and bitwise and is performed

print(5|3) #bitwise or

print(5^3) #bitwise xor

print (5 and 3) # here and is logical operator checks for both existance
#returns 5 in above case

print(5 or 3) #return 3 in the case


#Leftshift Operator << ,Right shift operator >>

print(5<1) #false Comparision
print(5<<1) #Left shift operation by 1 position 
print(5>>1) #Right shift operation


print(15 << 2) #convert 15 to binary and perform 2 times left shifting

print(15 >> 2) #same 2 times right shifting


#Input Formating --. input(),int(input()),float(input())
#You know -->single input
#2 or 3 inputs --> map()
#group of integers --> list(map(int,input().split('<'))

names = input('Enter the names:').split(',')
print(names)

name1,name2 = map(str,input('enter the friends names:').split(','))
print(name1,name2)
'''

#Tokens --> Numeric Datatypes --> Operartors -->Flow of the program
#Control Block Statements --->they control the flow of the program
#when to execute,how to execute
#Condition Statements -->ArithmeticError if,else,elif(rely on condition to be executed)
#repetition Statements --->if usage
'''
Syntax :

if <condition>:
    statement(s)...
    .......

#age = 15
age = int(input('enter the age:'))
if age >=18:
    print('your age is:',age)
    
age = int(input('enter your age'))
if age >=18 and age in [19,20,21]:
    print('your age is:',age)
print(age)

#else:
     statement(s)..

if-else usage as below:

if <condition>;
    statement(s)...
    ......
'''

#Vote Eligibility -> To check his/her voter eligibilty and give access...

age = int(input('enetr the age:'))
if age>=18:
    print('You have voter eligibility and age is',age)
    print('Access Granted')
else:
    age = 18-age
    print('You Dont Have Eligibility Wait For ',age,'Years To Get Eligibility')

'''
task : Student marks and grade analayzer
90 - 100 ---> A
80 - 89 ---> B
70 - 79 ---> C
60 - 69 --> 'D'
>60 --> Fail
#also -ve cases should not be allowed and marks shouldnt be greater than 100
    


          
