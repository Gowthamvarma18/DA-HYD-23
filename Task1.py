'''
products = list(map(int,input('Enter the price:').split(',')))
total = 0
for i in products:
    total = total+i
print(total)
'''

'''
password =input('Enter the password:')
upper = 0
lower = 0
digits = 0
special = 0
for i in password:
    if 'A' <= i <= 'Z':
        upper +=1
    elif 'a' <= i <= 'z':
        lower +=1
    elif '0' <= i <= '9':
        digits +=1
    else:
        special += 1
        
print('upper',upper)
print('lower:',lower)
print('digits:',digits)
print('special:',special)
'''
'''
email = input('Enter the username').split(',')
for mail in email:
    print(mail.split('@')[1])
'''




















                    
        
   
       

