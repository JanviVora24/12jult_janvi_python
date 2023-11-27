fnm=input("Enter Firstname:")
lnm=input("Enter Lastname:")


if fnm.isupper() and lnm.isupper():

    email=input("Enter an email:")
    mobile=input("Enter a mobile number:")
    if email.islower()  and len(mobile)==0:

        length=len(mobile)
        if  len(mobile)==10:

            if email.islower() and mobile.isdigit():
                print("Firsname:",fnm)
                print("Lastname:",lnm)
                print("Email:",email)
                print("Mobile:",mobile)
        else:
            print("Error! Plz input valid email address or mobile")
    password=input("enter your password")
    cpassword=input("enter your confrom password")
    if password==cpassword:
        print("password is",password)
    else:
        print("don't match")


else:
    print("Error!Plz input proper details!")
