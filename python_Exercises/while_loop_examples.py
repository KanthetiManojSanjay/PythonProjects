i = 0

while i < 11:
    print(i)
    i += 1


def print_squares_of_numbers_below(limit):
    i = 1
    while i * i < limit:
        print(i * i, end=' ')
        i += 1
    print()


print_squares_of_numbers_below(100)

number = int(input('Enter a number'))
while number >= 0:
    print(f'cube is {number ** 3}')
    number = int(input('Enter a number'))
