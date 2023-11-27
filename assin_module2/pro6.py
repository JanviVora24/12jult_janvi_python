#Write a Python function that takes a list and returns a new list with unique elements of the first list. 

def elements(list):
    return list(set(list))


l = [1, 2, 2, 3, 4, 4, 5]
unique_elements = elements(l)
print(unique_elements)
