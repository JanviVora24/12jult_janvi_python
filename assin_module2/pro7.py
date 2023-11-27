#Write a Python program to convert a list of characters into a string. 

def string(list):
    # Use the join() method to concatenate the characters in the list
    string = ''.join(list)
    return string


characters = ['H', 'e', 'l', 'l', 'o']
result = string(characters)
print(result)