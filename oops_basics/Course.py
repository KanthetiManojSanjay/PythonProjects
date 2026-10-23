class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def average(self):
        number_of_ratings = len(self.ratings)
        average_rating = sum(self.ratings) / number_of_ratings
        print("Average rating for ", self.name, " is: ", average_rating)


c1 = Course("Java Course", [1, 2, 3, 4])
print(c1.name)
print(c1.ratings)
c1.average()