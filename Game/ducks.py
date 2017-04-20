class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("weeee I'm flying")
        elif self.ratio == 1:
            print("This is hard but at least I'm in the air")
        else:
            print("I'll just walk")



class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()

class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit cold")

    def quack(self):
        print("I'm a penguin")


# def duck_tester(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # duck_tester(donald)
    #
    # percy = Penguin()
    # duck_tester(percy)