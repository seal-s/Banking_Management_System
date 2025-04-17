#Profile Management: User can update his details like contact information
import os
import pickle

def Edit_Contact(accno):    
    f = open("Customer.dat","rb")
    f1 = open("Temp.dat","wb")    
    flag = 0
    try:        
        while True:    
            data=pickle.load(f)        
            if accno in data:
                print("\nThe Account details are found and it is:\n",data)
                flag=1
                print('''Choice List:-
                 A. To edit Address
                 B. To edit Phone Number
                 C. To edit Email ID
                 D. To edit Password
                    ''')
                choice = input(" Enter a choice =")
                if choice == "A" :
                    new_addr = input("Enter new address=")
                    data[4]= str(new_addr)
                    pickle.dump(data,f1)
                elif choice == "B" :                
                    new_mob = input("Enter new phone number=")
                    data[5]= str(new_mob)
                    pickle.dump(data,f1)
                elif choice == "C" :
                    new_email = input("Enter new email id=")
                    data[6]= str(new_email)
                    pickle.dump(data,f1)
                elif choice == "D" :
                    new_pwd = input("Enter new password=")
                    data[2]= str(new_pwd)
                    pickle.dump(data,f1)
                else :
                    print("Invalid choice!!!")
                    pickle.dump(data,f1)
            else:
                pickle.dump(data,f1)
    except:
        print("EOF reached...")
        f.close()
        f1.close()
        os.remove("Customer.dat")
        os.rename("Temp.dat", "Customer.dat")
    if flag == 0:
        print("\nRecord not found!")
    else:
        print("\nRecord Edited Successfully...")    
    return