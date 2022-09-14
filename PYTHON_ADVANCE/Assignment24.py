#1 create a user class with 3 properties

'''class user:
    def __init__(self):
        self.name="deepanshu"
        self.age=20
        self.email="dk1078451@gmail.com"

    def show(self):
        print(self.name)
        print(self.age)
        print(self.email)

u1=user()
u1.show()'''


#2

'''class user:
    def __init__(self):
        print("happy birthday to you")


u1=user()'''


#3

'''class user:
    def __init__(self):
        self.a="deepanshu"
        self.b="durgersh"

    def show(self):
        print(self.a)
        print(self.b)



u1=user() 
u1.show()       
u2=user()
u2.show()'''


#4

'''class user:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def show(self):
        print(self.a)
        print(self.b)


u1=user("deepanshu",1)
u1.show()'''


#5

'''class user:
    def __init__(self,a):
        self.age=a
        #self.b=
    def show(self):
        del self.age
        print(self.age) 

u1=user(20)
u1.show()'''

#6

'''class user:
    def __init__(self,a,b,c):
        self.age1=a
        self.age2=b
        self.age3=c
    def show(self):
        if self.age1<self.age2:
            if self.age1<self.age2:
                print("age1 is youngest",self.age1)
        elif self.age2<self.age3:
            print("age2 is youngerst",self.age2)
        else:            
            print("self",self.age3)

u1=user(12,34,22)
u1.show()
print()            '''


#7

'''class laptop:
    def __init__(self):
        self.brand="HP"
        self.ram1=512
        self.ram2=912
        self.ram3=341
        self.cpu="i3"
        self.hdd="34"

    def showconfig(self):
        print(self.brand)
        print(self.ram)
        print(self.cpu)
        print(self.hdd)

l1=laptop()
l1.showconfig()
l2=laptop()
l3=laptop()
l3=[l1.ram1,l2.ram2,l3.ram3]
print(sorted(l3))'''

#8


'''class school:
    name="deepanshu kumar"
    def __init__(self):
        self.roll=12
        self.day="monday"
    @classmethod
    def hlo(cls):
        print(cls.name) 
    def show(self):
        print(self.roll)
        print(self.day)

s1=school()
s1.show()
school.hlo()        
print()'''

#10

'''class employee:
    def __init__(self):
        self.empid=3
        self.name="deepanshu"
        self.salary=1000000
    def set_data(self,a,b,c):
        self.empid=a 
        self.name="deepanshu kumar"
        self.salary=c

    def get(self):
        return self.empid
    def get1(self):
        return self.name
    def get3(self):
        return self.salary

e1=employee()
e1.set_data(2,0,39999)
print(e1.get())
print(e1.get1())
print(e1.get3())
print()'''

