class InventoryManager:
    def __init__(self):
        self.items = []
        self.next_id = 1

    def add_item(self):
        name = input("Enter the name of item: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        generated_id = f"ecom{self.next_id:03d}"


        item = {
            "id": generated_id,
            "name": name,
            "quantity": quantity,
            "price": price
        }

        self.items.append(item)
        print("Item added successfully!")
        self.next_id += 1

    def view_item(self):
        if not self.items:
            print("Inventory is empty!")
        else:
            print("\n=== Inventory items ===")
            for item in self.items:
                print(
                    f"ID: {item['id']},"
                    f"Name: {item['name']},"
                    f"Quantity: {item['quantity']},"
                    f"Price: #{item['price']}"
                )

    def update_item(self):
        item_id = input("Enter item to update: ")

        for item in self.items:
            if item["id"] == item_id:
                item["name"] = input("Enter new name: ")
                item["quantity"] = int(input("Enter new quantity: "))
                item["price"] = float(input("Enter new price: "))
                print("item updated successfully!")
                return
            
        print("item not found!")


    def delete_item(self):
        item_id = input("Enter item id to delete: ")

        for item in self.items:
            if item["id"] == item_id:
                self.items.remove(item)
                print("Item deleted successfully!")
                return

        print("Item not found!")

inventory = InventoryManager()

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