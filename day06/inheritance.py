class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Employee is working")


class BackendDeveloper(Employee):
    def work(self):
        print(f"{self.name} is building backend APIs")


dev = BackendDeveloper("Krishnam")
dev.work()
