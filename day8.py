# STRINGS --> GROUP OF CHARACTERS, WE USE  SINGLE O DOUBLE OR TRIPLE QUOTES
#FOR REPRESENTATION OF STRINGS...
#STRINGS ARE IMMUTABLE , ORDERED, INDEXED COLLECTION
#SPACE IS ALSO A CHARACTER
name = 'codegnan'
'''
print(name)
print(type(name))
print(len(name)) #LEN--> RETURNS THE NUMBER OF ITEMS IN CONTAINER
'''

#index() --> fetch the object (position) starts at 0 and ends at len(obj)
#we use [] representation
'''
print(name[0])
print(name[5])
#print(name[25]) indexerror --> as its out of range
'''
#Negative indexing --> -1 to len(obj) count from last to first
print(name[-5])

#SLICING --> we can access group of characters(objects)
# we use [start:end] start default --> 0, start is included ,end is excluded 

'''
print(name[:]) # returns entire strin
print(name[0:])
print(name[:4])# starts at 0th index 
print(name[1:5])
print(name[:6])

print(name[7:3])#returns empty string because its immutable
'''
#Slicing is applicable from lower index to higher index'
'''
name = "python"
print(name[:-4])
print(name[-5:-1])
#print 'on' from above string
print(name[4:6])
print(name[-2:])
print(name[1:-2])
'''
#STRIDING --> [start:end:step]
'''
course = 'dataanalysis'
print(course[:4])
print(course[::2])
print(course[1:6:3])
print(course[2::3])
print(course[::-1])
print(course[::-2])
'''
#task : workout with all possibilities of slicing and striding on a example
name= 'codegnan'
#name[3] = 'w' strings are immutable

#operations on strings--> indexing,concatenaton,repetition
print(name*3)
print("*" *3)

#concatenation --> combining strings
'''
data = "saketh" + "raj" + " " + "python"
print(data)
print('code' in 'codegnan')

for i in 'codegnan':
    print(i, ':')
for i in 'codegnan':
    print(i,end=' ')
'''
name='dataCodegnan'
#bulit-in function --> len(),min(),max(),sorted()
'''
print(len(name))
print(min(name))
print(ord('A'))
print(ord('a'))
print(ord('5'))
print(max(name))
print(chr(98))
print(sorted(name)) #return a list by sorting all elements
'''
#Methods on strings --> case-conversions, finding/searching...
name = 'codeGnan data'
#case-conversion -->upper(),lower(),title(),capitalize()
a = name.upper()
print(a)
b = name.lower()
print(b)
#capitalize()--> converts first letter to uppercase
c = name.capitalize()
print(c)
#title --> converts every work first letter to uppercase
d = name.title()
print(d)

#TASK : A B C D E F G H I J K L M N O P Q R S T U  V W X Y Z
#USE LOOPS AND STRINGS TO RETURN A-Z

for i in range(65,91):
    print(chr(i),end = ' ')








