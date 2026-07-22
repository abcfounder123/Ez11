
"""
Programming
1. Imperative paradigm
2. Declarative paradigm

#################################################

Python Programming
1. Procedural programming
2. Object-oriented programming
3. Functional programming

#################################################

Procedural programming
1. Sequence
2. Selection
3. Loop
4. Function

#################################################

1. Sequence
   - top
   - left
   - ()

Sequence သုံးမျိုး
1. အပေါ်အောက်
2. ဘယ်ညာ
3. ဝိုက်ကွင်း

#################################################

Exercises

p2(p1) p3       <---  Exercise.1
p4 p6(p5)
p7 p8 p9
p10

123 456 789 10


213 465 10 978  <---  Exercise.2

p1(p2) p3
p4 p5(p6)
p10
p9 p7 p8


p2(p1) p3(p11(p12))   <---  Exercise.3
p4 p6(p5) p1(p2(p3))
p7(p13) p8(p14) p9
p10

1 2 12 11 3
4 5 6 3 2 1
13 7 14 8 9
10

#################################################

Data Types (15)

စာ သုံးခု
1. Character              --->  chr()
2. Character String       --->  str()
3. Documentation String   --->  doc

နံပါတ် သုံးခု
1. Integer                --->  int()
2. Floating-point number  --->  float()
3. Complex number         --->  complex()

စာရင်း ရှစ်ခု
1. Normal list            --->  list(), tuple()
2. Unique list            --->  set(), frozenset()
3. Binary list            --->  bytearray(), bytes()
4. Number                 --->  range()
5. Item list              --->  dict()

အခြေအနေ တစ်ခု
1. boolean data type      --->  bool()

Data types 15 မျိုး
စာ သုံးခု
နံပါတ် သုံးခု
စာရင်း ရှစ်ခု
အခြေအနေ တစ်ခု

#################################################

Exercises

1 to 99    =>  range(1, 100, 1)
start = 1
stop = 100
step = 1

1 to 100    =>  range(1, 101, 1)
start = 1
stop = 101
step = 1

2, 4, 6, ... to 100    =>  range(2, 101, 2)
start = 2
stop = 101
step = 2

1, 3, 5, ... to 99    =>  range(1, 100, 2)
start = 1
stop = 100
step = 2

100, 98, 96, ... to 2    =>  range(100, 1, -2)
start = 100
stop = 1
step = -2

99, 97, 95, ... to 1    =>  range(99, 0, -2)
start = 99
stop = 0
step = -2

-100, -98, -96, ... to  -2    =>  range(-100, -1, 2)
start = -100
stop = -1
step = 2

-2, -4, -6, ... to  -100    =>  range(-2, -101, -2)
start = -2
stop = -101
step = -2


255, 260, ..., 500
range(255, 501, 5)

500, 495, ..., 255
range(500, 254, -5)

0 to 10    =>  range(0, 11, 1)
start = 0
stop = 11
step = 1

range(0, 11, 1)
range(0, 11)    <--- step = 1
range(11)       <--- start = 0, step = 1

#################################################

"""