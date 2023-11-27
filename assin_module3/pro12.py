#Write python program that user to enter only odd numbers, else will raise an exception. 

try:
    x=int(input("Enter Number:"))
    
    if x%2==0:
        raise ValueError
    print(x)

except ValueError:
    print("Enter odd Number:")