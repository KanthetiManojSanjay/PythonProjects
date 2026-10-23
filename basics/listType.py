#List
lst = [1,2,"sanjay"]
print(lst)
print(lst[2]) # To access value at an index
print(lst[2:5]) # To slice list endIndex will be excluded in the output
print(lst*3)  # To repeat list
print(len(list)) # To get length of list
print(lst.append(40)) # To add value
print(lst.remove("sanjay")) # To remove value
del(lst[1]) # To delete value at an index. Here del is a builtin function
print(lst)

# lst.clear() # To clear all elements in list
# print(lst)

print(max(lst))
print(min(lst))

lst.insert(3,99) # To add value at a index
print(lst)

lst.sort() # To sort index
lst.sort(reverse=True) # To sort index