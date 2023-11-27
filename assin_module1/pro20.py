#Write a Python function to insert a string in the middle of a string

n=input("Enter String:")
print(n)
mid_str="new"
temp=n.split()
mid_pos=len(temp)//2
res=(temp[:mid_pos]+[mid_str]+temp[mid_pos:])
print(' '.join(res))