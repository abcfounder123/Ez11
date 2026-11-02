
"""

Polymorphism
- Joker

-------------------------------------------------

Joker => +

1 .dollar + 10000 .kyat       =>  3 dollar
5000 .kyat + 2 .dollar        =>  15000 kyat
1 + 2                         =>  3
"1" + "2"                     =>  12

-------------------------------------------------


class DieselEngine:
   def on():
       pass
       
       
class PetrolEngine:
   def on():
       pass


class Fan:
    def on():
       pass


class Bulb:
    def on():
       pass

-------------------------------------------------

Joker => on()

e1.on()
e2.on()
e3.on()
p1.on()

-------------------------------------------------

Polymorphism (interface) (abstraction)

1 2 3
Y G R       R
G R Y       T
R Y G       E

1 2 3
Y G R 

-------------------------------------------------

>> Creating an interface for all cars by "abstraction" to become Polymorphism


from abc import ABC, abstractmethod


class CarRule(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def brake(self):
        pass
        

#################################################

Summary

OOP concepts
1. Inheritance  (parent and child) (code reuse)
2. Composition  (friends)          (flexiable)
3. Polymorphism (easy user interface)
4. Encapsulation  (seperate)
5. Abstraction    (rules)

Core programming
- Custom Types
- Controlling by magic methods 

#################################################

Design pattern (23)
1. Iterator pattern
2. Singleton pattern
...
...
...


Algorithms (1000, 300, 50)
Searching Algorithms
1. linearsearch   
2. binarysearch
...
...
...

#################################################

Exercises for 4 months

1. Tac Ti Toe                     =>  Procedural programming
2. Attributes 10 + 1              =>  OOP basics
3. Custom data types 11           =>  Core programming
4. Inheritance  20                =>  Large scale project
5. Inheritance and Composition 1  =>  ---

##################################################################################################

"""

