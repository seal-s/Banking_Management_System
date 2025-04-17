#Banking Management System

import Registration
import SystemLogin

def Main_menu():
    print("\n\t\t------------------")
    print("\t\t~:BANKING SYSTEM:~")
    print("\t\t------------------")
    print("\n  Press 1 for Register User.")
    print("  Press 2 for System Login.")    
    print("  Press 3 for Exit.")
    ch=int(input("\n  Enter your choice="))
    return ch

#System Run start from the following
while True:
    ch=Main_menu()
    if ch==1:
        Registration.CreateAccount()
    elif ch==2:        
        SystemLogin.login()   
    elif ch==3:
        print("\nBye...")
        break
    else:
        print("\nInvalid choice! Try Again...")
