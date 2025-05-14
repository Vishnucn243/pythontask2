def fun():
    balance=1000
    while True:
        print(f"\nBalance: ${balance}")
        print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice=input("Enter choice : ")
        if choice=='1':
            amount=float(input("Enter deposit amount: "))
            if amount>0:
                balance+=amount
                print("successful")
            else:
                print("Invalid amount")
        elif choice=='2':
            amount=float(input("Enter withdrawal amount: "))
            if 0<amount<=balance:
                balance-=amount
                print("success")
            else:
                print("invalid")
        elif choice=='3':
            print(f"Current balance: ${balance}")
        elif choice == '4':
            print("thank you for using ATM")
            break
        else:
            print("invalid")
if __name__ == "__main__":
    fun()