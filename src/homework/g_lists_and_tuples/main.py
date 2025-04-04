from lists import get_lowest_list_value, get_highest_list_value 

def main():
    user_values = []  
    
    while True:
        print("Menu:")
        print("1. Show the list low/high values")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            if len(user_values) < 3:
                print("Please enter at least 3 values before viewing the list.")
            else:
                lowest = get_lowest_list_value(user_values)
                highest = get_highest_list_value(user_values)
                print(f"The lowest value is: {lowest}")
                print(f"The highest value is: {highest}")
        
        elif choice == "2":
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
        if choice == "1" or len(user_values) < 3:
            while True:
                try:
                    value = int(input("Enter a list value: "))  
                    user_values.append(value)  
                    if len(user_values) >= 3:
                        another_value = input("Do you want to enter another value? (y/n): ")
                        if another_value.lower() != "y":
                            break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

