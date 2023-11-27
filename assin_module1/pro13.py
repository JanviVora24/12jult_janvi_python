#Write a Python program to count the occurrences of each word in a given sentence


n=input("Enter String:")
a=n.split()
b={}
for i in a:
    if i in b:
        b[i] +=1
    else:
        b[i]=1
for i,count in b.items():
    print(f"{i}:{count}")
    