class Player:
    count = 0

    def __init__(self, name):
        self.name = name
        Player.count += 1  # can access class/static variable using className only

    @staticmethod
    def get_count():
        return Player.count


messi = Player('Messi')
ronaldo = Player('Ronaldo')

# print(Player.count)
# print(messi.count) #use instance variable to only read static variable but not write bcz it creates instance variable
# print(ronaldo.count)

print(messi.get_count())
print(ronaldo.get_count())
print(Player.get_count())  # self willn't be there for staticmethods. better Use className to call staticMethods
