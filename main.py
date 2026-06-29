from Inventory_manager import *

while True:
    print("\n==== E-COMMERCE INVENTORY MANAGER ====")
    print("1. Add Item")
    print("2. View Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

    choice = input("select from option (1 - 5): ")

    if choice == "1":
        inventory.add_item()

    elif choice == "2":
        inventory.view_item()

    elif choice == "3":
        inventory.update_item()

    elif choice == "4":
        inventory.delete_item()

    elif choice == "5":
        print("thank you for your time!")
        break

    else:
        print("Invalid choice. try again")