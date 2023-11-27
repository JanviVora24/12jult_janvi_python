#Write a Python program to count the number of lines in a text file. 

f=open("one.txt","r")
a=f.readlines()

x=0
for i in a:
    x+=1
print(x)
