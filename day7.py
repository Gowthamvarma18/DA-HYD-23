'''
Usage of else with for --> the else keyword will only be exicuted when the loop is 

'''

#for with else...
'''
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
        print(longest_streak)
        #break 
    else:
        current_streak = 0 #streak breaks
else:
    print(f'Longest_streak is:{longest_streak}')

#in this case when the entire loop execution is done we get result of else block
'''
#same program with break usage
'''
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
        print(f'Longest Streak is {longest_streak}')
        break 
    else:
        current_streak = 0 #streak breaks
else:
    print(f'Longest_streak is:{longest_streak}')
print('Execution done')
'''

#for-else with notifications scenario
'''
#notifications = [0,0,1,0]
notifications = list(map(int,input('Enter the values --> 0 or 1:').split(',')))
print(notifications)
#try to take notifications from user -->list of integers
for notifications in notifications:
    if notifications == 1:
        print('Unread Notification')
        break
else:
    print('All Caught Up')
    '''

#while -->it relies on condition,it will be completly executed until yhe condition is satisfied
'''
syntax while:

while<condition>:
     statement(s)....
     .......
     ......

while True:
    print('yes')
'''
#It runs an infinite loop we need to press Ctrl+c (keyboard interrupt)
'''
i = 10 #initilised statement
while i>=1:
      print(i)
      i=i-1#decrimrnt i-=1
'''    '''
i = 0
while i<=10:
    print(10-i)
    i = i + 1
    '''

#banking scenario -->PIN authentication if more than 3 attempts
#Account locked

pin = '2345'
max_attempts = 3
current_attempt=0
while current_attempt < max_attempts:
    entered_pin = input('Enter The ATM PIN:')
    if entered_pin == pin :
        print('Login Successful')
        break
        #continue #it holds for this condition and skips to the next part
    else:
        print('Enterd pin is wrong try again carefully')
        current_attempt += 1
else:
    print('Account Locked,try again 24 hours')
     
        
    
    
        
