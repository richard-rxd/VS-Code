"""class Animal:
    def habitat(self):
        print("the Streets")

class Dog(Animal):
    def __init__(self):
        print("I got that DAWG in me")
        print("Hustling in ")
        self.habitat()

nasus = Dog()"""

class Animal:
    def __init__(self, habitat):
        self.habitat = "habitat"

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound")


class Dog(Animal):
    def __init__(self):
        super().__init__("Nasus")

    def sound(self):
        print("Woof woof!")


x = Dog()
x.print_habitat()
x.sound()
print(x.habitat)
