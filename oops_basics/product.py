class Product:
    def __init__(self):
        self.name = "Iphone"
        self.description = "Awesome mobile"
        self.price = 700

    # Destructor - This method will be invoked by GC before clearing up memory allocated to objects
    def __del__(self):
        print("Inside the destructor")

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)


p1 = Product()
p1.display()
p1 = None  # This will indicate GC that no longer required and will be immediately consider for GC
