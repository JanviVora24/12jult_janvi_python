#write a python program to find the longest words. 

f=open("first.txt","r")
a=f.read()
print(a)
a=a.split()

b=sorted(a,key=len)
print("Longest Words:",b[-1])
