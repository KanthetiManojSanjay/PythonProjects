class Computer:

    def __init__(self,cpu,ram):
        self.ram=ram
        self.cpu=cpu

    def config(self):
        print("Config is: ",self.cpu,self.ram)

    def compare(self,other):
        if self.ram==other.ram:
            return True
        else:
            return False

com1=Computer('i5',16)
com1.ram=4
com2=Computer('Ryzen 3',8)

if com1.compare(com2):
    print("Both are same")
else:
    print("Both are different")

com1.config()
com2.config()


