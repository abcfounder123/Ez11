
"""

Object-oriented Programming

- a paradigm based on the concept of "objects"
- paradigm ဂရိစကားလုံး တွေးပုံတွေးနည်း
- concept အယူအဆ / အမြင်
- object  အရာဝတ္ထု

အရာဝတ္ထုဆိုတဲ့ အယူအဆအပေါ်မှာ အခြေခံထားတဲ့ တွေးပုံတွေးနည်း ဖြစ်ပါတယ်။

အရာဝတ္ထုလို့တွေးပြီး program ရေးတာ ဖြစ်ပါတယ်။

##################################################

Attributes exercises

အရာဝတ္ထုတွေမှာ ကိုယ်ပိုင် ပိုင်ဆိုင်မှုတွေ ရှိကြပါတယ်။

ဒီနေ့သင်ခန်းစာက ပိုင်ဆိုင်မှုနဲ့ပတ်သတ်ပြီး စနစ်တကျ တွေးတတ်ဖို့ ဖြစ်ပါတယ်။

အဆင့်ဆယ်ဆင့်ရှိပြီး ပထမနှစ်ဆင့်ကို လေ့ကျင့်ပြီး အသားကျမှသာ ကျန်တာတွေ ဆက်လေ့လာလို့ရပါမယ်။

##################################################

1. Write

ပထမအဆင့်ကတော့ အတွေးတွေကို ချရေးတာ ဖြစ်ပါတယ်။

အများကြီးနဲ့ ရှုတ်ရှုတ်ထွေးထွေး မတွေးပဲ နည်းနည်းလေးနဲ့ ရိုးရိုးလေးပဲ တွေးရပါမယ်။

ရိုးရိုးလေးတွေးပြီး ရေးတတ်စေချင်တာပါ။

##################################################

2. Divide (data, fun/method)

leg = 2
hand = 2

def walk():


ဒုတိယအဆင့်ကတော့ ရေးထားတာကို ခွဲထုတ်တာ ဖြစ်ပါတယ်။

ခွဲထုတ်တဲ့အချိန်မှာ အတွေးတွေကို ဖျောက်ထားရမှာဖြစ်ပြီး အသစ်ထပ်ထည့်တာတွေ မလုပ်ရပါဘူး။

ရေးထားတဲ့အတိုင်းဖတ်ပြီး စက်ရုပ်လိုမျိုး ခွဲထုတ်ပေးရပါမယ်။

ခွဲထုတ်ရင်းနဲ့ data ဘယ်နှစ်ခု၊ function ဘယ်နှစ်ခု စသဖြင့် အရေအတွက်အပါအဝင် ပေးထားတဲ့အမည်တွေနဲ့ အလုပ်လုပ်ပုံတွေကိုပါ တစ်ခါတည်း အလွတ်ရအောင် မှတ်ထားဖို့လည်း လိုအပ်ပါသေးတယ်။

မှန်မှန်ကန်ကန် ခွဲထုတ်တတ်ဖို့နဲ့ မှတ်တတ်တဲ့အကျင့် ရှိစေချင်တာပါ။

##################################################

Python ၏ အနှစ်သာရ

1. လှတာ ပိုကောင်းတယ်။

2. ရှင်းလင်းတာ ပိုကောင်းတယ်။

3. အတွေးတွေဟာ ရိုးရှင်းနေရမယ်။

###################################################################################################

Answers of Attribute Exercises 

Step.1   --->   Write

Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, tires, engine)

Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။  (size, pressure=0) ( pump(p) )
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။  (fuel_type, state="off") 
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

#################################################

Step.2   --->   Divide

class   --->   Car
data    --->   VIN, tires, engine
method  --->

class   --->  Tires
data    --->  size, pressure = 0
method  --->  pump(p)

class   --->  Engine
data    --->  fuel_type, state = off
method  --->  on(), off()

#################################################

Step.3   --->   Draw


class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        pass


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        pass

    def off(self):
        pass
          

#################################################

Step.4   --->   controlling data by fun 

1. pressure by pump()  
   >> self.pressure = x
   
2. state by on() and off() 
   >> self.state = "on"
   >> self.state = "off"
        
        
class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        print(f"pump to {x} psi.")
        self.pressure = x


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        print("ON")
        self.state = "on"

    def off(self):
        print("OFF")
        self.state = "off"
        
        
#################################################


"""