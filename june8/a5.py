age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()

if age < 18 or age > 50:
    print("Not eligible for employment")

elif gender == "M":
    if age < 25:
        print("Customer Care Department")
    elif age < 45:
        print("Engineering Department")
    else:
        print("Security Department")

elif gender == "F":
    if age < 31:
        print("Customer Care Department")
    else:
        print("Admin Department")

else:
    print("Invalid input")