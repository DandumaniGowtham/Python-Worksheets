class Animal:
    def sound(self):
        print("Animals makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")


class Cat(Animal):
    def sound(self):
        print("Cat says Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()