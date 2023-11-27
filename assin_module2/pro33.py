#Write a Python program to print all unique values in a dictionary. 
dict={"a":1, "b":2, "c":1, "d":3}
value=set()
for i in dict.values():
    value.add(i)
print("Unique value is:")

for i in value:
    print(i)

print("Unique number is:",len(value))