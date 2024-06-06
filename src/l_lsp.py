'''
LSP: Liskov Substitution Principle (リスコフの置換原則)
'''


class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Bow Wow")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


def make_animal_sound(animal):
    animal.make_sound()


if __name__ == '__main__':
    dog = Dog()
    make_animal_sound(dog)  

    cat = Cat()
    make_animal_sound(cat)  