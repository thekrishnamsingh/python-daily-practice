class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


class Developer(Employee):
    def __init__(self, name, salary, tech):
        super().__init__(name, salary)
        self.tech = tech

    def get_details(self):
        return f"Developer: {self.name}, Tech: {self.tech}, Salary: {self.salary}"


dev = Developer("Krishnam", 80000, "Python")
print(dev.get_details())
