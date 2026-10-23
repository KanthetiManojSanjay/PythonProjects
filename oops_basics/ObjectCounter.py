class ObjectCounter:
    numberOfObjects = 0

    def __init__(self):
        ObjectCounter.numberOfObjects += 1

    @staticmethod
    def displayCount(): #self is not needed for static method
        print(ObjectCounter.numberOfObjects)

o1 = ObjectCounter()
ObjectCounter.displayCount()