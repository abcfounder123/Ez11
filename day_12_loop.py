
"""

1. Sequence

2. Selection (if, elif, else)

3. Loop
   1. Iteration - value  ( meaningful )
   2. Looping - 10 times ( underscore )
   3. nested loop   
   4. count (n=0, n+=1) 
   5. definite loop (for)
   6. indefinite loop (while)
   7. break => to stop loop
   8. exit() => to stop program
   9. else  => if, for, while

##########################################

1. Iteration

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]   

for number in numbers:
    print(f"2 x {number} = {2 * number}")

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")

##########################################

2. Looping - 12 times   (definite loop)

for _ in range(12):
    print("apple")

##########################################

for n in range(1, 11):
    print(f"{n}.I love you.")

for _ in range(10):
    print("I love you.")


for n in range(1, 11):    =>  iteration =>  1, ..., 10
for _ in range(10):       =>  loop      =>  10

##########################################

3. nested loop

print("2 x 1 = 2")

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
2 x 11 = 22
2 x 12 = 24

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")

print('-' * 42)

##########################################

for r in range(1, 13):
    print(f"2 x {r} = {2 * r}")
print("-" * 42)

for r in range(1, 13):
    print(f"3 x {r} = {3 * r}")
print("-" * 42)

for r in range(1, 13):
    print(f"4 x {r} = {4 * r}")
print("-" * 42)

for r in range(1, 13):
    print(f"5 x {r} = {5 * r}")
print("-" * 42)

....

....

##########################################

for l in range(1, 17):
    for r in range(1, 13):
        print(f"{l} x {r} = {l * r}")
    print("-" * 42)

##########################################

for l in range(1, 17):
    for r in range(1, 13):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)

    for r in range(12, 0, -1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)

##########################################

4. Count

fruits = ["apple", "banana", "orange", "mango"]
n = 0

for _ in fruits:
    n += 1
   
print(n)

##########################################

5. definite loop (for)

for _ in range(10):
    print("apple")

for _ in range(100):
    print("apple")

for _ in range(1000):
    print("apple")

##########################################    

6. Indefinite loop (while)

"Stop by condition"

condition = True

while condition:
    user_name = input("user name = ")
    password = input("password = ")
    if user_name == "Mg Mg" and password == "12345":
        print("Login successful")
        condition = False
    else:
        print("Try again.")
    print("-" * 42)

##########################################

7. break => to stop loop

"Stop by break"

while True:
    user_name = input("user name = ")
    password = input("password = ")
    if user_name == "abc" and password == "12345":
        print("login successful.(opened abc' account.)")
        break
    else:
        print("Wrong password. Try again.")
    print('-' * 42)

##########################################

"Indefinite loop with maximum count 3"

>> "Stop by condition" and "Stop by break"
>> Successfull and unsuccessfull


condition = True
n = 0

while condition:
    user_name = input("user name = ")
    password = input("password = ")
    if user_name == "abc" and password == "12345":
        print("Login successful")
        condition = False
    else:
        print("Try again.")
        n += 1
        if n == 3:
            print("Wait 24 hours.")
            break
    print("-" * 42)

##########################################

9. else  + (if, for, while)

>>  Successfully Done.

parents = ["UBa@gmail.com", "UMya@gmail.com", "DawMya@gmail.com"]

for email in parents:
    print(f"Sent Congratulation letter to {email}")

else:
    print("Successfully sent all email.")

##########################################

condition = True
n = 0

while condition:
    user_name = input("user name = ")
    password = input("password = ")
    if user_name == "abc" and password == "12345":
        print("Login successful")
        condition = False
    else:
        print("Try again.")
        n += 1
        if n == 3:
            print("Wait 24 hours.")
            break
    print("-" * 42)

else:
    print("Successfully Done.")

####################################################################################
####################################################################################

"""
