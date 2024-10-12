def sequence_encoder(sequence: list[int]) -> float:
    constant = 0
    for an in sequence:
        constant += 2**(-an)

    return constant

print(sequence_encoder([2, 3, 5, 7, 11, 13, 17]))