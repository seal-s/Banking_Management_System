#Core Operations
import pickle
import os
import datetime

def deposit(accno,money):
    f=open("Customer.dat","rb")
    f1=open("Temp.dat","wb")
    try:
        while True:
            data=pickle.load(f)
            if(accno in data):
                data[7]=str(int(data[7])+money)
                print("\nAfter deposit balance amount is: Rs. "+data[7])
                print("Amount Deposited Successfully...")
                pickle.dump(data,f1)

                #Save the transaction details to Transaction.dat
                d = datetime.datetime.now()
                dt = d.strftime("%Y-%m-%d %H:%M:%S")    
                valuelist=[accno, data[3], "Deposit", money, data[7], dt]    
                f2=open("Transaction.dat", "ab")
                pickle.dump(valuelist,f2)
                f2.close()
            else:
                pickle.dump(data,f1)
    except:
        print("\n...---...---...---...")
        f.close()
        f1.close()
        os.remove("Customer.dat")
        os.rename("Temp.dat", "Customer.dat")

def withdrawn(accno,money):
    f=open("Customer.dat","rb")
    f1=open("Temp.dat","wb")
    try:
        while True:
            data=pickle.load(f)
            if(accno in data):
                if(int(data[7])-money > 0):
                    data[7]=str(int(data[7])-money)
                    print("\nAfter withdrawn balance amount is: Rs. "+data[7])
                    print("Withdrawn Successful...")
                    pickle.dump(data,f1)

                    #Save the transaction details to Transaction.dat
                    d = datetime.datetime.now()
                    dt = d.strftime("%Y-%m-%d %H:%M:%S")    
                    valuelist=[accno, data[3], "Withdrawn", money, data[7], dt]    
                    f2=open("Transaction.dat", "ab")
                    pickle.dump(valuelist,f2)
                    f2.close()
                else:
                    print("\nInsufficient balance in account. Transaction is failed!!!")
                    pickle.dump(data,f1)
            else:
                pickle.dump(data,f1)
    except:
        print("\n...---...---...---...")
        f.close()
        f1.close()
        os.remove("Customer.dat")
        os.rename("Temp.dat", "Customer.dat")
        
def balanceInfo(accno):
    f=open("Customer.dat","rb")
    try:
        while True:
            data=pickle.load(f)            
            if(accno in data):
                print("\nBalance Amount is: Rs. "+str(data[7]))
    except:
        print("\n...---...---...---...")
        f.close()
        
def menu():
    print("\n\nWelcome to Banking System Core Operation")
    print("\n\t\t-------------")
    print("\t\t~:MAIN MENU:~")
    print("\t\t-------------")
    print("\n\tPress 1 for Balance Enquery.")
    print("\tPress 2 to Deposit Amount.")
    print("\tPress 3 to Withdraw Amount.")
    print("\tPress 4 to Back to Bank Main Menu.")
    c=int(input("\nEnter your choice="))
    return c

def operations(accno):
    while True:
        ch=menu()
        if ch==1:        
            balanceInfo(accno)
        elif ch==2:
            money=int(input("Enter the amount to deposit="))
            deposit(accno,money)
        elif ch==3:
            money=int(input("Enter the amount to withdraw="))
            withdrawn(accno,money)
        elif ch==4:
            print("\nBye...")
            break
