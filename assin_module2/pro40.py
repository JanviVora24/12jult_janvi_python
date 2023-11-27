#Write a Python function to check whether a number is perfect or not. 

number=int(input("Enter Number:"))
sum=0
for i in range(1,number):
    if  number%i==0:
        sum=sum+i
if sum==number:
    print("Number is perfect..")
else:
    print("Number is not perfect...")

while True:
    a=int(input("Enter number:"))
    if 0 <= a <= 100:
        print("yes")
        break
    print("no")
    print('plz try')
