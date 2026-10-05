
"""

အရာဝတ္ထုတွေဟာ သီခြားစီဆိုပေမယ့် အလုပ်လုပ်တဲ့အခါမှာတော့ ပေါင်းစပ်ပြီး လုပ်ကြရပါတယ်။

programming မှာလည်း ဒီအယူအဆကို ယူသုံးထားပါတယ်။

ပေါင်းစပ်မှု ပုံစံနှစ်မျိုး

1. ခိုင်မြဲသော တွဲစပ်မှု (မိဘနဲ့ သားသမီးလိုမျိုး)
2. လျော့ရဲသော တွဲစပ်မှု (အသိမိတ်ဆွေလိုမျိုး)

Data အယူအဆအရဆိုရင်တော့ 'is a' relation နဲ့ 'has a' relation ဆိုပြီး ခေါ်ကြပါတယ်။
OOP အယူအဆအရဆိုရင်တော့ inheritance နဲ့ composition ဆိုပြီး ခေါ်ကြပါတယ်။

Tightly couple    =>  'is a', inheritance
Loosely couple    =>  'has a', composition

BMW is a Car.     =>  'is a', inheritance       BMW(Car)
BMW has a Tire.   =>  'has a', composition      self.tire = t

ခြေလက်လိုမျိုး အသေထားချင်ရင် tightly coupled.
အဝတ်အစားလိုမျိုး အလွယ်တကူ လဲလှယ်ချင်ရင် loosely coupled.

#################################################

class BMW(Car):        <---   inheritance 
    pass


class BMW(Car):
    def __init__(self, t):
        self.tire = t        <---   composition
        
#################################################

တကယ်‌တော့ has a relation မှာလည်း strong နဲ့ weak ဆိုပြီး နှစ်ခု ရှိပါသေးတယ်။

-------------------------------------------------

"Composition"

object ပျက်စီးတဲ့အခါ ပေါင်းစပ်ထားတာပါ ပျက်စီးခဲ့ရင် strong has a တစ်နည်းအားဖြင့် composition 

>> Car(VIN="BMW-0001", tires=Tires(15), engine=Engine("Petrol"))

-------------------------------------------------

"Aggregation"

object ပျက်စီးတဲ့အခါ ပေါင်းစပ်ထားတာက ဆက်ပြီးရှိနေခဲ့ရင် weak has a တစ်နည်းအားဖြင့် aggregation

e1 = Engine("Petrol")
Car(VIN="BMW-0001", tires=Tires(15), engine=e1)

အလွယ်မှတ်ရရင် Engine ကို အပြင်မှာ သီးသန့်ဖန်တီးရင် weak ပေါ့။

#################################################

Composition / aggregation example (Loosely couple)

data တွေကို အသေမဟုတ်ပဲ ချိတ်ဆက်ချင်ရင် assignment operator သုံးရပါမယ်။


class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine     # Car has an engine. "has a"


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, p):
        print(f"pump to {p} psi.")


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        print(f"{self.fuel_type} Engine On.")

    def off(self):
        print(f"{self.fuel_type} Engine Off.")

    def __repr__(self):
        return f"{self.fuel_type} Engine"


# city_car -> "BMW-0001", 15" tires, Petrol engine
# 7psi, on

city_car = Car(VIN="BMW-0001", tires=Tires(15), engine=Engine("Petrol"))  # strong has a
print(city_car.engine)

city_car.engine = Engine("Gas")     # <---  Loosely couple (Engine ကို အလွယ်တကူ အသစ်လဲနိုင်ပါတယ်။)
print(city_car.engine)

-------------------------------------------------

e1 = Engine("Petrol")

city_car = Car(VIN="BMW-0001", tires=Tires(15), engine=e1) # weak has a
print(city_car.engine)

del city_car
print(e1)

##################################################################################################

Inheritance exercise

1. Jet လေယာဉ်တွင် တိုက်ခိုက်မှုအမျိုးအစား ၊ အမည်နှင့် ထုတ်လုပ်သောနိုင်ငံဟူသော အချက်အလက်ပါရှိသည်။
F35 နှင့် F22 သည် Jet လေယာဉ်ဖြစ်သည်။ 

#################################################

F35 နှင့် F22 သည် Jet လေယာဉ်ဖြစ်သည်။ ( is a relation ) (tightly coupled) (inheritance) 

F35 is a Jet.
F22 is a Jet.

       Jet
     /     \\
   F35     f22

#################################################

Jet လေယာဉ်တွင် တိုက်ခိုက်မှုအမျိုးအစား ၊ အမည်နှင့် ထုတ်လုပ်သောနိုင်ငံဟူသော အချက်အလက်ပါရှိသည်။

name     -->  Jet
data     -->  role, name, country
method   -->


class Jet:
    def __init__(self, role, name, country):
        self.role = role
        self.name = name
        self.country = country


# F35 သည် Jet လေယာဉ်ဖြစ်သည်။ is a,
class F35(Jet):
    pass

# F22 သည် Jet လေယာဉ်ဖြစ်သည်။
class F22(Jet):
    pass


x = F35("Multirole", "F35-001", "USA")

print(x.__dict__)

#################################################

                  Car

                /     \\

            BMW       TOYOTA

parent class, super class, base class
child class, sub class, derived class


ဝေမျှမှုပုံစံကို ရည်ညွှန်းချင်ရင် parent and child        A B

အုပ်စုခွဲတာကို ပေါ်လွင်စေချင်ရင် super and sub         4, 8, 

ဆင့်ပွားမှုပုံစံကို မြင်စေချင်ရင် base and derived        pt

#################################################

2.

I, J, K သည် A ၏ sub class ဖြစ်သည်။
X သည် I ၏ sub class ဖြစ်သည်။
Y သည် J ၏ sub class ဖြစ်သည်။
Z သည် K ၏ sub class ဖြစ်သည်။

ပုံဆွဲပါ။ class တည်ဆောက်ပါ။


I, J, K သည် A ၏ sub class ဖြစ်သည်။
A သည် I, J, K  ၏ super class ဖြစ်သည်။

               A

           /   |   \\

        I      J      K

X သည် I ၏ sub class ဖြစ်သည်။

            I

            |

            X

Y သည် J ၏ sub class ဖြစ်သည်။

            J

            |

            Y

Z သည် K ၏ sub class ဖြစ်သည်။

            K

            |

            Z


               A

           /   |   \\

        I      J      K

      /        |       \\

    X          Y         Z


class A:
    pass


class I(A):
    pass


class J(A):
    pass


class K(A):
    pass


class X(I):
    pass


class Y(J):
    pass


class Z(K):
    pass


#################################################

3.  အောက်ပါပုံအတိုင်း class တည်ဆောက်ပါ။


                      Fruit           

              /         |        \\

         Apple        Mango       Banana  

                  /     |     \\

             မချစ်စု   စိန်တလုံး   တောသရက်


class Fruit:
    pass


class Apple(Fruit):
    pass


class Mango(Fruit):
    pass


class Banana(Fruit):
    pass


class မချစ်စု(Mango):
    pass


class စိန်တလုံး(Mango):
    pass


class တောသရက်(Mango):
    pass


#################################################

multiple inheritance exercises

4. ပန်းသီးနှင့် သစ်တော်သီးသည် သစ်သီးများဖြစ်ကြသည်။ 

ပန်းသစ်တော်သီးသည် ပန်းသီးနှင့် သစ်တော်သီးနှစ်မျိုးလုံးမှ မျိုးဗီဇများ အမွေဆက်ခံထားသည်။

ထို့ကြောင့် ပန်းသစ်တော်သီးသည် ပန်းသီးလည်း ဖြစ်သလို သစ်တော်သီးလည်းဖြစ်သည်။

ပုံဆွဲပြီး class တည်ဆောက်ပါ။


                       သစ်သီး

                     /        \\

                ပန်းသီး           သစ်တော်သီး

                    \\          /

                     ပန်းသစ်တော်သီး    


class သစ်သီး:
    pass


class ပန်းသီး(သစ်သီး):
    color = "white"
    pass


class သစ်တော်သီး(သစ်သီး):
    taste = "sweet"
    pass


class ပန်းသစ်တော်သီး(ပန်းသီး, သစ်တော်သီး):
    pass


x = ပန်းသစ်တော်သီး()
print(x.color)
print(x.taste)

#################################################

5.

A, B သည် Y ဖြစ်သည်။
C, D, E သည် Z ဖြစ်သည်။
X သည် A, B, C, D, E, F ဖြစ်သည်။
ပုံဆွဲပြီး class တည်ဆောက်ပါ။

#################################################


X သည် A, B, C, D, E, F ဖြစ်သည်။


A, B သည် Y ဖြစ်သည်။

                    Y

                 /     \\

               A           B


C, D, E သည် Z ဖြစ်သည်။               


                    Z

                 /   |  \\

               C     D     E


X သည် A, B, C, D, E, F ဖြစ်သည်။


               A    B   C   D   E   F

                \\   \\ |  /  /  /

                        X

#################################################

               Y          Z             

             /  \\     /  |  \\    

             A    B    C   D   E   F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X     

                       X  ABY CDEZ F



#                 Y

#            A   /\   B
#                \/

#                 X


class Y:
    pass
class Z:
    pass
class F:
    pass

class A(Y):
    pass
class B(Y):
    pass

class C(Z):
    pass
class D(Z):
    pass
class E(Z):
    pass

class X(A, B, C, D, E, F):
    pass
    

print(X.__mro__)  # X  ABY CDEZ F

#################################################

6. X ၏ attributes ကို ရှာဖွေပါက မည့်သည့်အစီအစဉ်အတိုင်း ရှာဖွေမည်နည်း။

                 
               Y          Z

             /  \\     /  |  \\    

             A    B    C   D   E   F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X                         

Method Resolution Order = X ->  A -> B -> Y  -> C -> D -> E -> Z  -> F


class Y:
    a = "Y"
    pass
class Z:
    a = "Z"
    pass

class A(Y):
    a = "A"
    pass
class B(Y):
    a = "B"
    pass

class C(Z):
    a = "C"
    pass
class D(Z):
    a = "D"
    pass
class E(Z):
    a = "E"
    pass

class F:
    a = "F"
    pass

class X(A, B, C, D, E, F):
    a = "X"
    pass


print(X.a) # X

#################################################

7. Method Resolution Order Exercise.1  => X BAY CDEZ F

               Y         Z

             /  \\    /  |  \\

             B   A   C   D   E    F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X      


class X(B, A, C, D, E, F):
    pass

#################################################

8. Method Resolution Order Exercise.2  => X CDEZ ABY F 

                Z             Y   

             /  |  \\        / \

            C   D     E     A   B   F

             \\   \\   |   /  /  /

                  \\ \\| / / /

                       X


class X(C, D, E, A, B, F):
    pass


#################################################

9. Method Resolution Order Exercise.3  => X F CDEZ ABY

                 Z             Y   

              /  |  \\        / \

       F    C    D     E     A   B  

         \\    \\   \\   |   /  /  

              \\   \\ \\| / / 

                       X

class Y:
    a = "Y"
    pass
class Z:
    a = "Z"
    pass

class A(Y):
    a = "A"
    pass
class B(Y):
    a = "B"
    pass

class C(Z):
    a = "C"
    pass
class D(Z):
    a = "D"
    pass
class E(Z):
    a = "E"
    pass

class F:
    a = "F"
    pass


class X(F, C, D, E, A, B):
    a = "X"
    pass


print(X.__mro__)

#################################################

10. Method Resolution Order Exercise.4  

=> Cross diamond example
=> X  A C BY DEZ F                            


                 Y       Z

               /    X    |  \\

              A   C   B  D   E    F

               \\   \\  |  /  /  /

                  \\ \\ | / / /

                        X       


class X(A, C, B, D, E, F):
    pass


#################################################

Diamond problem 
စိန်ပုံစံပျက်စီးလို့ ဖြစ်လာသော ပြဿနာ

consistent MRO
တစ်ခုကို တစ်ခါစီရှာရင် မှန်ကန်သော ရှာဖွေမှုပုံစံ

inconsistent MRO
တစ်ခုတည်းကို နှစ်ခါသုံးခါထပ်နေရင် မမှန်ကန်သော ရှာဖွေမှုပုံစံ

ပုံကို ကြည့်ပြီး စိန်ပုံစံမဖြစ်ရင် inconsistent MRO ဖြစ်နေကြောင်း အလွယ်တကူသိနိုင်။

"""
# A consistent method resolution order (MRO)

