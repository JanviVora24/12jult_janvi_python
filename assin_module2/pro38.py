#Write a Python function to calculate the factorial of a number (a nonnegative integer) 

a=int(input("Enter number:"))
b=1

for i in range(a,1,-1):
    b=b*i
print(b)