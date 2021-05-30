# polymorphysm


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


print("\n#polymorphysm\n")
employees = [SoftwareEngineer("sara", 22, "jonior", 7000), Designer(
    "max", 23), SoftwareEngineer("philllip", 23, "senior", 23222)]


def motivate(employee):
    for e in employee:
        e.work()


motivate(employees)
