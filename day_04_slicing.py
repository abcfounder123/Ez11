

"""

"abcdefg"

  a  b  c  d  e  f  g 
  0  1  2  3  4  5  6     positive index
 -7 -6 -5 -4 -3 -2 -1     negative index


Slicing
   - value
   - index
   - start, stop, step

   - f5 (stop=5)
     >> 01234
     >> [:5]

   - l5 (start=-5)
     >> -5 -4 -3 -2 -1
     >> [-5:]

   - step
     >> left to right = +
     >> right to left = -

   - reverse => [::-1]

   - half, 1/3

   - 80%, 20%

slicing အနှစ်ချုပ်
1. f5, l5 ကို shortcut နဲ့ ထုတ်တတ်ရမယ်။
2. ပြောင်းပြန်လှန်တတ်ရမယ်။
အချမ်းသာဆုံးနိုင်ငံများစာရင်းရှိထားပေမယ့် အဆင်းရဲဆုံးနိုင်ငံများစာရင်းလိုအပ်လာတာမျိုးဆိုရင် ပြောင်းပြန်လှန်တတ်ရမယ်။
3. Binary search လိုမျိုးတွေအတွက် နှစ်ခု ပိုင်းတတ်ရမယ်။
Quantiles လိုမျိုးတွေအတွက် လေးခု ပိုင်းတတ်ရမယ်။
Train data, Test data တွေအတွက် 80% , 20% တွေ ခွဲတတ်ရမယ်။

#################################################

value = "bcde"
index = 1 2 3 4, -6 -5 -4 -3

1 2 3 4
start = 1
stop = 5
step = 1
=> [1:5:1]

-6 -5 -4 -3
start = -6
stop = -2
step = 1
=> [-6:-2:1]

#################################################

value = "edcb"
index = 4 3 2 1, -3 -4 -5 -6

4 3 2 1
start = 4
stop = 0
step = -1
=> [4:0:-1]

-3 -4 -5 -6
start = -3
stop = -7
step = -1
=> [-3:-7:-1]
 
#################################################     

"bcde"
>> b to f
start = b  (1 or -6)  
stop  = f  (5 or -2)
step  = +1           <--- left to right +

"edcb"
>> e to a
start = e  (4, -3)
stop  = a  (0, -7)
step  = -1           <--- right to left -

#################################################

f5 (stop=5)
>> [0:5:1]
>> [0:5]
>> [:5]

f10 (stop=10)
>> [0:10:1]
>> [0:10]
>> [:10]

fn (stop=n)

#################################################

l5 (start = -5)
-5 -4 -3 -2 -1
>> [-5::1]
>> [-5:]

l10 (start = -10)
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
>> [-10::1]
>> [-10:]

ln (start = -n)

#################################################

"reverse"

step 
>> pos  (left to right)
>> neg  (right to left)

reverse => [start:end:-1]

#################################################

Extra
1. half  => [:m], [m:] => even(equal), odd(r+1) 
2. 3     => [:p1], [p1:p2], [p2:]
3. 4     => [:p1], [p1:p2], [p2:p3], [p3:]
4. 5     => ?
6. 6     => ?

- 75% => start, 3/4, 75/100
- 25% => start, 1/4
- 80% => start, 4/5
- 20% => start, 1/5
- 80%, 20% => [:4/5], [4/5:]
- 83%, 17% => [:83/100], [83/100:]
- 86%, 14% => ?

#################################################

"Test for 1/3"

a b c d e f g h i j k l         t=12, p1=4, p2=8
0 1 2 3 4 5 6 7 8 9 10 11

"abcd" + "efgh" + "ijkl"

[:p1]  + [p1:p2] + [p2:]

#################################################

>> Test for "1/4"

x = "abcdefghijkl"

t = len(x)

p1 = t // 4
p2 = p1 * 2
p3 = p1 * 3

h1 = x[:p1]
h2 = x[p1:p2]
h3 = x[p2:p3]
h4 = x[p3:]

print(h1)
print(h2)
print(h3)
print(h4)

#################################################

>> 83%, 17% => [:83/100], [83/100:]

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

t = len(x)
p = t // 100 * 83

train_data = x[:p]
test_data = x[p:]

print(train_data)
print(test_data)

#################################################

richest = ['country.1', 'country.2', 'country.3', 'country.4', 'country.5', 'country.6', 'country.7', 'country.8', 'country.9', 'country.10', 'country.11', 'country.12', 'country.13', 'country.14', 'country.15', 'country.16', 'country.17', 'country.18', 'country.19', 'country.20', 'country.21', 'country.22', 'country.23', 'country.24', 'country.25', 'country.26', 'country.27', 'country.28', 'country.29', 'country.30', 'country.31', 'country.32', 'country.33', 'country.34', 'country.35', 'country.36', 'country.37', 'country.38', 'country.39', 'country.40', 'country.41', 'country.42', 'country.43', 'country.44', 'country.45', 'country.46', 'country.47', 'country.48', 'country.49', 'country.50', 'country.51', 'country.52', 'country.53', 'country.54', 'country.55', 'country.56', 'country.57', 'country.58', 'country.59', 'country.60', 'country.61', 'country.62', 'country.63', 'country.64', 'country.65', 'country.66', 'country.67', 'country.68', 'country.69', 'country.70', 'country.71', 'country.72', 'country.73', 'country.74', 'country.75', 'country.76', 'country.77', 'country.78', 'country.79', 'country.80', 'country.81', 'country.82', 'country.83', 'country.84', 'country.85', 'country.86', 'country.87', 'country.88', 'country.89', 'country.90', 'country.91', 'country.92', 'country.93', 'country.94', 'country.95', 'country.96', 'country.97', 'country.98', 'country.99', 'country.100', 'country.101', 'country.102', 'country.103', 'country.104', 'country.105', 'country.106', 'country.107', 'country.108', 'country.109', 'country.110', 'country.111', 'country.112', 'country.113', 'country.114', 'country.115', 'country.116', 'country.117', 'country.118', 'country.119', 'country.120', 'country.121', 'country.122', 'country.123', 'country.124', 'country.125', 'country.126', 'country.127', 'country.128', 'country.129', 'country.130', 'country.131', 'country.132', 'country.133', 'country.134', 'country.135', 'country.136', 'country.137', 'country.138', 'country.139', 'country.140', 'country.141', 'country.142', 'country.143', 'country.144', 'country.145', 'country.146', 'country.147', 'country.148', 'country.149', 'country.150', 'country.151', 'country.152', 'country.153', 'country.154', 'country.155', 'country.156', 'country.157', 'country.158', 'country.159', 'country.160', 'country.161', 'country.162', 'country.163', 'country.164', 'country.165', 'country.166', 'country.167', 'country.168', 'country.169', 'country.170', 'country.171', 'country.172', 'country.173', 'country.174', 'country.175', 'country.176', 'country.177', 'country.178', 'country.179', 'country.180', 'country.181', 'country.182', 'country.183', 'country.184', 'country.185', 'country.186', 'country.187', 'country.188', 'country.189', 'country.190', 'country.191', 'country.192', 'country.193', 'country.194', 'country.195', 'country.196', 'country.197', 'country.198', 'country.199', 'country.200']

poorest_10 = richest[-10:][::-1]
print(poorest_10)

##################################################################################################

"""


