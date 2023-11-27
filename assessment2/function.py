import pymysql
import re
from datetime import datetime

con=pymysql.connect(host='localhost',user='root',password='',database='pharmacymanagement')
print("connect")


#Ceate Table Pharmacy
create="create table pharmacy(no integer auto_increment primary key, Medicinename text, Qty int, Date date, Addedby int, Price int)"
try:
    cr=con.cursor()
    cr.execute(create)
    print("Table Created..")
except Exception as e:
    print(e)

#Add Medicine
class medicine:
    Medicinename=""
    Qty=""
    Date=""
    Addedby=""
    Price=""

    def tabalate(self):
        self.Medicinename=input("Enter Medicine Name:")
        self.Qty=input("Enter Qty:")

        self.Date=input("Enter a date in YYYY-MM-DD format:")
        pattern = r"\d{4}-\d{2}-\d{2}"

        self.Date1=re.match(pattern,self.Date)
        self.Addedby=input("Added By:")
        self.Price=input("Enter Price:")
        insert= f"insert into pharmacy(Medicinename,Qty,Date,Addedby,Price)values('{self.Medicinename}','{self.Qty}','{self.Date}','{self.Addedby}','{self.Price}')"
        try:
            cr.execute(insert)
            con.commit()
            print("Medicine Add...")
        except Exception as e:
            print(e)
add=medicine()
#add.tabalte()

#View Medicine
class viewmedicine:
    def view(self):
        select="select * from pharmacy"
        cr=con.cursor()
        cr.execute(select)
        a=cr.fetchall()
        for i in a:
            print(i)
v=viewmedicine()
#v.view()

#Delete Medicine
class delete:
    def deletemedicine(self):
        n=input("Do You Want to Delete Medicine:")
        delete=f"delete from pharmacy where no={n}"
        try:
            cr.execute(delete)
            con.commit()
            print("Medicine Delete...")
        except Exception as e:
            print(e)
d=delete()
#d.deletemedicine
        
#Create Table Manager
create="create table Manager(no integer auto_increment primery key, Managername text, Pharmacyname text)"
try:
    cr=con.cursor()
    cr.execute(create)
    print("Table Created..")
except Exception as e:
    print(e)

class manager:
    def phmanager(self):
        self.Managername=input("Enter Manager Name:")
        self.Pharmacyname=input("Enter Pharmacy Name:")
        insert=f"inset into Manager(Managername,Pharmacyname)values('{self.Managername}','{self.Pharmacyname}')"
        try:
            cr.execute(insert)
            con.commit()
            print("Manager Add...")
        except Exception as e:
            print(e)
p=manager()
#p.phmanager()

#View manager
class viewmanager:
    def view1(self):
        select="select * from Manager"
        cr=con.cursor()
        cr.execute(select)
        a=cr.fetchall()
        for i in a:
            print(i)
v1=viewmanager()
#v1.view1()

#Register Table
create="create table Register(no integer auto_increment primary key, Firstname text, Lastname text, Username text, Emailid text, Password integer)"
try:
    cr=con.cursor()
    cr.execute(create)
    print("Table Created..")
except Exception as e:
    print(e)

#Register
class Register:
    Firstname=""
    Lastname=""
    Username=""
    Emailid=""
    Password=""
    def registration(self):
        self.Firstname=input("Enter your FirstName:")
        self.Lastname=input("Enter your LastName:")
        self.Username=input("Enter your UserName:")
        self.Emailid=input("Enter your Emailid:")
        self.Password=input("Enter your Password:")
        insert= f"insert into Register(Firstname,Lastname,Username,Emailid,Password)values('{self.Firstname}','{self.Lastname}','{self.Username}','{self.Emailid}','{self.Password}')"
        cr.execute(insert)
        con.commit()
        print("Register Sucessfully...")
r=Register()
#r.registration()

#login
class login:
    def loging(self):
        Username=input("Enter your UserName:")
        Password=input("Enter your Password:")
        select=f"select * from Register where Username='{Username}' and Password='{Password}'  "
        cr=con.cursor()
        cr.execute(select)
        a=cr.fetchone()
        if a is not None :
            print("Login Successfully...")
        else:
            print("Invalid Username and Password..")
            l.loging()
l=login()
#l.loging()

#Admin
class Admin:
    def admin(self):
        print("Admin:")
        print("\t Can Register:")
        print("\t Can Login:")
        print("\t Can View all manger:")
        print("\t Can View all medicine:")
        n=input("Enter yuor Choice:")
        if n=='1':
            r.registration()
        elif n=='2':
            l.loging()
        elif n=='3':
            print("Login After View all Manager..")
            l.loging()
            print("View all Manager..")
            v1.view1()
        elif n=='4':
            print("Login After View all Medicine..")
            l.loging()
            print("View all Medicine..")
            v.view()
        else:
            exit
A=Admin()


#Pharmarcy Manager
class PharmarcyManager:
    def manager(self):
        print("Pharmarcy Manager:")
        print("\t Can Register:")
        print("\t Can Login:")
        print("\t Can Add Medicine:")
        print("\t Can View Medicine:")
        print("\t Can Delete Medicine:")
        n=input("Enter your Choice:")
        if n=='1':
            r.registration()
        elif n=='2':
            l.loging()
        elif n=='3':
            print("Login After Add Medicine..")
            l.loging()
            print("Add Medicine..")
            add.tabalate()
        elif n=='4':
            print("Login After View all Medicine..")
            l.loging()
            print("View all Medicine..")
            v.view()
        elif n=='5':
            print("Login After Delete Medicine..")
            l.loging()
            print("Delete Medicine..")
            d.deletemedicine()
        else:
            exit
P=PharmarcyManager()







    


    


