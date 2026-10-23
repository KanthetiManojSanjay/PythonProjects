class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")


# Parent class method is extended using (BMW)
class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        # super().__init__(make, model, year) # Using super we can avoid passing self
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    # overriden parent class start method
    def start(self):
        super().start()  # Parent class method will be called using this
        print("Button start")


class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        # super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    # overriden parent class start method
    def start(self):
        super().start()
        print("Remote start")

    def display(self):
        print(self.parkingAssistEnabled)


threeSeries = ThreeSeries(True, "BMW", "328i", 2018)
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()

fiveSeries = FiveSeries(True, "Innova", "1i", 2022)
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.start()
fiveSeries.stop()
fiveSeries.display()
