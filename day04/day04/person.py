class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old and I work as a {self.profession}."
