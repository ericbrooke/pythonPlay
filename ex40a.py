import mystuff


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I am CLASSSY Apple")


mystuff.apple()
print(mystuff.tangerine)

thing = MyStuff()
thing.apple()
print(thing.tangerine)
