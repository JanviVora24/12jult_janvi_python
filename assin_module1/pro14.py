#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

a=input("Enter String:")
b=input("Enter String:")

#print("Before Swap:",a,b)

x=b[:2]+a[2:]
y=a[:2]+b[2:]

print("After Swap:",x,y)