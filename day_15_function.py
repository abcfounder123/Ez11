
"""

Function 

1. Introduction
   - print(), input(), len(), int(input())
   - Function call =>  print, print()
   - Why?
     - Readability, reuse
     - Decomposition
   - Where?
     1. built-in module
     2. preinstalled module  tkinter.py, math.py, .....
     3. external module      PyQt5, numpy
     4. custom function

2. module, package, framwork
   - function (collection of program)         (one purpose - add(), sqrt() )
   - module   (file)   (collection of fun)    (one work - math.py, login.py)
   - package  (folder) (collection of module) (one group - frontend folder)
   - framework(folder) (collection of package)(one project - Django)

3. Function name
   - naming rules
   - same name (last one)
   - should not give the same name

4. Parameterized function
   - parameterized function   => def add(x, y):
   - parameter list           => (x, y), tuple
   - first parameter          => x

5. Arguments(7)
   - value passed by function
   - positional argument  =>  add(1, 2)
   - keyword argument     =>  add(x=1, y=2)
   - ...

6. Local, Global, Built-in
   Local          => local
   Global         => all (local file)
   Built-in       => all file

7. Standrd form(3)

8. Types of parameters(6)

9. Passing correct values to function

10. Checking Parameters

11. Components of function (8)

12. help(), doc

13. Types of function

14. Pure function

15. Exercises(27)

##########################################

Decomposition

     .    .
   X .    .  O
 ----------------
     . X  .  O
 ----------------
     .    .  X
     .    .


Board
draw X
draw O
check win
check tie
marks

##########################################

9. Passing correct values to function

a = 20
b = 10
c = 30
args = (1000, 700, 1100)
user_name = "Mg Mg"
password  = "12345"
kw        = {country: "Myanmar", "age": 10}


a, b, c,                pos
*args                   all pos
user_name, password     keyword
**kw                    all items


def f(a, b, c, /, *args, user_name, password, **kw):
    print(a, b, c)
    print(args)
    print(user_name, password)
    print(kw)


f(20, 10, 30, 1000, 700, 1100, user_name="Mg Mg", password="12345", country="Myanmar", age=10)

##########################################

10. Checking Parameters

No.5 + (No.2 + 4)
help(print)   =>   def print(*args, sep=' ', end='\n', file=None, flush=False):

No.2 + No.3
help(input)   =>   def input(prompt='', /):

No.3
help(len)     =>   def len(obj, /):

##########################################

11. Components of function (8)

1. Function define      =>   def
2. Function name        =>   dollar_kayat
3. Parameter list       =>   (dollar)            
4. Parameters           =>   dollar
5. Code block           =>   :
6. Documentation string =>   triple quotes
7. Function body        =>   programs 
8. return statement     =>   stop, return value


def dollar_kayat(dollar):
    '''This is dollar kayat function.
    eg.
    >> dollar_kayat(1)
    >> 5000

    '''
    kyat = dollar * 5000
    return kyat


##########################################

12. help(), doc

help()
1. function name
2. parameter list
3. documentation string

doc 
1. documentation string

################################################

13. Types of function
1. effect only function    =>  add_one()
2. result only function    =>  add()
3. effect and result       =>  pop()

################################################


def add(x, y):
    return x + y


def add_one(l):
    l.append("apple")


a = ["banana", "orange"]
print(add(1, 2))
print(add_one(a))

################################################

difference_update
effect = Remove all elements of another set from this set.
result = None

difference
effect = -
result = Return the difference of two or more sets as a new set.

pop
effect = Remove an arbitrary set element
result = return an arbitrary set element

len 
effect =  -
result = the number of items in a container   

################################################ 

14. Pure function (no side-effect) (result only function) 

################################################ 

Three steps of function


def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(fahrenheit)


def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32        
    return fahrenheit


def celsius_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32        


################################################

"""
