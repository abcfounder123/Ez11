
"""

1. Sequence 

2. Selection 

3. Loop

4. Function
   - code reuse
   - call, invoke   => ( )

##########################################

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")
print('-' * 42)

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")
print('-' * 42)

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")
print('-' * 42)

##########################################

Step.1


def m2():
    for r in range(1, 13, 1):
        print(f"2 x {r} = {2 * r}")
    print('-' * 42)


def m3():
    for r in range(1, 13, 1):
        print(f"3 x {r} = {3 * r}")
    print('-' * 42)


def m4():
    for r in range(1, 13, 1):
        print(f"4 x {r} = {4 * r}")
    print('-' * 42)


m2()
m2()
m2()
m3()
m4()

##########################################

Step.2


def m(l):
    for r in range(1, 13, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)


m(l=2)
m(l=3)
m(l=4)

##########################################

Step.3

def m12(l):
    for r in range(1, 13, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)


def m10(l):
    for r in range(1, 11, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)


m12(2)
m10(2)

##########################################

Step.4


def m(l, n):
    for r in range(1, n+1, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)


m(l=2, n=10)

####################################################################################

စည်းမျဉ်း 6 မျိုး

1. မဖြစ်မနေ လိုက်နာရမည့် စည်းမျဉ်း။         
2. ပျက်ကွက်၍ရသော စည်းမျဉ်း။
3. နေရာနဲ့သာ တန်ဖိုးထည့်ရမည့် စည်းမျဉ်း။    
4. အမည်နဲ့သာ တန်ဖိုးထည့်ရမည့် စည်းမျဉ်း။     
5. အရေအတွက် မကန့်သတ်ထားသော 3
6. အရေအတွက် မကန့်သတ်ထားသော 4


Parameters(6)

1. Normal Parameters, Standard Parameters        (x, y)
2. Default Parameters                            country="Myanmar"
3. Positional only Parameters                    /
4. Keyword only Parameters                       *
5. Variable length positional only Parameters    *args
6. Variable length keyword only Parameters       **kw, **kwargs

*   <---  all values
**  <---  all items

Standard Form(3)
1. Position                f(1, 2)
2. Keyword name            f(x=1, y=2)
3. 1 + 2                   f(1, y=2)

##########################################

1. Normal Parameters

def add(x, y):
    print(x + y)


add(1, 2)

##########################################

2. Default Parameters


def info(name, password, country="Myanmar"):
    print(name, password, country)


info("abc", "12345")

##########################################

3. Positional only Parameters

Simple is better than complex.

##########################################


def add(x, y, /):
    print(x + y)


add(1, 2)
add(2, 1)

##########################################

4. Keyword only Parameters

Complex is better than complicated.

##########################################


def info(*, name, age, ph_no, blood, height, weight, country):
    print(f"Name = {name}")
    print(f"age = {age}")
    print(f"ph_no = {ph_no}")
    print(f"blood = {blood}")
    print(f"height = {height}")
    print(f"weight = {weight}")
    print(f"country = {country}")


info(name="Mg Mg", age=10, weight=20, ph_no="09123456", height='''4' 2"''', country="Myanmar", blood="O")

##########################################

(x, y)
x <-- first parameter  (No.1)
y <-- second parameter (No.1)

(x, y, /)
x <-- first parameter  (No.3)
y <-- second parameter (No.3)

(*, x, y)
x <-- first parameter  (No.4)
y <-- second parameter (No.4)

####################################################################################

5. Variable length positional only Parameters

Fixed length = 2


def add(x, y):
    ans = x + y
    print(ans)


add(1, 2)

##########################################

variable length  (0, 1, 2, .. ) 

add()
add(1)
add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4)

##########################################


def add(*numbers):
    ans = 0
    for number in numbers:
        ans += number
    print(ans)


add()
add(1)
add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4)

##########################################

6. Variable length keyword only Parameters


Fixed length = 7


def info(*, name, age, ph_no, blood, height, weight, country):
    print(f"Name = {name}")
    print(f"age = {age}")
    print(f"ph_no = {ph_no}")
    print(f"blood = {blood}")
    print(f"height = {height}")
    print(f"weight = {weight}")
    print(f"country = {country}")


info(name="Mg Mg", age=10, weight=20, ph_no="09123456", height='''4' 2"''', country="Myanmar", blood="O")

##########################################

Variable length


def info(**x):
    print(x)


info()
info(name="Mg Mg")
info(name="Mg Mg", age=10)
info(name="Mg Mg", age=10, ph_no="09123456")

####################################################################################

"""
