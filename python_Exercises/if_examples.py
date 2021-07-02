x=2

if x>3 and x<6:
    print(f"{x} is between 3 and 6")
else:
    print(f"{x} is NOT between 3 and 6")

number=5
if(number%2==0):
    isEven=True
else:
    isEven=False
print(isEven)

#simpler way of if-else expression
isEven=True if number%2==0 else False
print(isEven)


x=int(input("Enter a Number"))
if x==1:
    print(f"{x} is 1")
    print("this is part of if")
elif x==2:
    print(f"{x} is 2")
    print("this is part of elif")
else:
    print(f"{x} is NOT 1 or 2")
    print("this is part of else")