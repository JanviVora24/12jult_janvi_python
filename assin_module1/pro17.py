#Write a Python function that takes a list of words and returns the length of the longest one

n=input("Enter String:")
longest=0
for length in n.split():
    if len(length)>longest:
        longest=len(length)
        longest_length=length
print("longest word is:",longest_length)
print("Length is:",len(longest_length))