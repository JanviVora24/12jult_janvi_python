#Write a Python program to read a random line from a file. 

import random
f=open("a.txt","r")
line=f.readlines()
print(random.choices(line))