'''
Strings --> CaseConverstion,Searching&Findiing,String testing methods
replace,Space removal
'''
#Searching,Finding,Replacing,Joining...
'''
a = 'Codegnan'

print(len(a))
print(min(a))
print(max(a))

b = a.index('g') #it returns the index position
print(b)
c = a.index('n')# it returns only the first occurance
print(c)
d = a.index('n',6)# it returns the next occurance
print(d)
#e = a.index(n,8)
#print(e)
#f = a.index('t')# ValueError
#print(f)
g = a.index('n',1,4)
print(g)
'''
#rindex() --> returns last occurance
'''
b = a.rindex('g')
print(b)
c = a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d = a.rindex('n',8)#it returns ValueError
#print(d)
'''
#count() -->returns the number of items object is repeating
'''
print ('Codegnan'.count('n'))
print('Code'.count('w')) #it returns 0 as we dont have 'w' in 'Code'
print('Cakshjasaksajs'.count('a'))
'''
#find () -->firts occurance but it avoid error returns -1 if substring is not found
'''
print('codegnan'.find('r'))

print('codegnan'.find('n'))

print('codegnan'.rfind('n'))

a = 'DataAnanlysis'
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))
'''
#Replacing,Splitting,Joining

#Stings are Immutable
'''
a = 'Codegnan'
#a[4] = 's'
a.replace('g','s')
print(a)
a = a.replace('g','s')
print(a)
print('gowtham_varma'.replace('_',' '))


a = 'code saketh python'
b = a.split() #by default if we have space it splits
print(b)
print(len(b))
c = 'code,saketh,python'
d = c.split()
print(d)
e = c.split(',')
print(e)
'''

#join(iterable) -->concatentate any number of strings
'''
a = 'code'
b = 'gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('saketh'))
print(' '.join('saketh'))
'''

#String testing methods (boolean)
#isalpha(),isalnum(),isupper(),islower().....
'''
a = 'Codegnan123'
print(a.isalnum())# returns True for alphanumeric strings else False
b = 'Codegnan'
print(b.isalnum())
print(a.isalpha()) #returns True only for alphabets
print(a.isdigit()) #returns True only for digit string
print('8989898989'.isdigit())
print('2345'.isnumeric()) #this has uppervedge (numbers,fractions,romans)
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('h'))


print('codegnan'.islower())#returns True for all the lowercase
print('Codegnan'.isupper())#returns True for all upperrcase
print('Codegnan Python'.istitle())
'''

#Space removal --> strip() (removes leading and trailing spaces)
'''
a = ' codegnan '
print(a.strip())
b = input('Enter the string:').strip().upper()
print(b)
'''
#zfill() filling with zeros as per the given numeric string
print ('234'.zfill(4))
print('234'.zfill(7))
#Center(),ljust(),rjust() -->Alignment  of string (check length and then modify the width accordingly)
print('hai'.center(6))
print('hai'.center(7,'-'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))










