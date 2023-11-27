#Write a Python program to map two lists into a dictionary 

values=['janvi','vrutika']
keys=[1,2]
print(str(values))
print(str(keys))

dict={}
for key in keys:
    for value in values:
        dict[key]=value
        values.remove(value)
print(str(dict))

name=["ishita","riddhi","gopi"]
id=[3,2,1]

mapped=zip(name,id)
print(dict(mapped))