# Outer class
class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

        # Inner class
    class Engine:
        def __init__(self, number):
            self.number = number

        def start(self):
            print("Engine started")


c = Car("Ford", "2008")
e = c.Engine(123)  # Using outerclass instance we are calling Inner class
e.start()
