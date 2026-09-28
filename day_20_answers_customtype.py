"""

"CustomTypes"

Answers

#################################################

Step.1 (Draw Dollar Type)

Dollar ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n
        
    def add(self, other):
        return self.n + other.n

#################################################

Step.2 (Representation string -> "1 dollar")

ကိုယ်စားပြုမယ့်စာတန်ဖိုးကို 1 dollar လို့ ပေးချင်တာပါ။
    
    
class Dollar:
    def __init__(self, n):
        self.n = n
        
    def add(self, other):
        return self.n + other.n
        
    def __repr__(self):
        return f"{self.n} dollar"


#################################################

Step.3 ( + ) (__add__)

သင်္ကေတနဲ့ ပေါင်းချင်တာပါ။

    
class Dollar:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, other):
        return self.n + other.n
        
    def __repr__(self):
        return f"{self.n} dollar"
        

#################################################

Step.4 (result of addition => 3 dollar )

Dollar နှစ်ခုပေါင်းတဲ့အခါ ရလဒ်ကို dollar အဖြစ်နဲ့ပဲ လိုချင်တာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, other):
        return Dollar(self.n + other.n)
        
    def __repr__(self):
        return f"{self.n} dollar"


#################################################

Step.5 ( Design for Kyat )

Kyat ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Kyat(self.n + other.n)

    def __repr__(self):
        return f"{self.n} kyat"


#################################################

Step.6 (dollar + kyats)

dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် ပေါင်းချင်တာပါ။

#################################################


class Dollar:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n + other.n)
        if type(other) == Kyat:
            return Dollar(self.n + other.n / 5000)
                    
    def __repr__(self):
        return f"{self.n} dollar"
        
        
class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n + other.n)
        if type(other) == Dollar:
            return Kyat(self.n + other.n * 5000)

    def __repr__(self):
        return f"{self.n} kyat"


#################################################

Step.7 ( - ) ( __sub__ )

သင်္ကေတနဲ့ နှုတ်ချင်တာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n + other.n)
        if type(other) == Kyat:
            return Dollar(self.n + other.n / 5000)
    
    def __sub__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n - other.n)
        elif type(other) is Kyat:
            return Dollar(self.n - other.n / 5000)
               
    def __repr__(self):
        return f"{self.n} dollar"
        
        
class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n + other.n)
        if type(other) == Dollar:
            return Kyat(self.n + other.n * 5000)
            
    def __sub__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n - other.n)
        if type(other) == Dollar:
            return Kyat(self.n - other.n * 5000)
            
    def __repr__(self):
        return f"{self.n} kyat"
        
#################################################

Step.8 ( == ) ( __eq__ )

သင်္ကေတနဲ့ တန်ဖိုးတူလား နှိုင်းယှဉ်ချင်တာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n + other.n)
        if type(other) == Kyat:
            return Dollar(self.n + other.n / 5000)
    
    def __sub__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n - other.n)
        elif type(other) is Kyat:
            return Dollar(self.n - other.n / 5000)
               
    def __eq__(self, other):
        return self.n == other.n
    
    def __repr__(self):
        return f"{self.n} dollar"
        
        
class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n + other.n)
        if type(other) == Dollar:
            return Kyat(self.n + other.n * 5000)
            
    def __sub__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n - other.n)
        if type(other) == Dollar:
            return Kyat(self.n - other.n * 5000)
    
    def __eq__(self, other):
        return self.n == other.n
                
    def __repr__(self):
        return f"{self.n} kyat"
        
 
#################################################

Step.9 ( dollar == kyat )

dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် နှိုင်းယှဉ်ချင်တာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, other):
        if type(other) == Dollar:
            return Dollar(self.n + other.n)
        if type(other) == Kyat:
            return Dollar(self.n + other.n / 5000)
    
    def __sub__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n - other.n)
        elif type(other) is Kyat:
            return Dollar(self.n - other.n / 5000)
               
    def __eq__(self, other):
        if type(other) is Dollar:
            return self.n == other.n
        if type(other) is Kyat:
            return self.n == other.n / 5000
   
    def __repr__(self):
        return f"{self.n} dollar"
        
        
class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n + other.n)
        if type(other) == Dollar:
            return Kyat(self.n + other.n * 5000)
            
    def __sub__(self, other):
        if type(other) == Kyat:
            return Kyat(self.n - other.n)
        if type(other) == Dollar:
            return Kyat(self.n - other.n * 5000)
    
    def __eq__(self, other):
        if type(other) is Kyat:
            return self.n == other.n
        if type(other) is Dollar:
            return self.n == other.n * 5000
                
    def __repr__(self):
        return f"{self.n} kyat"
     
                         
#################################################


"""