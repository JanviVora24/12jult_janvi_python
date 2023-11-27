#Write a Python program to find the highest 3 values in a dictionary 

dictionary={'a':10,'b':20,'c':30,'d':40,'e':50}
a=dict(sorted(dictionary.items(),key=lambda x: x[1],reverse=True))
print(a)
