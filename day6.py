'''
Control Statements --> control of Flow of execution of the program
                      --->Conditionla Statements --> if,elif,else...
                    --->Repetition Statements(Loops) --> for,while(for with else)
                                                           (while with else)
                    --->Jumping Statements --->break,continue,pass
'''
#Loops -->Loops are helpful for reprtition (Automative tasks)
#for keyword will be helpful to iterate over a sequence / range
#syntax for (for keyword):
'''
for <temp_var> in sequence/range:
     statement(s)...
     .....
'''
'''
#range(start,stop,step)
#by default range picks 0 as start value
for i in range(10):
    print(i)
    
#In above case we got 10 iterations
for i in range (1,10):
    #if i > 5:
        #print(f'Value of i is -->{i}')
   #Now i want to get only even numbers with above condition
    if i > 5 and i%2 ==0:
        print(f'Value of i is -->{i}')
    

#range(start,stop,step) -->here step --> interval..
for i in range(1,10,3):
    print(i)
    print('Done')
    

for i in range(10,1,-1):
    print(i)
    

#print -10 to -1
for i in range(-10,0,1):
    print(i)
    '''
'''
#[] --> we generally Lists
names = ['Gowtham','Varma','Raju']
print(len(names))# len(obj) --> returns the number of items in a container
for name in names:
    #print(name)
    #print(f'Student name is {name}')
    if name == 'Varma':
        print(f'Student name is {name}')
        '''
#Calculate the sum of first 10 numbers
#first understand your input --> range(11) -->10 numbers
#second understand your output --> sum (number)
# third we need to map the logic
'''
result = 0
for i in range (11):
    #print(i)
    #print(f'result is {i+i})
     result = result + i #result += i
     print(f'Now the result is{result}')
print(f'sum of 10 numbers is {result}')
'''
'''
# sum of even number
result = 0
for i in range(21):
    if i %2 == 0:
     result = result + i
print(f'the sum of number is {result}')

#  sum of odd number
result = 0
for i in range (21):
    if i %2 == 1:
        result = result + i
print(f'sum of number is{result}')
    '''

#Understand the loops usage with fitness streak example
#work_out -->,work_out_missed -->0

work_log = [0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
    #print(day)
       current_streak = current_streak + 1
       if current_streak > longest_streak:
        longest_streak = current_streak
        
    else:
        current_streak = 0 #streak breaks
print(f'Longest_streak is:{longest_streak}')
    

     

