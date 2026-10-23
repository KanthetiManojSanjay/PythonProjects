'''
Doesn’t allow duplicates
Allows heterogenous data
Ordering is not guaranteed so can’t perform indexing, slicing, repetition
'''

s={1,2,"sanjay",1}
print(s)
print(type(s))

s.update([3,4]) # To add new elements
print(s)

# As set doesn't maintain insertion order so we can't do indexing, slicing & repetition same as list


s.remove(1)
print(s)

f= frozenset(s) # To convert set to frozen set
print(f)
print(type(f))

