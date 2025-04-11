def get_p_distance(list1, list2):
    differences = 0

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            differences += 1

    p_distance = differences / len(list1)
    return p_distance


def get_p_distance_matrix(dna_lists):
    num_sequences = len(dna_lists)
    p_distance_matrix = []

    for i in range(num_sequences):
        row = []
        for j in range(num_sequences):
            distance = get_p_distance(dna_lists[i], dna_lists[j])
            row.append(round(distance, 5))  
        p_distance_matrix.append(row)

    return p_distance_matrix

