from lists import get_p_distance_matrix

def main():
    while True:
        print("\nMenu")
        print("1 - Get p distance matrix")
        print("2 - Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nEnter DNA sequences as lists (you can copy/paste the example below):")
            print("Example format: [['T','T','T','C','C','A','T','T','T','A'], ['G','A','T','T','C','A','T','T','T','C']]")

            try:
                user_input = input("Paste your DNA list here: ")
                dna_lists = eval(user_input)  
                matrix = get_p_distance_matrix(dna_lists)

                print("\nP Distance Matrix:")
                for row in matrix:
                    print(" ".join(f"{value:.5f}" for value in row))
            except Exception as e:
                print("Invalid input. Please try again. Error:", e)

        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
