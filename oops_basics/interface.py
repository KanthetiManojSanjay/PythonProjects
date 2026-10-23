from abc import abstractmethod, ABC


# Abstract class can't be instantiated
class BMW(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass


# Parent class method is extended using (BMW)
class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)  # Using super we can avoid passing self
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        print("Button start")

    def stop(self):
        print("Button stop")

    def drive(self):
        print("ThreeSeries is being driven")


class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def start(self):
        print("Remote start")

    def stop(self):
        print("Remote stop")

    def display(self):
        print(self.parkingAssistEnabled)

    def drive(self):
        print("FiveSeries is being driven")


threeSeries = ThreeSeries(True, "BMW", "328i", 2018)
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()
threeSeries.drive()

fiveSeries = FiveSeries(True, "Innova", "1i", 2022)
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.start()
fiveSeries.stop()
fiveSeries.display()
fiveSeries.drive()
