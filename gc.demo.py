#! /usr/bin/python3

# garbage collector in python. studio
# https://rico-schmidt.name/pymotw-3/gc/index.html

import gc
import pprint



class Nodo:

    def __init__(self, inf):
        self.info = inf
        self.next = None

    def set_next(self, next):
        if not isinstance(next, Nodo):
            raise TypeError
        print('linking {} -> {}'.format(self, next))
        self.next = next

    def get_next(self):
        return self.next


    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__, self.info)

    def print(self):
        print(f"[{self.info}]", end="")

    def printNext(self):
        if self.next:
            self.next.print()

    def printDeep(self):
        self.print()
        if self.get_next():
            self.get_next().printDeep()

# Construct a Nodo chain/cycle
n1 = Nodo('1')
n2 = Nodo('2')
n3 = Nodo('3')

# chain
# n1.set_next("patata")
n1.set_next(n2)     # n1->n2
n2.set_next(n3)     # n1->n2->n3

print()

n1.print()                 # [1]
print()

n1.printNext()             # [2]
print()

n1.get_next().printNext()  # [3]?
print()

n1.printDeep()

# cycle
n3.set_next(n1)  # n1->n2->n3-> ... ->n1 !!!

n1.printDeep()
exit() # -------------------------------------------------------


# print('three refers to:')
# for r in gc.get_referents(three):
#     pprint.pprint(r)
