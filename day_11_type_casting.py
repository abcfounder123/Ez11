
"""

Type casting (21) (14 + c o 2 8 16 r e)

1. str()

2. int()
3. float()
4. complex()

5. list()
6. tuple()
7. set()
8. frozenst()
9. bytearray()
10. bytes()
11. range()
12. dict()

13. bool()

14. memoryview()

15. chr -> str   eg. chr(65)    =>   'A'
16. ord -> int   eg. ord('A')   =>    65
17. bin -> str  "0b0011"
18. oct -> str  "0o75"
19. hex -> str  "0xa"
20. repr -> str
21. eval -> program output(15 +)

################################################

c o 2 8 16 r e

c    chracter               chr
o    ordinal number         ord

2    binary                 bin
8    octal                  oct
16   hexadecimal            hex

r    representation string  repr
e    evaluation             eval

################################################

ordinal number ( first, second )

chr    ordinal number, Unicode
A  =>  65
B  =>  66
a  =>  97
b  =>  98
က =>  4096
ခ  =>  4097

################################################

Numbering system

decimal  bin     oct

0         0       0
1         1       1
2        10       2   
3        11       3    
4       100       4      
5       101       5          
6       110       6
7       111       7                        
8                10
9
  
                 100   (64)

10                   
11
12
13
14
15
16
17
18
19

20


hex     dec
0       0
1       1
2       2
3       3
4       4
5       5
6       6
7       7
8       8
9       9
a      10
b      11
c      12
d      13
e      14
f      15

100    256


100    bin   =>  2 * 2 = 4
100    oct   =>  8 ** 2 = 64
100    dec   =>  10 ** 2 = 100
100    hex   =>  16 ** 2 = 256

################################################################################################

1. Explicit / direct type casting (list to set)

x = ["apple", "orange", "apple", "banana", "orange", "apple"]
ans = set(x)
print(ans)

################################################

2. Explicit type casting (range to list)

x = range(1000)
ans = list(x)
print(ans)

ans = list(range(1, 1001))
print(ans)

################################################

3. Explicit type casting (dict to list)

x = {"name": "Mg Mg",
     "age": 20,
     "grade": "A",
     "pn No": "09123456"
     }

k = list(x.keys()) # ['name', 'age', 'grade', 'pn No']
print(k)

kk = list(x) # list(x.keys())
print(kk)

v = list(x.values()) # ['Mg Mg', 20, 'A', '09123456']
print(v)

i = list(x.items()) # [('name', 'Mg Mg'), ('age', 20), ('grade', 'A'), ('pn No', '09123456')]
print(i)

################################################

4. Explicit type casting (list to dict)

i = [('name', 'Mg Mg'), ['age', 20], ('grade', 'A'), ('pn No', '09123456')]

d = dict(i)

print(d)

################################################################################################

ordinal number, unicode number, character

65.   A
66.   B
4096. က

################################################

ord & chr

chr(65)  --> A     <- str
ord("A") --> 65    <- int

################################################

5. Explicit type casting (chr to ord)

x = "A"
ans = ord(x)
print(ans)

################################################

6. Explicit type casting (ord to chr)

chr(4096) --> က

x = 4096
ans = chr(x)
print(ans)

################################################

7. Explicit type casting (int to str value of binary number)

x = 2
ans = bin(x) # "0b10"
print(ans)

################################################

8. Explicit type casting (int to str value of octal number)

x = 8
ans = oct(x) # "0o10"                  
print(ans)

################################################

9. Explicit type casting (int to str value of hexadecimal number)

x = 16
ans = hex(x) # "0x10"
print(ans)

################################################

10. Explicit type casting (int to repr value)

x = 1 
ans = repr(x) # repr value -> "1"
print(ans)
print(type(ans))

################################################

11. Explicit type casting (str to program value)

x = "1 + 1.5"
ans = eval(x) # float
print(ans)


x = "1 + 1"
ans = eval(x) # int
print(ans)

################################################

12. Explicit type casting (str to program value) (Dynamic formla)

x = 1
y = 2
ans = 2 * x + y
print("ans =", ans)

>> ans = 4


x = 1
y = 2
ans = 2 * x + 2 * y
print("ans =", ans)

>> ans = 6

x = 1
y = 2
f = input("f = ") # "2 * x + y", "2 * x + 2 * y", "x + y"
ans = eval(f)
print("ans =", ans)

################################################################################################

Type casting
- Explicit type casting (direct)   (21)
- Implicit type casting (indirect) (2)(float, bool)

################################################

Explicit type casting

1 + 1.6

int(truncate)
1 + int(1.6)
1 + 1              ->   2 

int(round)
1 + round(1.6) 
1 + 2              ->   3

float
float(1) + 1.6
1.0 + 1.6          ->   2.6

################################################

Implicit(float, bool)

1
float  ->  1.0
bool   ->  True

################################################

print(1 + 1.5)   # float(1) + 1.5 => 1.0 + 1.5 => 2.5

################################################

if 1:   =>  if bool(1):  =>  if True:

if 0:

################################################

bool (empty, any)

Empty    ->   False
0
0.0
0j
""
[]
()
{}
set()

Any      ->   True
1
10
1000000
1.0
0.000001
"apple"
" "
["apple", "banana"]
(1, 2)
{"name": "Mg Mg"}
set(1, 2, 3)     

################################################################################################


"""