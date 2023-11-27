#Write a Python program to unzip a list of tuples into individual lists. 

list=[(1,2),(3,4),(5,6)]
a,b=zip(*list)

print(a)
print(b)