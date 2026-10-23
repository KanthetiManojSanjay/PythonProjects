'''
Once created then cant be modified.
It maintains insertion order.
Allows duplicates and supports heterogenous data
() are optional but if only one value is there comma is mandatory at the end
'''


t=(1)
print(type(t))

t1=(2,)
print(type(t1))

t2=(1,2,'xyz','x')

# As tuple maintain insertion order so we can do indexing, slicing & repetition same as list
print(t2*3) # To repeat
print(t2.count(2)) # To know count of value in tuple
print(t2.index('xyz'))

# we can also use max, min, len as they dont change tuple
lst=[1,2,"3"]
print(type(lst))
t3 = tuple(lst)
print(type(t3))
print(t3)


'''
Both list and tuple
Similarity
1 Hold heterogenous data
2.Maintain insertion order
3.Duplicates are allowed

Difference
 1. List - Mutable so can’t be used as key for dictionary as key for dict should be hashable and immutable
2.Tuple - Immutable hence can be used as key for dict
'''

