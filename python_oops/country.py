from operator import attrgetter


class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name, self.population, self.area))  # can return a single value only so enclosed as a Tuple


countries = [
    Country('India', 1200, 100),
    Country('China', 1400, 200),
    Country('USA', 120, 300)
]
print(countries)
print(countries[0])
print(countries[0:2])
countries.append(Country('Russia', 80, 900))
print(countries)

countries.sort(key=attrgetter('population'))
print(countries)

countries.sort(key=attrgetter('population'), reverse=True)
print(countries)

print(max(countries, key=attrgetter('population')))
print(min(countries, key=attrgetter('population')))
print(max(countries, key=attrgetter('area')))
print(min(countries, key=attrgetter('area')))


