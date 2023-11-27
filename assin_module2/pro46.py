#Write a Python program to calculate surface volume and area of a cylinder 

pi=3.14
h=float(input("Enter height of cylinder:"))
r=float(input("Enter radiant of cylinder"))

v=pi*r*r*h
area=((2*pi*r)*h)+((pi*r**2)*2)

print("volume",v)
print("surface",area)