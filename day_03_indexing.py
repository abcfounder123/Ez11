"""

Indexing
   - positive index 
   - negative index
   - range => -t to t-1
   - hard = total - abs(easy)
   - f1, f5, f10, l1, l5, l10
   - middle index
     - odd, m = t // 2 
     - even, rm = t // 2, lm = rm - 1  
   
indexing အနှစ်ချုပ်
1. အညွှန်းနံပါတ် နှစ်မျိုးလုံးကို သိပြီး လွယ်တာရော ခက်တာရော ရှာတတ်ရမယ်။
2. သုံးလို့ရတဲ့ range ကို သိရမယ်။
3. f5, l5, middle ရှာတတ်ရမယ်။

################################################# 
 
 "abcdefg"

  a  b  c  d  e  f  g 
  0  1  2  3  4  5  6     positive index
 -7 -6 -5 -4 -3 -2 -1     negative index

#################################################

positive index (left to right)

f1 = 0
f5 = 4
f10 = 9

total = 196
l1 = t - 1 = 195
l2 = t - 2 = 194
l5 = t - 5 = 191  
l10 = t - 10 = 186

total = 200
l1 = t - 1 = 199
l5 = t - 5 = 195 
l10 = t - 10 = 190

middle = total // 2

#################################################

negative index (right to left)

l1 = -1
l2 = -2
l5 = -5
l10 = -10

total = 196
f1 = t = -196
f2 = t - 1 = -195
f3 = t - 2 = -194
f5 = t - 4 = -192
f10 = t - 9 = -187

#################################################

"range"   

total => 7
range => -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6

total => 10
range => -10, -9, -8, -7, -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7  8  9

total => 100
range => -100 to 99

total => 1000
range => -1000 to 999

total => 39
range => -39 to 38

total => 27
range => -27 to 26

total => t
range => -t to t-1

IndexError: string index out of range
IndexError: list index out of range
IndexError: tuple index out of range

#################################################

Access
>> x[i]

Update
>> x[i] = "mangoes"

Delete
>> del x[i]

##################################################################################################

"""