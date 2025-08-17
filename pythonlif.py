# single comment  


''' multi comment'''

'''variables'''
# a=10
# print(a)

# a=10,20,40
# print(a)  

# a, b, c =10
# print(a, b, c) not running

# a=b=c= 1,9,6
# print(a)

# a,b,c=10,20,30
# print(a,b,c)


'''DATA TYPE----> TYPE OF THE VALUE'''

''' BASIC DATATYPES'''
'''
INT
FLOAT
BOOLEAN
STRING
COMPLEX
'''

# a=10
# b=-10
# print(type(a),type(b))

# a=True
# b=False
# print(type(a),type(b))


# a=4.44
# print(type(a))

# a="amulya"
# print(type(a))

# a=4+4j
# print(type(a))

'''TYPE CONVERSION '''
''' data lose----> explict type conversion'''
'''no data lose ---->implict type conversion'''

# a=4
# print(float(a))

# a=4.07
# print(int(a))

'''CONDITION STATEMENTS'''
'''
IF
ELSE
ELIF
NESTED IF
'''

# age=18
# if age > 18:
#     print("you are vote")
# elif age == 18:
#     print("you can vote")
# else:
#     print("you are not vote")  


# n=int(input())
# if n%11==0:
#     if n%11==1:
#         print("special eleven")
# else:
#     print("normal num")        


# n=input()
# if n==True:
#     if n==False:
#         print("hii")
#     else:
#         print("heyy") 
# elif n==False:
#     print("hello nana")


'''LOOPING STATEMENTS'''
'''RANGE METHOD AND EACH METHOD'''
 
 
# for i in range(0,10):
#     print(i)

# for i in range(0,10,2):
#     print(i)  

# a=[2,3,4,5,6,7]
# for i in a:
#     print(i)

# a="ammuamulya"
# for i in a:
#     print(i)

# while True:
#     print("hi")

# a=9
# while a<15:
#     print("hi",a)
#     a+=1

# for i in range(0,100):
#     for j in range(0,100):
#         print(i+j)

'''JUMPING STATEMENTS'''
'''
PASS
BREAK
CONTINE
'''

# for i in range(0,10):
#     pass


# a="python language"
# for i in a:
#     if i=="l":
#         break
#         print(i)

# a="pythonlanguage"
# for i in a:
#     if a=="l":
#         continue
#         print(i)

'''STRING AND STRING METHODS'''

# a='ammu'
# b="ammu"
# c='''ammu'''
# print(type(a), type(b), type(c))

'''STRING METHODS'''

'''
lower()
upper()
isupper()
islower()
split()
strip()
Rstrip()
Lstrip()
count()
index()
removeperfix()
removesuffix()
replace(old one,new one)
find()
starts with()
ends with()
'''

# a="python language"
# print(a.upper())

# a="APYTHON LANGUAGE"
# print(a.lower())

# a="python language"
# print(a.isupper())


# a="APYTHON LANGUAGE"
# print(a.islower())


# a="python language"
# print(a.split("/"))


# a="python language"
# print(a.count(a))


# a="python language"
# print(a.index(a))


# a="python language"
# print(a.find(a))


# a="      python language      "
# print(a.strip())
# print(a.Rstrip())
# print(a.Lstrip())



# a="python language"
# print(a.removeprefix(a))
# print(a.removesuffix(a))

# a="python language"
# print(a.replace("language","programmming"))


# a="python language"
# print(a.endswith("e"))
# print(a.startswith("p"))


'''STRING SLICING [start:end:skip]'''

# a="python is programming language"
# print(a[0:5])
# print(a[0:10:2])
# print(a[:-1])  
# print(a[:-2])
# print(a[:-1:4])


'''STRING INDEXING'''
# a="python is programming language"
# print(a[2])
# print(a[-1])
# print(a[10])

'''LIST METHODS []   ---->  pre define methods'''
'''
append
extend
count
sort
clear
insert
pop
remove
index
'''
''' -----> builtin methods

sum 
min
max
len

'''


