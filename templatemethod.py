from __future__ import print_function
from abc import ABCMeta, abstractmethod

class CaffeineBeverageWithHook(object):
    __metaclass__ = ABCMeta

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()
        
    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    def customer_wants_condiments(self):
        return True

class CoffeeWithHook(CaffeineBeverageWithHook):
    def __init__(self):
        pass

    def add_condiments(self):
        print("Adding Sugar and Milk")

    def brew(self):
        print("Dripping Coffee through filter")

    def customer_wants_condiments(self):
        answer = raw_input("Would you like Milk or Sugar? (y/n)")
        if answer.lower().startswith('y'):
            return True
        else:
            return False

class TeaWithHook(CaffeineBeverageWithHook):
    def __init__(self):
        pass

    def add_condiments(self):
        print("Adding Lemon")

    def brew(self):
        print("Steeping the tea")

    def customer_wants_condiments(self):
        answer = raw_input("Would you like Lemon? (y/n)").lower()
        if answer.startswith('y'):
            return True
        else:
            return False

def demo():
    tea_hook = TeaWithHook()
    cofee_hook = CoffeeWithHook()
    print("Making tea...")
    tea_hook.prepare_recipe()
    print("Making coffee...")
    cofee_hook.prepare_recipe()

if __name__ == '__main__':
    demo() 