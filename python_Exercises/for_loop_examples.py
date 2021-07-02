
for i in range(1,10):
    print(i)

for ch in 'Hello World':
    print(ch)

for word in 'Hello World'.split():
    print(word)

for item in (3,8,9):
    print(item)

def is_prime(number):
    if number<2:
        return False

    for i in range(2,number):
        if number%i==0:
            return False
    return True

print("Number is prime") if is_prime(11) else print("Number is not prime")

def sum_upto_N(number):
    sum=0
    for i in range(1,number+1):
        sum+=i

    return sum

print("Sum of the numbers is :"+str(sum_upto_N(4)))


def print_number_triangle(number):
    for i in range(1,number+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()

print_number_triangle(5)