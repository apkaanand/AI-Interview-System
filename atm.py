balance = 8880
pin = int(input('Enter your ATM pin: '))
if pin == 192007:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        Choice = int(input('Enter Your choice: '))
        if Choice == 1:
            print('Your Balance is Rs.', balance)
        elif Choice == 2:
            amt = int(input("Enter amount to deposit: "))
            balance += amt
            print("Amount deposited successfully. \nNew balance is Rs.", balance)
        elif Choice == 3:
            amt = int(input("Enter amount to withdraw: "))
            if amt <= balance:
                balance -= amt
                print("Please collect your cash. \nRemaining balance is Rs.", balance)
            else:
                print("Insufficient balance.")
        elif Choice == 4:
            print('Thank You for Using Atm')
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print('Wrong Pin')
