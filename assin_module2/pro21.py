#Write a Python program to find the repeated items of a tuple. 

tuple=(1,2,3,4,5)
print(tuple)
for i in tuple:
    if tuple.count(i)>1:
        print(i)