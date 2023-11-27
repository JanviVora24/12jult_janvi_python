#Write a Python program to read a file line by line and store it into a list

list=[]
f=open("one.txt","r")
list=f.readlines()
print(type(list),list)