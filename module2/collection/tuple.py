data=('iOS','Android','Python','JAVA','Ruby')
'''print(data)
print(data[0])
print(data[-1])
print(data[0:3])
print(data[2:])
print(data[:3])
print(len(data))
if 'python' in data:
    print("Yes..")
else:
    print("No..")'''




'''print(data)

print(data.index('JAVA'))
for i in data:
    print(i)
    print(f"Index[{data.index(i)}] = {i}")'''

#del data
#print(data)





#--------------------------------------------------#
#tuple_userinput
data=[]

n=int(input("Enter number of elements:")) #n=5

for i in range(n):
    x=input("Enter an elements:")
    data.append(x)

print(tuple(data))


