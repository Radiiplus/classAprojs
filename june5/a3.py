import time

list1 = []
list2 = []

print("Enter items for list1")
while True:
    item = input("Enter an item: ")
    list1.append(item)

    done = input("Are you through? (yes/no): ").lower()
    if done == "yes":
        break

print("\nEnter items for list2")
while True:
    item = input("Enter an item: ")
    list2.append(item)

    done = input("Are you through? (yes/no): ").lower()
    if done == "yes":
        break

if len(list1) != len(list2):
    print("length of lists don't match")
else:
    print("lengths match. Proceeding")
    
    for i in range(3):
        print(".")
        time.sleep(1)

    result = dict(zip(list1, list2))
    print(result)