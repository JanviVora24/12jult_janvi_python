#Write python program that swap two number with temp variable and without temp variable

#without temp variable

'''a=int(input("Enter A:"))
b=int(input("Enter B:"))

a,b=b,a

print("Value of A:",a)
print("Value of B:",b)'''


#with temp variable

a=int(input("Enter A:"))
b=int(input("Enter B:"))

temp=a
a=b
b=temp

print("Value of A:",a)
print("Value of B:",b)
