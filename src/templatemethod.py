"""
# Template Method Pattern

The Template Method Pattern defines the skeleton of an
algorithm in a method, deferring some steps to subclasses.
Template Method lets subclasses redefine certain steps of
an algorithm without changing the algorithm's structure.

"""

from __future__ import print_function
from abc import ABCMeta, abstractmethod

class CaffeineBeverageWithHook(object):
    """
    CaffeineBeverageWithHook is abstract just like in
    the class design.
    """
    __metaclass__ = ABCMeta

    def prepare_recipe(self):
        """
        Now, the same prepare_recipe() method will be used 
        to make both Tea and Coffee. We don't want our subclasses
        to be able to override this method and change the recipe.
        """
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()
        
    @abstractmethod
    def brew(self):
        """
        Because Coffee and Tea handle these methos in different ways,
        they're going to have to be declared as abstract. Let the 
        subclasses worry about that stuff!
        """
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    def customer_wants_condiments(self):
        """
        Here we've defined a method with a empty default implementation.
        This method just returns true and does nothing else.
        This is a hook because the subclass can override this method, but
        doesn't have to.
        """
        return True

class CoffeeWithHook(CaffeineBeverageWithHook):
    def __init__(self):
        pass

    def add_condiments(self):
        """
        Same for coffee, except CoffeeWithHook deals TeaWithHook
        coffee, and sugar and milk instead of tea bags and lemon.      
        """
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
        """
        TeaWithHook needs to define brew() and add_condiments()
        the two abstract methods from CaffeineBeverageWithHook
        """
        print("Adding Lemon")

    def brew(self):
        print("Steeping the tea")

    def customer_wants_condiments(self):
        """
        Here's where we override the hook and provide our own functionality.
        Get the user's input on the condiment decision and return true or
        false, depending on the input.
        """
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