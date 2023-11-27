import random


def studata(name,sub,city):
    x=random.random()
    print("ID:",x)
    print("Name:",name.upper)
    print("Subject:",sub)
    print("City:",city)

studata('janvi','python','rajkot')

l=[]
n=int(input("Enter student info:"))

def staffdata():
    for i in range(n):
        x=random.random()
        name=input("Enter Name:")
        sub=input("Enter Subject:")
        city=input("Enter City:")
        '''l1=[name,sub,city]
        l.append(l1)'''

        print("ID:",x)
        print("Name:",name)
        print("Subject:",sub)
        print("City:",city)
for i in l:
        staffdata()
    
print(i)

