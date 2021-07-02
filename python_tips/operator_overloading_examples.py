from functools import total_ordering


@total_ordering  # to reduce redudancy
class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        return Money(self.currency, self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.currency, self.amount - other.amount)

    def __repr__(self):
        return repr((self.currency, self.amount))

    def __eq__(self, other):
        return ((self.currency, self.amount) == (other.currency, other.amount))

    # def __ne__(self, other):
    #     return ((self.currency, self.amount) != (
    #         other.currency, other.amount))  # not needed as we already implemented equals method above

    def __gt__(self, other):
        return ((self.currency, self.amount) > (other.currency, other.amount))


# If we use total_ordering then eq & any one of other is enough. remaining methods(lt,gt ..etc) need not be explicitly overloaded
"""
    def __lt__(self, other):
        return ((self.currency, self.amount) < (other.currency, other.amount))

    def __ge__(self, other):
        return ((self.currency, self.amount) >= (other.currency, other.amount))

    def __le__(self, other):
        return ((self.currency, self.amount) <= (other.currency, other.amount))
"""

amount1 = Money('EUR', 10)
amount2 = Money('EUR', 20)
amount3 = Money('EUR', 10)

print(amount1 + amount2)

print(amount2 - amount1)

print(amount1 == amount2)
print(amount1 != amount2)
print(amount1 == amount3)

print(amount1 > amount2)
print(amount1 > amount3)
print(amount2 > amount3)

print(amount1 >= amount2)
print(amount1 >= amount3)
print(amount2 >= amount3)
