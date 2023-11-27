'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:{'3': 1's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} '''

dict1={'a':10,'b':20,'c':30}
dict2={'a':50,'b':20,'d':10}
dict={}

for key,value in dict1.items():
    dict[key]=value

for key,value in dict2.items():
    if key in dict:
        dict[key]+=value
    else:
        dict[key]=value

print("Dictionary:",dict)