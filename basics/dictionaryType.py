dict1={1:"john", 2:"bob"}
print(dict1)
print(dict1.items())

k=dict1.keys()
for i in k:print(i)

v=dict1.values()
for i in v:print(i)

print(dict1[1]) # to extract value of key 2

del dict1[2] # to delete key value pair with key as 2
print(dict1)