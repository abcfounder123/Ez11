
"""

Combination of Parameters (16)

1. Simple is better than complex. (N0.3)


def add(n1, n2, /):
    print(n1 + n2)


add(1, 2)

##########################################

2. Complex is better than complicated. (No.4)


def info(*, name, age, grade, roll):
    print(name, age, grade, roll)


info(name="abc", age=10, grade="A", roll=1)


##########################################

3. No.1 + No.4

x, y       --->   F1, F2, F3
name, age    --->   F2


def f(x, y, *, name, age):
    print(x, y, name, age)


f(1, 2, name="Mg Mg", age=10)
f(x=1, y=2, name="Mg Mg", age=10)
f(1, y=2, name="Mg Mg", age=10)

##########################################

4. N0.3 + No.4

a, b, c     --->   F1

name, age   --->   F2


def f(a, b, c, /, *, name, age):
    print(a, b, c, name, age)
    
    
f(1, 2, 3, name="Mg Mg", age=10)

##########################################

5. N0.3 + N0.1 + No.4

a, b, c     --->   F1
x, y        --->   F1, F2, F3
name, age   --->   F2


def f(a, b, c, /, x, y, *, name, age):
    print(a, b, c, x, y, name, age)


f(1, 2, 3, 4, 5, name="Mg Mg", age=10)
f(1, 2, 3, x=4, y=5, name="Mg Mg", age=10)
f(1, 2, 3, 4, y=5, name="Mg Mg", age=10)

##########################################

Understanding other functions

(a, b, c, /, x, y, *, name, age)

Step.1   ->  check parameter list (/, *)
Step.2   ->  divide

a, b, c      ->   F1
x, y         ->   F1, F2, F3
name, age    ->   F2

##########################################

6. No.3 + No.4 + No.2

a, b, c     --->   F1                    No.3
name, age   --->   F2                    No.4
country     --->   F2 ("Myanmar")        No.4 + No.2


def f(a, b, c, /, *, name, age, country="Myanmar"):
    print(a, b, c, name, age, country)


f(1, 2, 3, name="Mg Mg", age=10)
f(1, 2, 3, name="Mg Mg", age=10, country="England")

##########################################

7. No.5

variable length + simple data


def add(*x):
    ans = 0
    for number in x:
        ans += number
    print(ans)


add(60, 70, 65)
add(60, 70, 65, 70, 68)
add()

##########################################

8. No.6

variable length + complex data


def info(**x):
    print(x)


info()
info(name="abc", age=10, weight=20)

##########################################

9. No.3 + No.6

3 simple data              No.3
unlimited complex data     No.6


def f(a, b, c, /, **x):
    print(a, b, c, x)


f(1, 2, 3)
f(1, 2, 3, name="Mg Mg", age=10)

##########################################

10. No.4 + No.5   =>   No.5 + No.4

2 complex data             No.4
unlimited simple data      No.5


def f(*x, name, password):
    print(x)
    print(name, password)


f(1, 2, 3, 4, "Mg Mg", 12345, name="abc", password=1234)

##########################################

11. No.3 + No.5

unlimited simple data, minium = 3

unlimited simple data               No.5
at least 3 simple data              No.3


def f(a, b, c, /, *x):
    print(a, b, c)
    print(x)


f(1, 2, 3)
f(1, 2, 3, 4, 5, 6)

##########################################

12. No.4 + No.6

unlimited complex data, minium = 2

unlimited complex data              No.6
at least 2 complex data             No.4


def f(*, user_name, password, **x):
    print(user_name, password)
    print(x)


f(user_name="Mg Mg", password="12345")
f(user_name="Mg Mg", password="12345", gender="Male")

##########################################

13. 11 + 12

unlimited simple data, minium = 3
unlimited complex data, minium = 2

(a, b, c, /, *x)
(*, user_name, password, **x)
(a, b, c, /, *t, user_name, password, **d)


def f(a, b, c, /, *t, user_name, password, **d):
    print(a, b, c)
    print(t)
    print(user_name, password)
    print(d)


f(1, 2, 3, 4, 5, 6, user_name="Mg Mg", password="12345", gender="Male", age=10)

##########################################

14. Unlimited function (No.5 + No.6)    

unlimited simple data
unlimited complex data


def f(*args, **kw):
    print(args)
    print(kw)
    print("-"* 42)


f()

f(1)
f(1, 2, 3)

f(age=10)
f(age=10, weight=20, name="Mg Mg")

f(1, 2, 3, age=10, weight=20, name="Mg Mg")

##########################################

15. No.5 + (No.4 + No.2)

def print(*x, sep=' ', end='\n', file=None, flush=False)

##########################################

16. No.2 + No.3

(prompt='', /)

##########################################

*x   all positional arguments    (args)
**y  all keyword arguments       (kw, kwargs)

####################################################################################

"""

