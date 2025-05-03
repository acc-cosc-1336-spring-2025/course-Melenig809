from class_a import Die  

def main():
    die = Die()  
    while True:  
        print("1. Roll the die")
        print("2. Exit")
        
        choice = input("Please choose an option (1 or 2): ")
        
        if choice == "1":
            die.roll() 
            print(die)  
            continue_choice = input("Do you want to roll again? (y/n): ")
            if continue_choice.lower() != 'y':
                break  
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break  
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

