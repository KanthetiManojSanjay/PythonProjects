def print_hello_world_multiple_times(times):
    print(times)
    for i in range(1,times+1):
        print('Hello world')


def print_squares_of_numbers_upto(n):
    for i in range(1,n+1):
        print(i*i)


def print_squares_of_even_numbers_upto(n):
    for i in range(2,n+1,2):
        print(i*i)


def print_numbers_in_reverse(n):
    for i in range(n,0,-1):
        print(i)

def print_multiplication_table(table=5,start=1,end=10):
    for i in range(start,end+1):
        print(f"{table} X {i} = {table*i}")

def sum_of_two_numbers(number1,number2):
    sum=number1+number2
    return sum

#print_hello_world_multiple_times(4)

#print_squares_of_numbers_upto(10)

#print_squares_of_even_numbers_upto(10)

#print_numbers_in_reverse(10)

#print_multiplication_table(7,1,10)

#print_multiplication_table(7)

#print(sum_of_two_numbers(5,6))

#Python is strongly typed & Dynamic language
