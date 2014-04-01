"""
# The State Pattern

The State Pattern allows an object to alter its behaviour
when its internal state changes. The object will appear to
change its class.

"""

from __future__ import print_function
from abc import ABCMeta, abstractmethod

class State(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass

class SoldState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Please wait, we're already giving you a gumball")

    def eject_quarter(self):
        print("Sorry, you already turned the crank")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() > 0:
            self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
        else:
            print("Oops, out of gumballs!")
            gumball_machine.set_state(self.gumball_machine.get_sold_out_state())

class SoldOutState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def eject_quarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def trun_crank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")

class NoQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You inserted a quarter")
        self.gumball_machine.set_state(self.gumball_machine.get_has_quarter_state())

    def eject_quarter(self):
        print("You haven't inserted a quarter")

    def turn_crank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")

class HasQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())

    def turn_crank(self):
        print("You turned...")
        self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())

    def dispense(self):
        print("No gumball dispensed")

class GumballMachine(object):

    def __init__(self, n_gumballs):
        self.sold_out = SoldState(self)
        self.no_quarter = NoQuarterState(self)
        self.has_quarter = HasQuarterState(self)
        self.sold = SoldState(self)
        self.count = n_gumballs
        if self.count > 0:
            self.state = self.no_quarter
        else:
            self.state = self.sold_out

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        print("A gumball comes rolling out the slot...")
        if self.count != 0:
            self.count -= 1

    def get_count(self):
        return self.count

    def get_state(self):
        return self.state

    def get_sold_out_state(self):
        return self.sold_out

    def get_no_quarter_state(self):
        return self.no_quarter

    def get_has_quarter_state(self):
        return self.has_quarter

    def get_sold_state(self):
        return self.sold

    def __repr__(self):
        return "Count: %s State: %s" % (self.count, type(self.state).__name__)

def demo():
    gumball_machine = GumballMachine(5)
    print(gumball_machine)
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    print(gumball_machine)
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    print(gumball_machine)
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    print(gumball_machine)

if __name__ == '__main__':
    demo()
