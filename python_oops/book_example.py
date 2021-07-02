class Book:
    name = "Default"

    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    def increase_copies(self, how_much):
        self.copies += how_much

    def decrease_copies(self, how_much):
        self.copies -= how_much

    def __repr__(self):
        return repr((self.name, self.copies))


book1 = Book('Mastering Spring 5.0', 200)
book1.increase_copies(10)
book2 = Book('Mastering Python', 15)
book2.decrease_copies(1)
print(book1)
print(book2)
