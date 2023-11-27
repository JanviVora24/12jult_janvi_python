#Write a Python program to remove an empty tuple(s) from a list of tuples.

def remove(tuple):
    for i in tuple:
        if (len(i)==0):
            tuple.remove(i)
    return tuple

tuple=[(1,2),(),(3,4),()]
print(remove(tuple))