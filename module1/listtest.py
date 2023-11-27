l=[]
n=int(input("Enter number of id:"))

for i in range(n):
    list=int(input("Enter id:"))
    name=input("Enter Name:")
    city=input("Enter City:")
    l1=[list,name,city]
    l.append(l1)
for a in l:
    print(a)