#                 Y

#            A   /\   B
#                \/

#                 X

# A, B သည် Y ဖြစ်သည်။
# X သည် A, B ဖြစ်သည်။  (A, B, Y)
"""

class X(A, B):
    pass


class X(Y, A, B):
    pass


"""
#################################################

# Not a consistent method resolution order

#                 Y
#              /

#          /    /   \
#              A      B
#          \    \   /
#            \
#              \
#                 X  


# X သည် Y, A, B ဖြစ်သည်။ (Diamond problem) (Y, A, B, Y)
# TypeError: Cannot create a consistent method resolution order (MRO)

#################################################  
"""

class Y:
    pass
class Z:
    pass
class F:
    pass

class A(Y):
    pass
class B(Y):
    pass

class C(Z):
    pass
class D(Z):
    pass
class E(Z):
    pass

class X(A, B, C, D, E, F):
    pass


print(X.__mro__)

#################################################

11. Method Resolution Order Exercise.5 


               Y         Z

             /  \\    /  |  \\

             A   B   C   D   E    F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X     

=> G is Y.
=> X is G.
=> X AGBY CDEZ F


Y
|
G      <---
|
X

               Y              Z

             /  | \\       /  |  \\

             A  G  B      C   D   E    F

               \\ \\  \\  |  /  /  /

                  \\ \\ \\| / / /

                         X       

class G(Y):
    pass


class X(A, G, B, C, D, E, F):
    pass


#################################################

12. Method Resolution Order Exercise.6 

                Y             Z

             /  | \\       /  |  \\

             A  G  B      C   D   E    F

               \\ \\  \\  |  /  /  /

                  \\ \\ \\| / / /

                         X     


=> H is Z.
=> X is H.
=> X AGBY CHDEZ F

Z
|
H    <---
|
X  

"""
#              Y              Z

