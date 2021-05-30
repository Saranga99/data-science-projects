# inheritance

# parent class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f"{self.name} is working")


# child classes
class SoftwareEngineer(Employee):

    def __init__(self, name, age, level, salary):
        super().__init__(name, age)
        # extend functionality
        self.level = level
        self.salary = salary

    # overriden
    def work(self):
        print(f"{self.name} is codeing")

    def debugging(self):
        print(f"{self.name} is debugging")


class Designer(Employee):

    def designing(self):
        print(f"{self.name} is designing")


se = SoftwareEngineer("Sara", 22, "Junior", 8000)
se.work()
se.debugging()

de = Designer("Thathsara", 23)
de.work()
de.designing()
