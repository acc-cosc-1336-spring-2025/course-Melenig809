# Function to calculate Hamming distance between two DNA strings
def get_hamming_distance(dna1, dna2):
    # Check that the two strings are of equal length
    if len(dna1) != len(dna2):
        return "Error: DNA strings must be of equal length"
    
    # Initialize a counter for the differences
    hamming_distance = 0
    
    # Loop through both DNA strings and compare each base
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming_distance += 1
    
    return hamming_distance

# Function to get the reverse complement of a DNA string
def get_dna_complement(dna):
    # Dictionary to map each DNA base to its complement
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Initialize an empty string to hold the complement
    complement = ""
    
    # Loop through the DNA string in reverse order
    for i in range(len(dna) - 1, -1, -1):
        complement += complement_map[dna[i]]
    
    return complement

print(get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")) 

print(get_dna_complement("GTCA")) 

