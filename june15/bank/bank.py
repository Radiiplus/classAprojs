import acc

CMDS = {"back", "b", "menu", "m"}


class back(Exception):
    pass


def backish(value):
    if value.lower() in CMDS:
        raise back


def menu():
    print("\nWelcome to Orbit Bank!")
    print("1. Create Account")
    print("2. Login")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Check Balance")
    print("7. View Transaction History")
    print("8. Logout")
    print("9. Exit")

def menchoice(prompt, min_val, max_val):
    while True:
        choice = input(prompt)

        if not choice.isdigit():
            print("Enter numbers only")
            continue

        choice = int(choice)

        if choice < min_val or choice > max_val:
            print("Invalid choice range")
            continue

        return choice


def textval(prompt):
    while True:
        text = input(prompt).strip()
        backish(text)

        if not text:
            print("Input cannot be empty")
            continue

        return text


def amountval(prompt):
    while True:
        try:
            value = input(prompt).strip()
            backish(value)

            amount = float(value)

            if amount <= 0:
                print("Amount must be positive")
                continue

            return amount

        except ValueError:
            print("Enter a valid number")


def createval():
    while True:
        username = textval("Enter username (back for menu): ")

        if acc.userexist(username):
            print("Username already exists")
            continue

        password = textval("Enter password (back for menu): ")

        result = acc.toughpass(password)

        if result != "Password is strong":
            print(result)
            continue 

        print(acc.create(username, password))
        return True

def loginval():
    while True:
        username = textval("Enter username (back for menu): ")
        password = textval("Enter password (back for menu): ")

        result = acc.auth(username, password)
        print(result)

        if "successful" in result.lower():
            return True

while True:
    menu()

    try:
        choice = menchoice("Enter your choice: ", 1, 9)

        if choice == 1:
            createval()

        elif choice == 2:
            loginval()

        elif choice == 3:
            amount = amountval("Enter amount to deposit (back for menu): ")
            print(acc.deposit(amount))

        elif choice == 4:
            amount = amountval("Enter amount to withdraw (back for menu): ")
            print(acc.withdraw(amount))

        elif choice == 5:
            receiver = textval("Enter receiver's account ID or username (back for menu): ")
            amount = amountval("Enter amount to transfer (back for menu): ")
            print(acc.transfer(receiver, amount))

        elif choice == 6:
            print(acc.balance())

        elif choice == 7:
            print(acc.history())

        elif choice == 8:
            print(acc.logout())

        elif choice == 9:
            print("Thank you for banking with us!")
            break

    except back:
        continue

    except Exception as e:
        print("Unexpected error:", e)
