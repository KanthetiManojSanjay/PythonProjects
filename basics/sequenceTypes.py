s="You are awesome"
print(s)

s1="""You are the 
creator of 
your destiny"""
print(s1)

#Indexing
print(s[0])

# Repetition
print(s*2)

#Length
print(len(s))

# Slicing end index is excluded
print(s[0:3])
print(s[0:])
print(s[:8]) # start from start and go till 8th index
print(s[-3:-1]) # -1 indicates last index
print(s[0:9:2]) # Start from index 0 till index 9 with Step of 2
print(s[::-1]) # Reverse the string

s2="  You are awesome  "
print(s2.strip()) # Strips white spaces before and end
print(s2.lstrip()) # Strips only at left side
print(s2.rstrip()) # Strips only at right side

print(s2.find("awe")) # Returns index where awe started in s2 string
# Returns index where awe started in s2 string.Search starts from 0 and go till index 8. If it couldn't find then it returns -1
print(s2.find("awe",0,8))
print(s2.count('a'))
print(s2.replace("awe","super"))
print(s2.upper())
print(s2.lower())
print(s2.title())
