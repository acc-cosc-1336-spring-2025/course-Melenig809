import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from homework.h_strings.strings import get_hamming_distance
from homework.h_strings.strings import get_dna_complement

def main():
    while True:
        print("Menu:")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")
        
        choice = input("Please select an option (1, 2, or 3): ")

        if choice == '1':
            dna1 = input("Enter the first DNA string: ")
            dna2 = input("Enter the second DNA string: ")
            print(f"Hamming Distance: {get_hamming_distance(dna1, dna2)}")

        elif choice == '2':
            dna = input("Enter a DNA string: ")
            print(f"DNA Complement: {get_dna_complement(dna)}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
