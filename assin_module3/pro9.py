#Write a Python program to count the frequency of words in a file. 

'''f=open("first.txt","w")
f.write("Hello word")'''

f=open("first.txt","r")
x=f.read()

a=0
for i in x.split():
    a+=1
print(a)