#             / | \       / / | \

#             A G  B    C H  D   E   F

#               \ \ \   | | /  /  /

#                  \ \\ | |/ / /

#                        X

"""

class H(Z):
    pass


class X(A, G, B, C, H, D, E, F):
    pass


#################################################

13. Method Resolution Order Exercise.7  

=> X is I.
=> X AGBY CHDEZ F I

  I
  |
  X


"""
#              Y              Z

#             / | \       / / | \

#             A G  B    C H  D  E   F  I

#               \ \ \   | | /  /  / /

#                  \ \\ | |/ /  / /

#                        X


"""

class I:
    pass


class X(A, G, B, C, H, D, H, E, F, I):
    pass


#################################################

14. Method Resolution Order Exercise.8  

=> X is J.
=> X J AGBY CHDEZ F I

  J
  |
  X


"""
#              Y              Z

#             / | \       / / | \

#         J  A G  B     C H  D  E   F  I

#           \   \ \ \   | | /  /  / /

#               \  \ \\ | |/ /  / /

#                        X

"""

class J:
    pass


class X(J, A, G, B, C, H, D, E, Z, F, I):
    pass


#################################################

15. Method Resolution Order Exercise.9 

=> All is K.

               Y         Z

             /  \\    /  |  \\  

             A   B   C   D   E     F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X   

#################################################

=> All is K.

                     K


                /      \\   \\

               Y         Z

             /  \\    /  |  \\  \\

             A   B   C   D   E    F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X   

#################################################

class K:
    a = "K"
    pass

class Y(K):
    pass
class Z(K):
    pass
class F(K):
    pass

class A(Y):
    pass
class B(Y):
    pass

class C(Z):
    pass
class D(Z):
    pass
class E(Z):
    pass

class X(A, B, C, D, E, F):  
    pass

print(X.a)

#################################################

"""
