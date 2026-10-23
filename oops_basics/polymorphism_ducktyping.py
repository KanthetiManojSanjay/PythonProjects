class Duck:
    def talk(self):
        print("Quack Quack")


class Human:
    def talk(self):
        print("Hello")


# Depending on type of object passed corresponding method will be invoked
def callTalk(obj):
    obj.talk()


d = Duck()
callTalk(d)

h = Human()
callTalk(h)
