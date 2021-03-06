

# Animal is-a object
class Animal(object):
    pass


# Dog is-a Animal
# Dog has-a name
class Dog(Animal):

    def __init__(self, name):

        self.name = name


# Cat is-a Animal
# Cat has-a name, which it ignores
class Cat(Animal):

    def __init__(self, name):

        self.name = name


# Person is-a object
# Person has-a name
# Person may-have-a Pet
class Person(object):

    def __init__(self, name):

        self.name = name
        self.pet = None


# Employee is-a Person
# Employee has-a name and salary
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)

        self.salary = salary


# Fish is a object
class Fish(object):
    pass


# Salmon is-a Fish
class Salmon(Fish):
    pass


# Halibut is-a Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# Satan is-a Cat
satan = Cat("Satan")

# Mary is a Person
mary = Person("Mary")

# Mary has-a pet
mary.pet = satan

# Frank is-a Employee
frank = Employee("Frank", 120000)

# Frank has_a pet
frank.pet = rover

# Flipper is a Fish
flipper = Fish()

# Crouse is-a Salmon
crouse = Salmon()

# Harry is-a Halibut()
harry = Halibut()
