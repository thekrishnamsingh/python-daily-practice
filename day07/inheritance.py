class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        return "Employee is working"


class PythonDeveloper(Employee):
    def work(self):
        return f"{self.name} is writing Python code"


dev = PythonDeveloper("Krishnam")
print(dev.work())
