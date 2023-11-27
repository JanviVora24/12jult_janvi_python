#Write a Python program to write a list to a file. 

list=[1,2,3,4,5]

f=open("list.txt","w")
f.write(f"{list}")
print("Sucessfully...")