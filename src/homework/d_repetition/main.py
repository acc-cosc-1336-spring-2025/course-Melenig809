from repetition import get_factorial, sum_odd_numbers

def get_valid_number(prompt, min_val, max_val):
    """Prompt user for a valid number within a range."""
    while True:
        try:
            num = int(input(prompt))  # Convert input to integer
            if min_val <= num <= max_val:
                return num
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def main():
    while True:
        print("\nHomework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            num = get_valid_number("Enter a number (1-9) for factorial: ", 1, 9)
            result = get_factorial(num)
            print(f"Factorial of {num} is {result}")
        
        elif choice == "2":
            num = get_valid_number("Enter a number (1-99) for sum of odd numbers: ", 1, 99)
            result = sum_odd_numbers(num)
            print(f"Sum of odd numbers up to {num} is {result}")
        
        elif choice == "3":
            exit_choice = input("Are you sure you want to exit? (y/n): ").strip().lower()
            if exit_choice == "y":
                print("Goodbye!")
                break  
        
        else:
            print("Invalid choice! Please select a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()
