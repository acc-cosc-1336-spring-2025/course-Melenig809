from dictionary import add_inventory, remove_inventory_widget

def main():
    inventory = {}

    while True:
        print("\nInventory Menu")
        print("1 - Add or Update Item")
        print("2 - Delete Item")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the item name: ")
            try:
                quantity = int(input("Enter the quantity: "))
                add_inventory(inventory, name, quantity)
                print(f"Updated inventory: {inventory}")
            except ValueError:
                print("Invalid quantity. Please enter a number.")

        elif choice == "2":
            name = input("Enter the item name to delete: ")
            result = remove_inventory_widget(inventory, name)
            print(result)

        elif choice == "3":
            print("Exiting Inventory Program.")
            break

        else:
            print("Invalid choice. Please select from the menu options.")

if __name__ == "__main__":
    main()
