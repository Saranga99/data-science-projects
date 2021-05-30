# encapsulation - hiding implementations
# with decoraters
class SoftwareEngineer:
    def __init__(self, name, age):
        # public
        self.name = name
        self.age = age
        # private
        self._salary = None
        self._bugs_sloved = 0

    def code(self):
        self._bugs_sloved += 1

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._bugs_sloved < 10:
            return base_value
        elif 10 < self._bugs_sloved < 100:
            return base_value*2
        else:
            return base_value*3


se = SoftwareEngineer("adooo", 23)
print(se.salary)
se.salary = 5000
print("bugs < 10       ", se.salary)


# 1st
for i in range(70):
    se.code()
se.salary = 5000
print("10 < bugs < 100 ", se.salary)


# 2st
for i in range(70):
    se.code()
se.salary = 5000
print("bugs > 100      ", se.salary)
