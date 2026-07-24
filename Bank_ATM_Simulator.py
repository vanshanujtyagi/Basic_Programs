print("                        TYAGIBANK ATM")
ini = 0

while True:
    print("Welcome, User choices :")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    ch = int(input("Select your choice : "))

    if ch == 1:
        print("Existing Balance is ₹", ini)

    elif ch == 2:
        depo = int(input("Enter the Amount : "))
        ini = ini + depo
        print("Amount Deposited successfully.")

    elif ch == 3:
        withr = int(input("Enter the Amount : "))
        ini = ini - withr
        print("Amount Withdrawn successfully.")

    elif ch == 4:
        print("Thank You for Visiting!")
        break

    else:
        print("Invalid choice, please refer to the above choices.")