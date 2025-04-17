#System Login
import pickle
import CoreOperations
import ProfileManagement
import Reports

def login():
    print("\n\t\t-:BANKING MANAGEMENT SYSTEM:-\n")
    f=open("Customer.dat","rb")
    flag=0
    accno=input("Enter Account Number=")
    pwd=input("Enter Password=")
    try:
        while True:            
            cdata=pickle.load(f)            
            if (accno in cdata) and (pwd in cdata):                
                flag=1
                print("\nWelcome "+cdata[3]+" to Banking System...")
                f.close()

                while True:
                    ch=menus()
                    if ch==1:
                        #Call Main Menu of core operations
                        CoreOperations.operations(accno)
                    elif ch==2:
                        #Call Edit_Contact() of ProfileManagement
                        ProfileManagement.Edit_Contact(accno)
                    elif ch==3:
                        #Call Main Menu of Reports
                        Reports.diff_reports(accno)
                    elif ch==4:
                        print("\n\t\tYou are Logout Successfully...")
                        System.exit(0)
        
    except:
        print("\n\n...---...---...---...")
        f.close()
    if flag==0:
        print("\nError: Invalid Account Number or Password!!!")

def menus():
    print("\n\t\t------------------")
    print("\t\t~:BANK MAIN MENU:~")
    print("\t\t------------------")
    print("\nPress 1 for Core Operations.")
    print("\nPress 2 for Profile Management.")
    print("\nPress 3 for Reports.")
    print("\nPress 4 for Logout.")
    opt=int(input("\nEnter your choice="))
    return opt
