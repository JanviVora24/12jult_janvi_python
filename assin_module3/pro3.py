#Write a Python program to read first n lines of a file.

f=open("one.txt","r")
n=int(input("Enter number:"))
print(f.readlines()[0:n]) 
