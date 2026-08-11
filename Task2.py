#Write a program to calculate the score of a batsman
#[4,6,1,0,2,4,0,6]
'''
runs = [4,6,1,0,2,4,0,6]
total_score = 0
boundaries = 0
dot_balls = 0

for i in runs:
    total_score +=i
    
    if i== 4 or i == 6 :
        boundaries +=1
    elif i == 0:
        dot_balls +=1
        
print('Total Score:',total_score)
print('Boundaries:',boundaries)
print('Dot Balls:',dot_balls)
 '''

password = '1234'
max_attempt = 5
current_attempt = 0
while current_attempt < max_attempt:
    entered_pin =input('Enter the password:')
    if entered_pin == password:
        print('Phone Unlocked')
        break
    elif entered_pin != password:
        print('Try Again')
        current_attempt +=1
        

else:
    current_attempt > max_attempt
    print('Phone Locked Try After Few Hours')
'''  
password = '1234'
max_attempt = 5
current_attempt = 0
while current_attempt < max_attempt:
    entered_pin =input('Enter the password:')
    if entered_pin == password:
        print('Phone Unlocked')
        current_attempt=5
    else:
        current_attempt +=1   
if entered_pin != password:
    print("Phone lock")
    '''

