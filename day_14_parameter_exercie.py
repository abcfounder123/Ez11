
"""

1. simple data နှစ်ခု လက်ခံချင်တဲ့အခါ
2. complex data 4ခု လက်ခံချင်တဲ့အခါ
3. ကြုံသလိုထည့်မယ့် data နှစ်ခုနဲ့ complex data 2ခု လက်ခံချင်တဲ့အခါ
4. simple data 3ခုနဲ့ complex data 2ခု လက်ခံချင်တဲ့အခါ
5. simple data 3ခု ၊ complex data 2ခုနဲ့ ကြုံသလိုထည့်တာ 2ခု လက်ခံချင်တဲ့အခါ
6. simple data 3ခု ၊ complex data 3ခုနဲ့ 
country တန်ဖိုးမထည့်ခဲ့ရင် Myanmar ဖြစ်စေချင်သောအခါ
7. simple data တွေကို အကန့်အသတ်မရှိ လက်ခံချင်သောအခါ
8. complex data တွေကို အကန့်အသတ်မရှိ လက်ခံချင်သောအခါ
9. simple data 3 ခုနဲ့ complex data တွေကို အကန့်အသတ်မရှိ လက်ခံချင်သောအခါ
10. complex data 2 ခုနဲ့ simple data တွေကို အကန့်အသတ်မရှိ လက်ခံချင်သောအခါ
11. unlimited simple data, minium = 3
12. unlimited complex data, minium = 2
13. 11 + 12
14. အကန့်အသတ်မရှိတဲ့ function, ဘာစည်းမျဉ်းမှ လိုက်နာစရာမလိုတဲ့ function ဖန်တီးချင်သောအခါ
15. print function ၏ စည်းမျဉ်းများ
16. input function ၏ စည်းမျဉ်းများ

##########################################

Combination of Parameters (16)

1. Simple is better than complex. (N0.3)

simple data နှစ်ခု လက်ခံချင်တဲ့အခါ



def add(n1, n2, /):
    print(n1 + n2)


add(1, 2)

##########################################

2. Complex is better than complicated. (No.4)

complex data 4ခု လက်ခံချင်တဲ့အခါ


def info(*, name, age, grade, roll):
    print(name, age, grade, roll)


info(name="abc", age=10, grade="A", roll=1)


##########################################

3. No.1 + No.4

ကြုံသလိုထည့်မယ့် data နှစ်ခုနဲ့ complex data 2ခု လက်ခံချင်တဲ့အခါ

x, y         --->   F1, F2, F3
name, age    --->   F2


def f(x, y, *, name, age):
    print(x, y, name, age)


f(1, 2, name="Mg Mg", age=10)
f(x=1, y=2, name="Mg Mg", age=10)
f(1, y=2, name="Mg Mg", age=10)

##########################################

4. N0.3 + No.4

simple data 3ခုနဲ့ complex data 2ခု လက်ခံချင်တဲ့အခါ


a, b, c     --->   F1

name, age   --->   F2


def f(a, b, c, /, *, name, age):
    print(a, b, c, name, age)
    
    
f(1, 2, 3, name="Mg Mg", age=10)

##########################################

5. N0.3 + N0.1 + No.4

simple data 3ခု ၊ complex data 2ခုနဲ့ ကြုံသလိုထည့်တာ 2ခု လက်ခံချင်တဲ့အခါ

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

simple data 3ခု ၊ complex data 3ခုနဲ့ 
country တန်ဖိုးမထည့်ခဲ့ရင် Myanmar ဖြစ်စေချင်သောအခါ


a, b, c     --->   F1                    No.3
name, age   --->   F2                    No.4
country     --->   F2 ("Myanmar")        No.4 + No.2


def f(a, b, c, /, *, name, age, country="Myanmar"):
    print(a, b, c, name, age, country)


f(1, 2, 3, name="Mg Mg", age=10)
f(1, 2, 3, name="Mg Mg", age=10, country="England")

##########################################

7. No.5

simple data တွေကို အကန့်အသတ်မရှိ လက်ခံချင်သောအခါ
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

complex data တွေကို အကန့်အသတ်မရှိ လက်ခံချင်သောအခါ
variable length + complex data


def info(**x):
    print(x)


info()
info(name="abc", age=10, weight=20)

##########################################

9. No.3 + No.6

simple data 3 ခုနဲ့
complex data တွေကို အကန့်အသတ်မရှိ လက်ခံချင်သောအခါ

3 simple data              No.3
unlimited complex data     No.6


def f(a, b, c, /, **x):
    print(a, b, c, x)


f(1, 2, 3)
f(1, 2, 3, name="Mg Mg", age=10)

##########################################

10. No.4 + No.5   =>   No.5 + No.4

complex data 2 ခုနဲ့
simple data တွေကို အကန့်အသတ်မရှိ လက်ခံချင်သောအခါ

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

အကန့်အသတ်မရှိတဲ့ function, ဘာစည်းမျဉ်းမှ လိုက်နာစရာမလိုတဲ့ function ဖန်တီးချင်သောအခါ  

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

