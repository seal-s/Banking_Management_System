#Profile Management: User can update his details like contact information
import os
import pickle
import datetime

def menu():    
    print("\n\n\t\t-------------")
    print("\t\t~:MAIN MENU:~")
    print("\t\t-------------")
    print("\n\tPress 1 for show all transaction details.")
    print("\tPress 2 to check transaction details of a date.")
    print("\tPress 3 to check transaction details between date range.")
    print("\tPress 4 to Back to Bank Main Menu.")
    c=int(input("\nEnter your choice="))
    return c

def diff_reports(accno):
    while True:
        ch=menu()
        if ch==1:        
            all_transaction_info(accno)
        elif ch==2:
            d=input("Enter the date as [YYYY-MM-DD]=")
            datewise_transaction(accno,d)
        elif ch==3:
            d1=input("Enter the start date as [YYYY-MM-DD]=")
            d2=input("Enter the end date as [YYYY-MM-DD]=")
            date_rangewise_transaction(accno,d1,d2)
        elif ch==4:
            print("\nBye...")
            break

def all_transaction_info(accno):
    f1=open("Transaction.dat","rb")
    try:
        while True:
            data=pickle.load(f1)
            if(accno in data):
                print(data)
    except:
        print("\n\n*****")
        f1.close()


def datewise_transaction(accno,d):
    f1=open("Transaction.dat","rb")
    try:
        while True:
            data=pickle.load(f1)
            if(accno in data[0] and d in data[5]):
                print(data)
    except:
        print("\n\n*****")
        f1.close()


def date_rangewise_transaction(accno,d1,d2):
    f1=open("Transaction.dat","rb")
    try:
        while True:
            data=pickle.load(f1)
            if(accno in data[0]):
                dt1=data[5]
                if(dt1[0:10]>=d1 and dt1[0:10]<=d2):
                    print(data)
    except:
        print("\n\n*****")
        f1.close()
    
