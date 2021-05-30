
class SoftwareEngineer:
    # class variable
    alias = "Code Expert"

    def __init__(self, name, age, level, salary) -> None:
        # instance variables
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    # instance

    def coding(self):
        print(f"{self.name} is writing code....")

    def codeing_language(self, lan):
        print(f"{self.name} is writing code in {lan}")

    # special methodes
    # objact convered to string
    def __str__(self):
        return f"name = {self.name}"

    # object equal
    def __eq__(self, other):
        return self.name == other.name

    # class method
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 8000
        else:
            return 10000


se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
print(se1.name)
se3 = SoftwareEngineer("Saranga", 22, "junior", 80000)


# class attributes can be used in class
print(se1.alias, SoftwareEngineer.alias)
print(se3.name)
se1.coding()
se1.codeing_language("java")
print(se1)
print(se1 == se3)

print(SoftwareEngineer.entry_salary(22))
print(se1.entry_salary(30))
