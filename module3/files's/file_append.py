f1=open('newfile.txt','a')

'''f1.write(id)
f1.write(name)'''

n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter an ID:")
    name=input("Enter a Name:")

    f1.write(f"ID:{id}\nName:{name}\n")