#Write a Python program to read last n lines of a file. 

f=open("one.txt","r")
x=int(input("Enter Number:"))
print(f.readlines()[x:-1])