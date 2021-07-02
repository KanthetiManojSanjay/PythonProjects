from enum import Enum


class Currency(Enum):
    USD = 1
    EUR = 2
    INR = 3


for currency in Currency:
    print(currency)
# print(Currency.USD)
# print(Currency.EUR)
# print(Currency.INR)

print(Currency(1))

print(Currency(1).name)
print(Currency(1).value)
