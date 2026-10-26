class OverTheLimitException(Exception):
    def __init__(self, msg):
        self.message = msg


def withdrawl(amount):
    if (amount > 500):
        raise OverTheLimitException("You cannot withdraw more than 500 per day")

withdrawl(600)