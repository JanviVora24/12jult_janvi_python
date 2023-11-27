#Write a Python program to find the second smallest number in a list. 

list= [] 
n = int(input("Enter the number of elements: "))
for i in range(1, n+1): 
    a = int(input("Enter the elements: ")) 
    list.append(a) 
#li.sort() 
print("The second smallest value of this list: ",list[1])
