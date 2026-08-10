"""

Arithmetic operators in programming

------------------------------------------------------

Arithmetic operators(9) (e u */ +-)

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

Exercises of Arithmetic operators

1. age = 2026 - birth year, "You are 26 years old."
2. kyat to dollar, "10000 kyats is equal to 2 dollars."
3. 350 seconds is equal to 5 minutes and 50 seconds.
4. 90350 seconds is equal to 1 days 1 hours 5 minutes and 50 seconds.
5. Half-life calculator

------------------------------------------------------

1. input(), prompt letter
2. TypeCasting (int, str, ... )
3. print()
4. String concatenation (+)
5. String formatting  => f, {}

------------------------------------------------------

1. age = 2026 - birth year, "You are 26 years old."

birth_year = int(input("Birth year = "))
age = 2026 - birth_year
ans = "You are " + str(age) + " years old."
print(ans)

------------------------------------------------------

2. kyat to dollar, "10000 kyats is equal to 2 dollars."

kyat = input("Kyats = ")
dollar = int(kyat) / 5000
ans = kyat + " kyats is equal to " + str(dollar) + " dollars."
print(ans)

------------------------------------------------------

3. 350 seconds is equal to 5 minutes and 50 seconds.

sec = int(input("Seconds = "))
minute = sec // 60
second = sec % 60
ans = str(sec) + " seconds is equal to " + str(minute) + " minutes and " + str(second) + " seconds."
print(ans)

------------------------------------------------------

ans = f"{sec} seconds is equal to {minute} minutes and {second} seconds."

------------------------------------------------------

4. 90350 seconds is equal to 1 days 1 hours 5 minutes and 50 seconds.

                90350 seconds
            
         1505 min          50 sec
            
     25 hour    5 min    
            
  1 day   1 hour 

sec = int(input("Seconds = "))

min = sec // 60
second = sec % 60   # 50 sec

h = min // 60
minute = min % 60   # 5 min

day = h // 24       # 1 day
hour = h % 24       # 1 hour

ans = f"{sec} seconds is equal to {day} days {hour} hours {minute} minutes and {second} seconds."
print(ans)

------------------------------------------------------

5. Half-life calculator

                       500 g

                       250 g      6

                       125 g      6
       
500 / 2 / 2 / 2 
500 * 0.5 * 0.5 * 0.5     
500 * 0.5 ** 3

weight = int(input("Weight = "))
half = int(input("Half-life = "))
time = int(input("Time = "))
count = time / half
ans = 500 * 0.5 ** count
print(ans)

------------------------------------------------------------------------------------------------------------

"""