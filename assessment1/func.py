
import datetime
x=datetime.datetime.now()

def role():
    print("\tBanker")
    print(" ")
    print("\t1. Add Customer")
    print("\t2 View Customer")
    print("\t3 Search Customer")
    print("\t4 View All Customer")
    print("\t5 Total Amount in Bank")
    print(" ")


def customer():
    d={}
    keys=["acoount no.","name","balance"]
    for i in range(len(keys)):
        v=input (f"Enter {keys[i]}:")
        d[keys[i]]=v
    f1=open("customer.txt","a")
    f1.write(f"customer{d}\n{x}\n")
    

def abc():
    x=input("Do you want to performe more operations:press y for yes and n for no:").lower()
    if x=="y":
        customer()
    else:
        exit()



def view():
    f1=open("customer.txt","r")
    print(f1.read())


'''def open():
    x=input("Do you want to performe more operations:press y for yes and n for no:").lower()
    if x=="y":
        customer()
    else:
        exit()
open()'''





'''def menu():
    print("\tWelcome to customer's App")
    print(" ")
    print("\t1. withdrow Amount")
    print("\t2. deposite Amount")
    print("\t3. view Balance")
    
    c=input("Operation Menu:")
    if c=="1":
        global balance
        balance=int(input("Enter your Balance:"))
        withdrow_amount=int(input("Enter withdrow amount:"))
        if balance < withdrow_amount:
            print("do you not enough money in your account")
        else:
            print("Your balance:",(balance-withdrow_amount))

    elif c=="2":
        balance=int(input("Enter your Balance:"))
        deposite_amount=int(input("Enter deposite amount:"))
        print("Your New balance:",(balance+deposite_amount))
    
    elif c=="3":
        print("view balance:",balance)
menu()'''







