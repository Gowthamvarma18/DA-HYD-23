'''
task : Student marks and grade analayzer
90 - 100 ---> A
80 - 89 ---> B
70 - 79 ---> C
60 - 69 --> 'D'
>60 --> Fail
#also -ve cases should not be allowed and marks shouldnt be greater than 100
'''
'''
marks = int(input('Enter The Marks'))
   
if marks <0 or marks >100:
    print('*Invalid*')

if marks >=90 and marks <=100:
    print('you got grade a')

if marks >=80 and marks <=89:
    print('you got grade b')

if marks  >=70 and marks <=79:
    print('you got grade c')

else:
    marks <60 and marks >=0 
    print('you failed your exam')
'''
'''    
marks = int(input('Enter The Marks'))

while True:   
 if marks >0 and marks <=100:

  if marks >=90 and marks <=100:
    print('You got grade A')

  if marks >=80 and marks < 90:
    print('You got grade B')

  if marks  >=70 and marks < 80:
    print('You got grade C')

  if marks >=60 and marks < 70:
    print('You got grade D')

  if marks <60:
    print('You Failed Your Exam')

else:
     print('You should not enter the negative marks or above 100')

#elif keyword -->if -else-elif
'''
'''
if<condition>:
  statement(s)...
elif <condition2>
   statement(s)...
elif <condition.:
    statement(s)
else:
    statement(s)

    .......
'''

'''
marks = int(input('Enter The Marks:'))
if marks <0 or marks >100:
    print('*INVALID*')
elif marks >=90: 
    print('You Got A Grade:',marks)
    print('*Passed*')
elif marks >=80:
    print('You Got B Grade:',marks)
    print('*Passed*')
elif marks >=70:
    print('You Got C Grade:',marks)
    print('*Passed*')
elif marks >=60:
    print('You Got D Grade:',marks)
    print('*Passed*')
else:
    marks < 60
    print('You Failed Your Exam',marks)
'''
'''
marks = int(input('Enter the student marks:'))
if marks >= 100:
    print('entered values should be greater than 1 and less than 100')
elif marks >=90 and marks <=100:
     print('user got grade a')
elif marks >=80 and marks <=89:
     print('user got garde b')
elif marks >=70 and marks <=79:
     print('user got grade c')
elif marks >=60 and marks <=69:
     print('user got grade d')
elif marks <60 and marks >=0:
     print('you faliled exam')
else :
    print('-ve values are not valid')
'''
'''
#tast . try same usecase with if-elif-else


# voter elgibility 










age = int(input('Enter The Age'))
if age>=18 and age <=100:
    print('------ User has vote Eligibility -----')
    print('-------Access Granted--------')
elif age<18 and age >=0:
    print('-------User is not eligible to vote----')
    print('--------Access Denied-----')
else:
    print('only positive values less than 100 are acceptable')


prefer if-elif-else....
'''

#output ---> print() -->we acn pass any values also use sep and end
#out

'''
a,b = 7,9
print(a)
print(b)
print(a,b)
name = 'Codegnan';batch = 'DataAnalysis'
print(name,batch)#by default sep is having space
print(name,batch,sep=',')
print(name,batch,sep='------>')
#end='\n',\t --->tab space
print(name,batch,end='\t')
print(a,b,end='')
print('hyderbad')
'''

name='codegnan';age=7;batch='DA-023';place='Hyderbad'
'''#Usage of commas
print(batch,'is in',place,'age is',age,'years')
#Old style formating --> %d -->integer,%s--->string,%f-->float
salary = 24253.256

print('his salary is %d'%(salary))
print('his salary is %f'%(salary))
print('his salary is %.1f'%(salary)) #%.1f ---> rounding to 1 decimal
'''
#.format()usage
print('{} is in {}'.format(name,place))#order matters

#fstring usage (more recommende)

print(f'{name} is in {place}')






    


















      

