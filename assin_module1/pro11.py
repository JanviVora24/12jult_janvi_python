#write a Python program to count the number of characters (character frequency) in a string

string=input("Enter a String:")
freq={}
for i in string:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("Character frequency")
for key,value in freq.items():
    print(key,":",value)