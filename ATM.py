pin={'Hridoy':2344,'Abhigyan':1922,'Abhinab':2488}
account=[50000]
def bank_user(a,account,pin,name):
    if a=="Deposit":
        dep=int(input("Enter amount: "))
        account=account[0]+dep
        print(f"Rs{dep} added to your account")
        print(f"{account} is your current account balance")
    elif a=="Withdraw":
        wit=int(input("Enter amount"))
        account=account[0]-wit
        print(f"Rs{wit} taken out from your account")
        print(f"{account} is your current account balance")
        if account<0:
            print(f"Your account is in the debt of Rs{account}")
    elif a=="View" or "see":
         print(account)
    elif a=='Exit':
        breakpoint
    elif a=="Share":
        acc=input("Enter the person account name: ").capitalize()
        name=input("Enter your name: ")
        mypin=int(input("Enter your pin: "))
        x=pin.get(name)
        if mypin==x:
                pin.get(name)
                amount=int(input("Enter amount: "))
                account=account[0]-amount
                print(f"Rs{amount} sent to {acc}")
                if account<0:
                        print(f"Your account is in the debt of Rs{account}")
                else:
                     print(f"Your account have Rs{account} left.")
    else:
                    print('Give Valid Indentity')
name=input("Enter your name:").capitalize()
if name in pin:
    verification=int(input("Enter your pin: "))    
    veri=pin.get(name)
    if veri==verification:
            ask=input("What you want to do:\n'Deposit'\n'Withdraw'\n'See'\n'Share' \n: ").capitalize()
            bank_user(ask,account,pin,name)
    else:
        print("Give proper details")
print("Ok bye!!")
