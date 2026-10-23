a=100
b=50
print(a,b)
# To print the datatype of variable
print(type(a))

c=33.3
d=100.0
print(c,d)
print(type(d))

#
e= 3+4j
print(e)
print(type(e))

# Binary(use either b or B)
f=0b1010
print(f)
print(type(f))

# Hexadecimal(we can use either x or X)
g=0XFF
print(g)
print(type(g))

#Octal
h=0o10
print(h)
print(type(h))

# Bool type
i = True
print(i)
print(type(i))

print(9>8)

# To convert to int
j= int(c)
print(j)
print(type(j))

# To convert to float
k= float("22.5")
print(k)
print(type(k))

# To convert to binary
print(bin(10))
print(type(bin(10)))

# To convert to hexadecimal
print(hex(10))
print(type(hex(10)))

# To convert to octal
print(oct(10))
print(type(oct(10)))

# python is case sensitive language. Identifiers can start with alphanumeric & underscore only
# _ before variableName or methodName means it is private.
# If __ (double underscore) is used before then it is really private. It is just a convention used for developer
# __init__  Example of magic function