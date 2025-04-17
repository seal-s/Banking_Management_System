#Registration: A customer can create an account in the bank by providing important information such as personal details.
import pickle
import random
import datetime

def CreateAccount():
    print("\n\t\t-:NEW USER REGISTRATION:-\n")
    acctype=input("\nSelect Account Type [S: Savings / C: Current]=")
    while True:
        accno=str(random.randint(100000,999999))
        check=SearchAccount(accno)
        if check==0:
            print("\nYour Account number is:",accno)
            break
        
    cname=input("Enter Full Name=")
    caddr=input("Enter Address=")
    cphone=input("Enter Phone Number=")
    cemail=input("Enter Email ID=")
    camount=input("Enter Amount to deposit=")
    password=input("Enter Account Password=")
    
    listvalues=[accno, acctype, password, cname, caddr, cphone, cemail, camount]
    #Save the details to the Customer.dat
    f=open("Customer.dat", "ab")
    pickle.dump(listvalues,f)
    f.close()

    #Get system date and time
    d = datetime.datetime.now()
    dt = d.strftime("%Y-%m-%d %H:%M:%S")    
    valuelist=[accno, cname, "A/C Opening", camount, camount, dt]
    #Save the details to the Transactions.dat
    f=open("Transaction.dat", "ab")
    pickle.dump(valuelist,f)
    f.close()
    print("\nRegistration is Successful...\n")

def SearchAccount(accno):
    with open("Customer.dat","rb") as f:
        flag=0        
        try:
            while True:
                cdata=pickle.load(f)
                if (accno in cdata):
                    flag=1
        except:
            print("\nAccount Number is generated successfully...")
    if flag==0:
        return 0
    else:
        return 1

   
