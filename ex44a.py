class Parent(object):

    def implict(self):
        print("PARENT implict()")


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implict()
son.implict()
