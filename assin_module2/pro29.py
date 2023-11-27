#Write a Python program to check multiple keys exists in a dictionary 

def check(dict,keys):
    return all(key in dict for key in keys)
dict={'name':'janvi','sub':'python','city':'rajkot'}
keys=['name','sub','city']

if  check(dict,keys):
    print("exists..")
else:
    print("not exists..")
