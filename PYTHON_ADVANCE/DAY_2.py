#constructuor in python
'''class mobile:
    def __init__(self):
        self.a="deepanshu"
        self.b=23
        self.c=12.34

    def show(self):
        print(self.a)
        print(self.b)
        print(self.c)

m1=mobile()
m1.show()'''

#2



'''class user:
    def __init__(self,n,m,x,z):
        self.a=n
        self.b=m
        self.c=x
        self.d=z

    def show(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)

u1=user(23,23,1,23,)
u1.show()
u1.a="deepanshu"
u1.b="mohit"
u1.c="deepak kumar"

print(u1.a,u1.b,u1.c,sep="\n")'''


#4

'''class user:
    def __init__(self,a,b,c):
        self.x=a
        self.y=b
        self.z=c

    def show(self):
        self.x="deepanshu"
        self.y=32
        print(self.x)
        print(self.y)
        print(self.z)

u1=user(23,43,12)
u1.show()'''


#4 instance variable

'''class user:
    def __init__(self):
        self.a=23
        self.b="deepanshu"
        self.c=32.23
        self.d=True
    def show(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)

u1=user()
u1.show()            '''


#5 

'''class mobile:
    def __init__(self):
        self.a="deepanshu kumar"
        self.model="Real me"
        self.country="india"
        self.price=1233.13

    def show(self):
        return self.a,self.country,self.price   


m1=mobile()
print(m1.show())
print()'''


#4

'''class user:
    def __init__(self):
        self.a="deepanshu"
        self.b="rahul"

    def show(self):
        return self.a,self.b
    def show(self,n,m):
        self.a=n
        self.b=m
        print(self.a,self.b)

u1=user()
u2=user()
u3=user()
u1.show()
u2.show()
u3.show()       '''


#6

class mobile:
    def __init__(self):
        self.model="Realme"
        self.price=3412.56
    def show(self):
        print(self.model)
        print(self.price)


realme=mobile()
redmi=mobile()
geek=mobile()

print("realme_model",realme.model)
print("redmi_model",redmi.model)
print("geek",geek.model)
print()
redmi.model="redmi 34"
print(realme.model)
print(redmi.model)
print(geek.model)
print()


#5 class variable 

'''class method:
    fp="yes"
    def __init__(self):
        self.a="deepanshu kumar"
        self.b=34
    def show(self):
        return self.a,self.b    

    @classmethod
    def is_fp(cls):
        print(cls.fp)

m1=method()
method.is_fp        
r1=m1.show()
print(r1)'''


#class method 

'''class add:
    a=3
    b=5
    def __init__(self):
        self.x=34
        self.y=65

    @classmethod
    def show(cls):
        return cls.a+cls.b,cls.a*cls.b,cls.a-cls.b

a1=add()
print(a1.show())            '''


'''class mobile:
    fp="yes"
    def __init__(self):
        self.a="Deepanshu"
        self.b=23
    def show(self):
        print(self.model)

    @classmethod
    def is_fp(cls):
        print(cls.fp)

m1=mobile()
mobile.is_fp()            '''


#4



