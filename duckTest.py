# mmm Ducks...
# THIS IS A DUCK SIMULATOR USING THE STRATEGY DESIGN

# FLYING
class FlyBehavior:
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I cannot fly.")


# QUACK
class QuackBehavior:
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack.\n")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak.\n")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("....\n")


# DUCK
class Duck:
    # all functions that ducks have
    # variables / attributes
    flyBehavior = FlyBehavior()
    quackBehavior = QuackBehavior()

    def __int__(self):
        self.duckType = ''

    # operations / functions
    def display(self):
        print(f"I'm a {self.duckType} Duck.")

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")


# MALLARD DUCK
class MallardDuck(Duck):
    flyBehavior = FlyWithWings()
    quackBehavior = Quack()
    duckType = "Mallard"


class RedDuck(Duck):
    flyBehavior = FlyWithWings()
    quackBehavior = Quack()
    duckType = "Red"


class RubberDuck(Duck):
    flyBehavior = FlyNoWay()
    quackBehavior = Squeak()
    duckType = "Rubber"


class DecoyDuck(Duck):
    flyBehavior = FlyNoWay()
    quackBehavior = MuteQuack()
    duckType = "Decoy"


def main():
    print("Testing the Duck Simulator.\n")
    # object
    # MALLARD
    mallard = MallardDuck()
    mallard.display()
    mallard.swim()
    mallard.performFly()
    mallard.performQuack()
    # RED
    red = RedDuck()
    red.display()
    red.swim()
    red.performFly()
    red.performQuack()
    # RUBBER
    rubber = RubberDuck()
    rubber.display()
    rubber.swim()
    rubber.performFly()
    rubber.performQuack()
    # DECOY
    decoy = DecoyDuck()
    decoy.display()
    decoy.swim()
    decoy.performFly()
    decoy.performQuack()


if __name__ == '__main__':
    main()

