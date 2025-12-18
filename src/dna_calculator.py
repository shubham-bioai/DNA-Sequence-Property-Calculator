"""
DNA Sequence Property Calculator

This script calculates basic properties of a DNA sequence:
- Sequence length
- Count of A, T, G, C
- GC percentage
- AT percentage
"""

def validate_dna(sequence):
    """
    Checks whether the given sequence is a valid DNA sequence.
    Allowed characters: A, T, G, C
    """
    sequence = sequence.upper()

    for base in sequence:
        if base not in ["A", "T", "G", "C"]:
            return False
    return True


def calculate_properties(sequence):
    """
    Calculates DNA sequence properties.
    """
    sequence = sequence.upper()

    length = len(sequence)
    count_a = sequence.count("A")
    count_t = sequence.count("T")
    count_g = sequence.count("G")
    count_c = sequence.count("C")

    gc_percentage = ((count_g + count_c) / length) * 100
    at_percentage = ((count_a + count_t) / length) * 100

    return {
        "Length": length,
        "A": count_a,
        "T": count_t,
        "G": count_g,
        "C": count_c,
        "GC%": round(gc_percentage, 2),
        "AT%": round(at_percentage, 2)
    }


def main():
    print("DNA Sequence Property Calculator")
    print("--------------------------------")

    dna_sequence = input("Enter DNA sequence: ").strip()

    if not dna_sequence:
        print("Error: Empty sequence provided.")
        return

    if not validate_dna(dna_sequence):
        print("Error: Invalid DNA sequence.")
        print("Only A, T, G, C characters are allowed.")
        return

    result = calculate_properties(dna_sequence)

    print("\nResults:")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
