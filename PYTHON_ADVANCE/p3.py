#1

'''class father:
    money=1000
    def show(self):
        print("parent class instance method")
    @classmethod
    def show1(cls):
        print("parent class method",cls.money) 

    @staticmethod
    def show2():
        a=12
        print(a) 

class son(father):
    def disp(self):
        print("son class method")              
#son class ka object father class ka har ek member ko 
#access kar lega.son child class hai aur father parent 
#class hai
s1=son()
s1.show()
son.show1()
s1.show2()
s1.disp()'''


#2

'''class deepanshu:
    x="champion"
    y=True
    def __init__(self):
        self.a=12
        self.b=23
        self.c,self.d="deepanshu","kumar"
    def show(self):
        print(self.a)
        print(self.b)
        print(self.c)
    @classmethod
    def show2(cls):
        print("This is a class method")       
class shivani(deepanshu):
    def disp(self):
        print("in a child class method")
        print(self.a)
        return self.a,self.b,self.c,self.d

d1=shivani()
d1.show()
shivani.show2()                
d2=d1.disp()
print(d2)'''


#4

'''class father:
    def __init__(self):
        self.a=12
        self.b=23
    def show(self):
        print("a=",self.a,"self.b",self.b)

class son(father):
    def disp(self):
        print(self.a)
        print(self.b)

s1=son()
s1.show()
s1.disp()               '''


#3

from re import M


'''class father:
    def __init__(self,m,n):
        self.a=m
        self.b=n
        print("deepanshu is a champion")
    def show(self):
        print("father class method")

class son(father):
    def disp(self):
        print("son class instance method",self.a)
        print(self.b)

s1=son(10,12)
s1.disp()
s1.show()'''