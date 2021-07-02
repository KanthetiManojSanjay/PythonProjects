
a=5
b=2

try:
    print('resource open')
    print(a/b)
    k=int(input("enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("Hey, you cannot divide a number by zero",e)
except ValueError as e:
    print("Invalid input",e)
except Exception as e:
    print("Other errors",e)
finally:
    print("resource closed")