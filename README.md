# -k-d--mer-Composition-Generator


# Description
This Python script generates the (k,d)-mer composition from a given DNA sequence. For fixed values of k and d, it extracts pairs of substrings (k-mers) separated by a gap of d nucleotides. Each pair represents a fragment that could be used in sequence assembly algorithms or genome reconstruction problems.

# Usage
Example
```
def generate_composition_from_sequence(sequence):
    k = 3
    d = 2
    composition = []

    for i in range(len(sequence) - 2 * k - d + 1):
        pattern1 = sequence[i:i + k]
        pattern2 = sequence[i + k + d:i + 2 * k + d]
        composition.append((pattern1, pattern2))

    return composition

# Example sequence
sequence = "TAATGCCATGGGATGTT"
composition_result = generate_composition_from_sequence(sequence)

# Print the generated composition
for pair in composition_result:
    print(f"({pair[0]}|{pair[1]})", end=" ")

```

Output
(TAA|CCA) (AAT|CAT) (ATG|ATG) (TGC|TGG) (GCC|GGG) (CCA|GGA) (CAT|GAT) (ATG|ATG) (TGG|TGT) (GGG|GTT) 

# Function Description
* generate_composition_from_sequence(sequence)
Parameters:
* A DNA sequence as a string.

# Returns:
* A list of tuples, each representing a (k,d)-mer pair extracted from the sequence.

# Note:
* In this example, k = 3 and d = 2 are hardcoded.

# Applications
* Preprocessing step for genome reconstruction problems
* Teaching tool for understanding sequence overlap and paired reads
* Useful in k-mer analysis and assembly algorithms

# License
This project is licensed under the MIT License.

