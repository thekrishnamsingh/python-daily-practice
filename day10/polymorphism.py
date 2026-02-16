

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog says Woof!")


class Cat(Animal):
    def speak(self):
        print("Cat says Meow!")



animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()
