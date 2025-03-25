#class 12 project

import pickle
bal=0

def createacc():
    f=open("bank.dat","ab")
    L=[]
    accno=int(input("Enter accno:"))
    name=input("Enter name:")
    atype=input("Enter account type[C/S]:")
    phoneno=int(input("Enter phoneno:"))
    pinno=int(input("Enter pin number:"))
    L=[accno,name,atype,phoneno,pinno]
    pickle.dump(L,f)
    f.close()
    
def deposit():
    global bal
    amt=int(input("Enter amount to be deposited:"))
    bal=bal+amt
    
def withdraw():
    global bal
    amt=int(input("Enter amount to be withdrawn:"))
    if bal>=amt:
        bal=bal-amt
    else:
        print("LOW BALANCE")

def showacc():
    f=open("bank.dat","rb")
    p=int(input("Enter pin number:"))
    try:
        while True:
            A=pickle.load(f)
            if p==A[4]:
                print("Account holder's account number:",A[0])
                print("Account holder's name:",A[1])
                print("Account holder's account type:",A[2])
                print("Account holder's phone number:",A[3])
    except:
       f.close()

print("BANK MANAGEMENT SYSTEM")
print("MAIN MENU")
while True:
    print('''1: NEW ACCOUNT
2: DEPOSIT AMOUNT
3:WITHDRAW AMOUNT
4:BALANCE ENQUIRY
5:ACCOUNT HOLDER LIST
6:EXIT''')
    ch=int(input("ENTER CHOICE"))
    if ch==1:
        createacc()
    
    elif ch==2:
        deposit()
        
    elif ch==3:
        withdraw()
        
    elif ch==4:
        print("Your bank balance is",bal)
        
    elif ch==5:
        showacc()
        
    else:
        break



OUTPUT:
BANK MANAGEMENT SYSTEM
MAIN MENU
1: NEW ACCOUNT
2: DEPOSIT AMOUNT
3:WITHDRAW AMOUNT
4:BALANCE ENQUIRY
5:ACCOUNT HOLDER LIST
6:EXIT
ENTER CHOICE:1
Enter accno:1001
Enter name:Monu
Enter account type[C/S]:S
Enter phoneno:1234567890
Enter pin number:5555
1: NEW ACCOUNT
2: DEPOSIT AMOUNT
3:WITHDRAW AMOUNT
4:BALANCE ENQUIRY
5:ACCOUNT HOLDER LIST
6:EXIT
ENTER CHOICE:2
Enter amount to be deposited:5000
1: NEW ACCOUNT
2: DEPOSIT AMOUNT
3:WITHDRAW AMOUNT
4:BALANCE ENQUIRY
5:ACCOUNT HOLDER LIST
6:EXIT
ENTER CHOICE:3
Enter amount to be withdrawn:2000
1: NEW ACCOUNT
2: DEPOSIT AMOUNT
3:WITHDRAW AMOUNT
4:BALANCE ENQUIRY
5:ACCOUNT HOLDER LIST
6:EXIT
ENTER CHOICE:4
Your bank balance is 3000
1: NEW ACCOUNT
2: DEPOSIT AMOUNT
3:WITHDRAW AMOUNT
4:BALANCE ENQUIRY
5:ACCOUNT HOLDER LIST
6:EXIT
ENTER CHOICE:5
Enter pin number:555
1: NEW ACCOUNT
2: DEPOSIT AMOUNT
3:WITHDRAW AMOUNT
4:BALANCE ENQUIRY
5:ACCOUNT HOLDER LIST
6:EXIT
ENTER CHOICE:6

