myset={'A','B','C','D'}
#print(myset)

#print(len(myset))

'''if 'B' in myset:
    print("yes..")
else:
    print("no...")'''

'''for i in myset:
    print(i)'''



'''print(myset)
#myset.add('G')
#myset.update(['H','I','J','A','B'])
#myset.pop()
#myset.remove('B')
#myset.clear()
print(myset)'''

'''print(myset)
#myset.remove('A')
#myset.discard('A')
print(myset)'''

newset={'P','Q','R','S','A','C'}
print(newset)
x=myset.union(newset)
x=myset.intersection(newset)
print(x)



#----------------------------------------------------------------------------------#
#set_userinput

myset=set()

n=int(input("Enter number of elements:"))

for i in range(n):
    x=input("Enter an element:")
    myset.add(x)

print(myset)

