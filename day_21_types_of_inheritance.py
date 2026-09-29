
"""

OOP
- Attributes
- Inheritance

#################################################

Inheritance
- parent and child 
- code reuse

#################################################

Types of inheritance
1. Single inheritance 
2. Multiple inheritance
3. Mutilevel inheritance 
4. Hierarchical inheritance
5. Hybrid inheritance

#################################################

1. Single inheritance

       Animal  

         |

        Dog


class Animal:
    def eat(self):
        print("Animal eat.")


class Dog:
    def eat(self):
        print("Animal eat.")

    def bark(self):
        print("Dog bark.")


#################################################


class Animal:
    def eat(self):
        print("Animal eat.")


class Dog(Animal):
    def bark(self):
        print("Dog bark.")


x = Dog()
x.eat()
x.bark()

#################################################

2. Multiple inheritance  

          Father   Mother
             \\     /
               Child


      old.1  old.2  old.3  old.4  old.5  old.6  old.7    =>  700
      
          \\           |             /             /

                     New                                 => old 400   


class New(old.1, old.3, old.5, old.7):
    pass

#################################################

class Phone:
    def call(self, number):
        print("Calling to ", number)


class Camera:
    def take_photo(self):
        print("Taking a photo.")


class SmartPhone:
    def call(self, number):
        print("Calling to ", number)

    def take_photo(self):
        print("Taking a photo.")

#################################################

class Phone:
    def call(self, number):
        print("Calling to ", number)


class Camera:
    def take_photo(self):
        print("Taking aa photo.")


class SmartPhone(Phone, Camera):
    pass


y = Phone()
y.call("09123456")

z = Camera()
z.take_photo()

x = SmartPhone()
x.call("09123456")
x.take_photo()

#################################################

3. Mutilevel inheritance

          Grand X  
            |
         Parent Y       Single inheritance
            |
          Child Z       Mutilevel inheritance


class X:
    def x(self):
        print("x")


class Y(X):
    def y(self):
        print("y")


class Z(Y):
    def z(self):
        print("z")


a = Z()
a.z()
a.y()
a.x()


#################################################

4. Hierarchical inheritance


                        Human     
                     
                     /    |     \\
                    
                 white   Brown  Black



            X          eat .1

         /     \\

      Y           Z
     bark        meow



class Animal:
    def eat(self):
        print("Animal eat.")


class Dog:
    def eat(self):
        print("Animal eat.")

    def bark(self):
        print("Dog bark.")


class Cat:
    def eat(self):
        print("Animal eat.")

    def meow(self):
        print("Cat meow.")


#################################################

class Animal:
    def eat(self):
        print("Animal eat.")


class Dog(Animal):
    def bark(self):
        print("Dog bark.")


class Cat(Animal):
    def meow(self):
        print("Cat meow.")

x = Dog()
x.eat()
x.bark()

#################################################

            X  

         /     \\

      Y           Z



class X:
    pass


class Y(X):
    pass


class Z(X):
    pass


#################################################

5. Hybrid inheritance

              A       Hierarchical inheritance

           /     \\

          B        C      single

           \\     /

               D      (multiple + multilevel) => Hybrid


D(B, C)            (multiple)
D <- B <- A        (multilevel)
D <- C <- A        (multilevel)

################################################################################################## 

"""