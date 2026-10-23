class Programmer:
    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setSalary(self, sal):
        self.salary = sal

    def getSalary(self):
        return self.salary

    def setTechnologies(self, tech):
        self.technologies = tech

    def getTechnology(self):
        return self.technologies


p1 = Programmer()
p1.setName("John")
p1.setSalary(500)
p1.setTechnologies(["Python", "Ruby"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnology())
