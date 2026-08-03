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
   - ternary operator  =>   (Left operand, Right operand, Middle operand)

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

6. Bitwise NOT ( ~ )


1 -----  NOT  ----- 0

0 -----  NOT  ----- 1

0011 -----  NOT  ----- 1100

~ 0011
=> 1100

------------------------------------------------------

Comparison operators (6) (equal, greater) (boolean value)

1. Equal                    == 
2. Not equal                !=
3. Greater than             >
4. Less than                <
5. Greater than or Equal    >=
6. Less than or Equal       <=

------------------------------------------------------

"""


