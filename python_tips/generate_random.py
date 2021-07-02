import random

print(random.random())

print(random.randint(1, 10))

print(random.randrange(1, 10, 2))

list = [2, 7, 9, 34, 56]
print(random.choice(list))  # pick randomly 1 value from list
print(random.choice('abcdef'))  # pick 1 character from given string

print(random.sample(list, 2))  # randomly pick 2 values from list
