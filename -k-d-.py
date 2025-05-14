def generate_composition_from_sequence(sequence):
    k = 3
    d = 2
    composition = []

    for i in range(len(sequence) - 2 * k - d + 1):
        pattern1 = sequence[i:i + k]
        pattern2 = sequence[i + k + d:i + 2 * k + d]
        composition.append((pattern1, pattern2))

    return composition

sequence = "TAATGCCATGGGATGTT"
composition_result = generate_composition_from_sequence(sequence)

for pair in composition_result:
    print(f"({pair[0]}|{pair[1]})", end=" ")
