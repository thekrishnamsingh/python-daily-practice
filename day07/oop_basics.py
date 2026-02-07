class Developer:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        return f"My name is {self.name} and I am a {self.role}"


dev1 = Developer("Krishnam Singh", "Python Developer")
print(dev1.introduce())
