import trade

CMDS = {"back", "b", "menu", "m"}


class back(Exception):
    pass


def backish(value):
    if value.lower() in CMDS:
        raise back


def menu():
    print("\nWelcome to Orbit Trading!")
    print("1. View Market")
    print("2. Buy Asset")
    print("3. Sell Asset")
    print("4. View Portfolio")
    print("5. Transaction History")
    print("6. Exit")


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


def qtyval(prompt):
    while True:
        value = input(prompt).strip()
        backish(value)

        if not value.isdigit():
            print("Enter numbers only")
            continue

        quantity = int(value)

        if quantity <= 0:
            print("Quantity must be positive")
            continue

        return quantity


def buyval():
    asset = textval("Enter asset to buy (back for menu): ")
    quantity = qtyval("Enter quantity to buy (back for menu): ")
    print(trade.buy(asset, quantity))


def sellval():
    asset = textval("Enter asset to sell (back for menu): ")
    quantity = qtyval("Enter quantity to sell (back for menu): ")
    print(trade.sell(asset, quantity))


while True:
    menu()

    try:
        choice = menchoice("Enter your choice: ", 1, 6)

        if choice == 1:
            print(trade.viewmarket())

        elif choice == 2:
            buyval()

        elif choice == 3:
            sellval()

        elif choice == 4:
            print(trade.viewportfolio())

        elif choice == 5:
            print(trade.transhistory())

        elif choice == 6:
            print("Thank you for using Orbit Trading!")
            break

    except back:
        continue

    except Exception as e:
        print("Unexpected error:", e)
