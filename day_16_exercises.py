
"""

Exercises (27)

1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)

------------------------------------------

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )

------------------------------------------

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

------------------------------------------

4. is_lower (a to z တွေက lower case character ဖြစ်ပါတယ်။)

------------------------------------------

5. is_upper (A to Z တွေက upper case characterဖြစ်ပါတယ်။)

------------------------------------------

6. is_alphabet (a to z တွေက english အက္ခရာဖြစ်ပါတယ်။)

------------------------------------------

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )

------------------------------------------

8. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )
    - "I go to school."
    - ".loohcs ot og I"

------------------------------------------

9. Lower case to upper case

------------------------------------------

10. Upper case to lower case

------------------------------------------

11. upper()

------------------------------------------

12. lower()

------------------------------------------

13. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 )

------------------------------------------

14. less number ( n1 < n2 )

------------------------------------------

15. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)

------------------------------------------

16. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)

------------------------------------------

17. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။
    
------------------------------------------

18. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)

------------------------------------------

19. summation
    => summation of 5 = 1 + 2 + 3 + 4 + 5 = 15

------------------------------------------

20. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120

------------------------------------------

21. Linear search

------------------------------------------

22. Binary search

------------------------------------------

23. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)

------------------------------------------

24. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)

Add item to dict
d["I"] = 1

Access dict value
d["I"]

Update dict value
d["I"] = 2
d["I"] += 1

------------------------------------------

25. leap year (ရက်ထပ်နှစ်) (Julian calendar)
 >> divisible by 4  (y % 4 == 0)

------------------------------------------

26. leap year (ရက်ထပ်နှစ်) (Gregorian calendar)
>> divisible by 400 ( eg. 2000, 1600 )       ( y % 400 == 0 )
>> divisible by 4 and not divisible by 100   ( y % 4 == 0 and y % 100 != 0 )
>> Rule.1 or Rule.2

------------------------------------------

27. leap year (ရက်ထပ်နှစ်) Modern calendar
>> divisible by 400 and not divisible by 3200  ( y % 400 == 0 and y % 3200 != 0 )
>> divisible by 4 and not divisible by 100     ( y % 4 == 0 and y % 100 != 0 )

------------------------------------------

Summary
=> +1 days by 4 years                     <---  Julian
=> -3 days by 400 years                   <---  Gregorian
=> -1 days by 3200 years                  <---  Modern

------------------------------------------------------------------------------------     

Answers (27)    


1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)


def is_even(n):
    return n % 2 == 0
    

------------------------------------------

"Test"


def is_even(n):
    return n % 2 == 0


data = [100, 50, 75, 60, 20, 18, 6, 4, 1, 3]
even = []
odd = []

for n in data:
    if is_even(n):
        even.append(n)
    else:
        odd.append(n)


print(even)
print(odd)

------------------------------------------

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )

def is_odd(n):
    return n % 2 == 1

------------------------------------------

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

def is_number(c):
    return c in "0123456789"
    
------------------------------------------

"Test"


def is_number(c):
    return c in "0123456789"


x = "My phone number is 091234567."
y = ""

for c in x:
    if is_number(c):
        y += c

print(y)

------------------------------------------

4. is_lower (a to z တွေက lower case character ဖြစ်ပါတယ်။)


def is_lower(c):
    return c in "abcdefghijklmnopqrstuvwxyz"
    

------------------------------------------

5. is_upper (A to Z တွေက upper case characterဖြစ်ပါတယ်။)


def is_upper(c):
    return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


------------------------------------------

6. is_alphabet (a to z တွေက english အက္ခရာဖြစ်ပါတယ်။)


def is_alphabet(c):
    return c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


------------------------------------------

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )


def is_palindrome(word):
    return word == word[::-1]


def is_palindrome(word):
    return word.lower() == word[::-1].lower()

------------------------------------------

8. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )
    - "I go to school."
    - ".loohcs ot og I"

------------------------------------------

9. Lower case to upper case


def lower_upper(c):
    return chr(ord(c) - 32)

------------------------------------------

10. Upper case to lower case


def upper_lower(c):
    return chr(ord(c) + 32)
 

------------------------------------------

11. upper()


def upper(s):
    ans = ""

    for c in s:
        ans += lower_upper(c)

    return ans
    
    

def upper(s):
    ans = ""

    for c in s:
        if is_lower(c):
            ans += lower_upper(c)
        else:
            ans += c

    return ans


------------------------------------------

12. lower()


def lower(s):
    ans = ""

    for c in s:
        ans += upper_lower(c)

    return ans
    

def lower(s):
    ans = ""

    for c in s:
        if is_upper(c):
            ans += upper_lower(c)
        else:
            ans += c

    return ans
  
------------------------------------------

"Test"


def is_lower(c):
    return c in "abcdefghijklmnopqrstuvwxyz"


def is_upper(c):
    return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def lower_upper(c):
    return chr(ord(c) - 32)


def upper_lower(c):
    return chr(ord(c) + 32)


def upper(s):
    ans = ""

    for c in s:
        if is_lower(c):
            ans += lower_upper(c)
        else:
            ans += c

    return ans


def lower(s):
    ans = ""

    for c in s:
        if is_upper(c):
            ans += upper_lower(c)
        else:
            ans += c

    return ans


x = "I go to school by bus."
y = upper(x)
z = lower(x)

print(y)
print(z)

------------------------------------------

13. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 )


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

------------------------------------------

14. less number ( n1 < n2 )


def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2

------------------------------------------


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    elif n1 == n2:
        return n2


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return n2


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


1 sec
2 sec
3 sec

1 sec
2 sec
2 sec

1 sec
1 sec
1 sec

------------------------------------------

15. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)


def max(l):
    m = l[0]
    for n in l[1:]:
        m = greater_number(m, n)
    return m
    

------------------------------------------

16. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)


def min(l):
    m = l[0]
    for n in l[1:]:
        m = less_number(m, n)
    return m


------------------------------------------

17. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။


def find_max_min(l):
    return max(l), min(l)
    

------------------------------------------

"Test"


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


def max(l):
    m = l[0]
    for n in l[1:]:
        m = greater_number(m, n)
    return m


def min(l):
    m = l[0]
    for n in l[1:]:
        m = less_number(m, n)
    return m


def find_max_min(l):
    return max(l), min(l) 


x = [100, 5, 7, 400, 200, 40, 300, 25]
m = find_max_min(x)
print(m)

------------------------------------------

"Wrong example"


def find_max_min(l):
    max = l[0]
    for n in l[1:]:
        if n > max:
            max = n

    min = l[0]
    for n in l[1:]:
        if n < min:
            min = n

    return max, min
    
    
------------------------------------------

18. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)


def sum(l):
    t = 0
    for n in l:
        t += n
    return t


------------------------------------------

19. summation
    => summation of 5 = 1 + 2 + 3 + 4 + 5 = 15


def summation(n):
    t = 1
    for i in range(2, n + 1):
        t += i
    return t
   
    
------------------------------------------

20. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120
    

def factorial(n):
    t = 1
    for i in range(2, n + 1):
        t *= i
    return t
    

------------------------------------------

21. Linear search


def linear_search(l, element):
    for n in l:
        if n == element:
            return True
    return False


------------------------------------------

"""