'''MUTABLE DATA TYPE ----> CHANGEALBE'''


# a=[5,6,7,8,9,"amulya"]
# print(type(a))
# print(a[2])
# print(a[-1])
# print(a[0:7:2])


# a=[3,5,7,9,1,,3,"ammulu","python"]
# print(a.append("program"))
# print(a.extend([1,3,5,6,"ammu"]))
# print(a.count(3))
# print(a.remove(3))
# print(a.pop(3))
# print(a.index(3))


# a=[3,5,7,9,1,,3,"ammulu","python"]
# for i in a:
#     print(i)

'''TUPLE DATA TYPE ( )'''
''' IMMUTABLE--->NO CHANGES'''

'''tuple operations'''
'''
concatenation
iteration
membership operation
identity operation
repetation
'''
# a=(1,2,3,4,5,6)
# print(type(a))
# print(a[-1])
# print(a[0:5:2])
# print(max(a))
# print(min(a))
# print(sum(a))
# print(len(a))

# a=(1,2,3)
# b=(4,5,6)
# print(a+b)

# a=(1,2,3,4,5,6)
# print(a*5)
# for i in c:
#     print(i)

# print(2 in a)
# print(11 not in a)

'''DICTIONARY DATA TYPE {KEY : VALUE, ..... }'''
''' IMMUTABLE--->NO CHANGES   KEY ----> IMMUTABLE , VALUES---->MUTABLE'''
'''NO SLICING AND NO INDEX'''
'''METHODS'''
'''
get
update
values
keys
item
'''

# a={1:555,'g':123,6:888,'r':999}
# print(type(a))
# # print(a[1]) key calling
# print(a.get(1))
# print(a.keys())
# print(a.values())
# print(a.items())
# print(a.update({'a':777}))


# for i,j in {1:555,'g':123,6:888,'r':999}.items():
#     print(i,j)


'''SET { ELEMENTS AND NO DUPLICATES} UNORDERED'''
'''NO INDEX AND NO SLICING'''
''' SET METHODS'''
'''
add
update
pop
remove
'''
'''SET OPERATIONS'''
'''
UNION
INTERSECTION
DIFFERENCE
ISSUBSET
ISSUPERSET
'''

# s={1,3,4,2,14,7,8,3,2,9}
# print(s)
# s.add(123)
# print(s)
# s.update({1,2,366})
# print(s)
# s.pop()
# s.remove(2)
# print(s)


'''FUNCTION----> BLOCK OF CODE,RUN WHEN ITS CALLED'''
'''SYNTAX ---->def--->keyword, function name():'''

# def add(a,b):
#     return a+b
# print(add(1,2))

# def func(a,b,c):# function defination   
#     print("this is function:",a,b,c) # function body
# func(1,2,3)    #function call

# '''orbitary arguments ----> TUPLE'''

# def func(*a):# function defination   
#     print("this is function:",a) # function body
# func(1,2,3)    #function call

# '''KEYWORS ARGUMENTS ---->DICTIONARY'''

# def func(**a):# function defination   
#     print("this is function:",a) # function body
# func(a=1,b=2) 

# '''NESTED FUNCTIONS'''

# def outer():
#     print("outer function")
#     def inner():
#         print("inner function")
#     inner()
# outer()


# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)

'''FILE HANDLING ----> READING,WRITING,CREATING,DELETING'''

'''MODES'''
'''

OPEN

r--read mode
w--write mode (trucate)
a--append mode
r+--read write
w+--write read (truncate)

CLOSE
'''

# s=open('demo2.txt',mode='r')
# print(s.read())
# s.close()



'''CLASS ---> template or blue print of object'''
'''class class_name():'''
'''OBJECT--->physical entity--->we can create no of objects for class
object----> data and function
syntax= object name = class name()

access obj---> objectname.method()
'''






