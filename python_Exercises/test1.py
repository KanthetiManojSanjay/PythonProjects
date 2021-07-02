# from array import *
from numpy import *
from numpy import array
from functools import reduce
from Calc import *

#x=int(input())
""""
y=int(input())
z=x+y
print(z)

res=eval(input('Expression'))
print(res)

if True:
    print('hello')
    print('python')
print('Bye python')

"""

for i in range(2,11,1):
    if i%2==0:
        print('i value is',i)

##2
x=int(input("How many candies do you need?"))

i=1
avg=10
while i<=x:
    if i>avg:
        print('Out of stock')
        break
    print("Candy no: ",i)
    i+=1

print('Bye')

##3
for i in range(1,20):
    if i%3==0 or i%5==0:
        continue
    else:
        print(i)

##4
for i in range(1,11):
    if (i%2!=0):
        pass     # If you dont know what to put in this suite then mention as pass
    else:
        print(i)

##5
for i in range(4):
    for j in range(4-i):
        print('# ',end='')
    print()

##6
vals=array('i',[1,3,-6,9,2])

for i in range(len(vals)):
    print(vals[i])

for j in vals:
    print(j)

newArr=array(vals.typecode,(a*a for a in vals))

for e in newArr:
    print(e)

i=0
while i<len(newArr):
    print(newArr[i])
    i+=1

##7
arr=array('i',[])
n=int(input('Enter the length of the array'))
for i in range(n):
    x=int(input('Enter the next value'))
    arr.append(x)

print(arr)

val= int(input('Enter the value to be searched'))

k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1

print(arr.index(val))  #Alternative way

##8

arr= array([1,2,3,4][5,6,7,8])
print(arr)


##9

def greet():
    print("Hello")
    print("Good Morning")

greet()


def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)


sum(1,2,3,4,5)


def add(name,age=18):
    print(name)
    print(age)

add(name="sanjay")

def add2(name,age=18):
    print(name)
    print(age)

add2("sanjay",13)

def person(name,**data):   //keyworded variable length argument using **
    print(name)
    for i,j in data.items():
        print(i,j)


person('sanjay',age=20,city='Hyderabad',mobile=98765)

##10

a=10
def something():
    global a
    a=15
    print("in fun",a)

something()

print("outside",a)

print(id(a))
def something():
    a=15
    x=globals()['a']
    print(id(x))
    print("in fun",a)
    globals()['a']=3

something()

print("outside",a)

##11

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
list=[1,2,3,4,5,6,7,8,9]
e,o=count(list)
print("Even is: {} & odd is: {}" .format(e,o))


def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=5
res=fact(x)
print(res)



def fact2(n):
    if n==0:
        return 1
    return n*fact2(n-1)
result=fact2(4)
print("Recursion result is : ",result)

##12: Lambda/Anonymous
f=lambda a:a*a
result=f(5)
print("Anonymous/lambda: ",result)

def is_even(n):
    return n%2==0
nums=[3,4,6,7,9,8,1,5]
evens=list(filter(is_even,nums))
print(evens)

evens2=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens2))
sum=reduce(lambda m,n:m+n,doubles)
print(doubles)
print(sum)

##13:  Decorators
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    return inner

div=smart_div(div)
div(2,4)

##14 Modules
res=add(2,3)
print(res)

print("test starts")
