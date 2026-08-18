
"""

1. Sequence
   - top
   - left
   - parenthesis first

#################################################

2. Selection (if, elif, else)

#####################################

1. if

ချိတ်ဆက်ထားတဲ့ condition မှန်ရင် အလုပ်လုပ်သည်။

#####################################

mark = int(input("Marks = "))

if mark >= 40:
    print("Exam pass.")

#####################################

2. else

ချိတ်ဆက်ထားတဲ့ condition မှားရင် အလုပ်လုပ်သည်။

#####################################

mark = int(input("Marks = "))

if mark >= 40:
    print("Exam pass.")

else:
    print("Exam fail.")

#####################################

mark = int(input("Marks = "))

c1 = mark >= 40

if c1:
    print("Exam pass.")

else:
    print("Exam fail.")

#####################################

3. all from all , one from one

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

if c2: print("Programmer.")

if c3: print("Engineer.")

if c4: print("Distance.")

#####################################

mark = 500

if mark >= 500: print("Doctor.")

if mark >= 400: print("Programmer.")

if mark >= 300: print("Engineer.")

if mark >= 240: print("Distance.")

if mark < 240:: print("Grade.12")

#####################################

4. one from all

mark = 400

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

if not c1 and c2: print("Programmer.")

if not c1 and not c2 and c3: print("Engineer.")

if not c1 and not c2 and not c3 and c4: print("Distance.")

#####################################

5. one from all by Python ( elif ) ( else + if )

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

elif c2: print("Programmer.")

elif c3: print("Engineer.")

elif c4: print("Distance.")

#####################################

Code Quality

1. if1
2. ge()
3. print

4. if2
5. gt
6. ge

7. if3
8. gt
9. ge

10. if4
11. gt
12. ge

13. if5
14. lt

14, 14 micro sec


mark = 500

if mark >= 500: print("Doctor.")

if 500 > mark >= 400: print("Programmer.")

if 400 > mark >= 300: print("Engineer.")

if 300 > mark >= 240: print("Distance.")

if mark < 240: print("Grade.12")

#####################################

6. one from all by Python (if + elif + else)

500  (3, 3 micro sec)
1. if
2. ge
3. print

400  (4, 4 micro sec)


mark = 500

if mark >= 500: print("Doctor.")

elif mark >= 400: print("Programmer.")

elif mark >= 300: print("Engineer.")

elif mark >= 240: print("Distance.")

else: print("Grade.12")

##########################################################################

7. Exercise  

Write by (if + elif + else).

mark = 100

if 100 >= mark >= 90:
    print("A+")

if 90 > mark >= 80:
    print("A")

if 80 > mark >= 70:
    print("B")

if 70 > mark >= 50:
    print("C")

if mark < 50:
    print("Fail")
    
##########################################################################
##########################################################################


"""

