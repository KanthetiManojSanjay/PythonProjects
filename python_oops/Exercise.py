marks = [12, 23, 45, 67, 80]

print(max(marks))
print(min(marks))
print(len(marks))

marks.append(56)
print(marks)

marks.insert(2, 60)
print(marks)

marks.remove(60)
print(marks)

print(23 in marks)

print(marks.index(45))

# for mark in marks:
#     print(mark)

animals = ['Cat', 'Dog', 'Elephant']
print(len(animals))

animals.append('Fish')  # can add only 1 item
print(animals)

animals.remove('Dog')  # remove specific element
print(animals)

print(animals[0])

del animals[2]  # remove based on index
print(animals)

animals.extend('Fish')
print(animals)

animals.extend(['Horse', 'Giraffe'])  # can add multiple items
print(animals)

animals = animals + ['Jackal', 'Kangaroo']
print(animals)

animals.append(10)  # No type restriction for list
print(animals)

# Slicing
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

print(numbers[2])
print(len(numbers))
print(numbers[2:6])
print(numbers[:6])
print(numbers[3:])
print(numbers[1:8:2])
print(numbers[1:8:3])
print(numbers[::3])
print(numbers[::-1])  # Reverse
print(numbers[::-3])
del numbers[5:7]
print(numbers)
numbers[3:7] = [3, 4, 5, 6]
print(numbers)

numbers.reverse()  # Inplace reverse
print(numbers)

for number in reversed(numbers):
    print(number)

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers.sort()  # Inplace sort - original list is modified
print(numbers)

for number in sorted(numbers):  # Willn't modify original list
    print(number)

for number in sorted(numbers, key=len):  # sort based on length
    print(number)

for number in sorted(numbers, key=len, reverse=True):
    print(number)

numbers.sort(key=len)
print(numbers)

numbers.sort(key=len, reverse=True)
print(numbers)

# list as stack - LIFO
num = []
num.append(1)
num.append(2)
num.append(3)
num.append(4)
num.pop()
print(num)

# list as queue - FIFO
num = []
num.append(1)
num.append(2)
num.append(3)
num.append(4)
num.pop(0)
print(num)

# List comprehension
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers_length_four = [number for number in numbers if len(number) == 4]
print(numbers_length_four)
