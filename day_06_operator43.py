
"""

Operators 43

1. Operation, Operator, Operand


1 + 2     <=   Additional operation
  +       <=   Additional operator
1         <=   Left operand
    2     <=   Right operand

------------------------------------------------------

2. Types of operators (3)
   - unary operator    =>      -2    (Right operand)
   - binary operator   =>   1 + 2    (Left operand, Right operand)
   - ternary operator  =>            (Left operand, Right operand, Middle operand)

------------------------------------------------------

3. Positive, Negative, Addition, Substraction

+1       <=   pos(), unary plus
-1       <=   neg(), unary minus
1 + 2    <=   add(), binary plus
2 - 1    <=   sub(), binary minus

2 + - 1 

------------------------------------------------------

4. Precedence

add
1 + 2 * 3
3 * 3
9

mul
1 + 2 * 3
1 + 6
7

------------------------------------------------------

5. Associativity 
   - left-sided bind  (24)
   - right-sided bind (e u assign)(1 + 4 + 14)(19) 

left-sided bind  
2 ** 2 ** 3
     4 ** 3
         64

right-sided bind
2 ** 2 ** 3
2 ** 8
256

x = y = z = 1

not not True

------------------------------------------------------

Exercises

1 + 2 * 3 // 4 - 5 % 6 + 1 ** 7

1. **
1 + 2 * 3 // 4 - 5 % 6 + 1

2. *
1 + 6 // 4 - 5 % 6 + 1

3. //
1 + 1 - 5 % 6 + 1

4. %
1 + 1 - 5 + 1

5. +
2 - 5 + 1

6. -
-3 + 1

7. +
-2

------------------------------------------------------

Arithmetic operator(9) (e u */ +-)

1. Exponent            **
2. Unary minus         -
3. Unary plus          +
4. Multiplication      *
5. True division       /
6. Floor division      //
7. Modulus             %
8. Addition            +
9. Substraction        -

------------------------------------------------------

Bitwise operators(6)

1. Left shift              <<
2. Right shift             >>
3. Bitwise AND             &
4. Bitwise Exclusive OR    ^
5. Bitwise OR              |
6. Bitwise NOT             ~

------------------------------------------------------

1. Left shift (<<)

4 bits
1111 << 1    --->   1110
1111 << 2    --->   1100

8 bits
1111 << 1    --->   00011110
1111 << 2    --->   00111100

    0000
    1111
   1111
    1110
    
------------------------------------------------------
    
2. Right shift (>>)

4 bits
1111 >> 1    --->   0111
1111 >> 2    --->   0011

    0000
    1111
     1111
    0111
 
------------------------------------------------------

I want apple and banana.
I want apple or banana.
I want apple exclusive or banana.

------------------------------------------------------

3. Bitwise AND (&) (2 wires)

1 -----
         AND   ----  1
1 -----

0 -----
         AND   ----  0
1 -----

1 -----
         AND   ----  0
0 -----

0 -----
         AND   ----  0
0 -----

0101 -----
           AND   ----  0001
0011 -----

0101 & 0011     
=> 0001

------------------------------------------------------

5. Bitwise OR (|) (1 wires)

1 -----
         OR   ----  1
1 -----

0 -----
         OR   ----  1
1 -----

1 -----
         OR   ----  1
0 -----

0 -----
         OR   ----  0
0 -----

0101 -----
            OR   ----  0111
0011 -----

0101 | 0011     
=> 0111

------------------------------------------------------

4. Bitwise XOR (^) (only 1 wires)

1 -----
         XOR   ----  0
1 -----

0 -----
         XOR   ----  1
1 -----

1 -----
         XOR   ----  1
0 -----

0 -----
         XOR   ----  0
0 -----

0101 -----
            XOR   ----  0110
0011 -----

0101 ^ 0011     
=> 0110

------------------------------------------------------

6. Bitwise NOT             ~


1 -----  NOT  ----- 0

0 -----  NOT  ----- 1

0011 -----  NOT  ----- 1100

~ 0011
=> 1100

------------------------------------------------------

Precedence 15
1. e                     
2. u         +, -, ~
3. */                     
4. +-                     

5. shift
6. and       bitwise
7. Xor
8. or        

9. C 
10. not      logical
11. and
12. or

13. t
14. assignment
15. walrus

------------------------------------------------------

Comparison operators (6) (equal, greater) (boolean value)

1. Equal                    == 
2. Not equal                !=
3. Greater than             >
4. Less than                <
5. Greater than or Equal    >=
6. Less than or Equal       <=

------------------------------------------------------

Identity operators (2) (id, same object)

1. is
2. is not

------------------------------------------------------

Membership operators (2)

1. in
2. not in

------------------------------------------------------

Logical operator (3)

1. not 
2. and
3. or

------------------------------------------------------

Bitwise operator Vs logical operator

0011 & 0001    =>   0001
True and True  =>   True

0011 | 0001    =>   0011
True or False  =>   True

~ 01           =>   10
not True       =>   False

------------------------------------------------------

Ternary operator, conditional operator, if-else operator

"pass" if mark >= 40 else "fail"
"fail" if mark < 40 else "pass"

------------------------------------------------------

mark = 80
condition_for_pass = mark >= 40
condition_for_fail = mark < 40

result = "pass" if condition_for_pass else "fail"
result2 = "fail" if condition_for_fail else "pass"

print(result)
print(result2)

------------------------------------------------------

Assignment (13)

1. normal assign                  =

2. exponent and assign            **=
3. multiply and assign            *=
4. division and assign            /=
5. floor division and assign      //=
6. modulus and assign             %=
7. add and assign                 +=
8. substract and assign           -=

9. left shift and assign          <<=
10. right shift and assign        <<=
11. bitwise AND and assign        &=
12. exclusive OR and assign       ^=
13. bitwise OR and assign         |=

------------------------------------------------------

walrus operator (:=)
- operation and assign 
- assign in operation

------------------------------------------------------

Groups of operators (8) 
1. Arithmetic operator(9) 
2. Bitwise operators(6)
3. Comparison operators (6) 
4. Identity operators (2)
5. Membership operators (2)
6. Logical operator (3)
7. Conditional operator (1)
8. Assignment (14)

------------------------------------------------------

Exercises
1. Precedence (15)
2. Operators (43)
3. Groups of operators (8) 
4. Groups of operators by operand (3) (4, 38, 1)
5. Associativity (e u assign) (19, 24)

------------------------------------------------------------------------------------------------------------

Precedence 15 ခုက ဒါကို အလွတ်ကျက်ရပါမယ်။

(e u */ +-) 
(shift and or 2) 
(c not and or) 
(t assignment walrus)

#################################################

Associativity ကတော့ (e u assign) ကို အလွတ်ကျက်ရပါမယ်။

#################################################

အနှစ်ချုပ်

e u မြှောက်စား ပေါင်းနှုတ်
shift and or နှစ်ခု
c not and or
t assignment walrus 


e u assign

#################################################

ဒီအတိုကောက်နှစ်ခုတည်းနဲ့ 

1. Precedence (15)
2. Operators (43)
3. Groups of operators (8 ) 
4. Groups of operators by operand (3) (4, 38, 1)
5. Associativity (e u assign) (19, 24)

ဒီငါးခုလုံးကို ပြန်ပြီး ပုံဖော်နိုင်ရပါမယ်။

##################################################################################################


"""

