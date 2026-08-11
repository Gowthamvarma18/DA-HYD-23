'''
user = input('Enter Sentence:')
method = ['upper','lower','title','capitalize','swapcase']
for i in method:
    
    if i == 'upper':
        print('Upper:',user.upper())
    elif i == 'lower':
        print('Lower:',user.lower())
    elif i == 'title':
        print('Title:',user.title())
    elif i == 'capitalize':
        print('Capitalize:',user.capitalize())
    else:
        i == 'swapcase'
        print('Swapcase:',user.swapcase())
       
if user.isupper():
    print('The sentence is upper case',True )
else:
    print('The sentence is upper case',False)
if user.islower():
    print('The sentence is lower case',True)
else:
    print('The sentence is lower case',False)
if user.istitle():
    print('The sentence is title ',True)
else:
    print('The sentence is title',False)
'''

while (True):
    username = input("enter the username:")
    if username == "quit":
        break
    if username.isalnum():
        print("username contains letter and numbers")
    else :
        print("username doesn't contains letter and numbers")
    if username[0].isalpha():
        print("username begins with letter")
    else :
        print("username not start letter")
    if username.isidentifier():
        print("username contains valid python identifier")
    else :
        print("username contains invalid")
    if username.isascii():
        print("username contains ascii value")
    else:
        print("username doesn't contains ascii value")

    

            
    
