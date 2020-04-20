def distance(strand_a, strand_b):
    if type(strand_a) is not str or type(strand_b) is not str:
        raise ValueError("Wrong type.")
        # return "Wrong type :/"

    # All capitals
    strand_a = strand_a.upper()
    strand_b = strand_b.upper()

    if len(strand_a) != len(strand_b):
        raise ValueError("Length mismatch")
        # return "Length mismatch"

    valid_chars = ["C", "A", "G", "T"]

    count = 0
    for i in range(len(strand_a)):
        if strand_a[i] not in valid_chars or strand_b[i] not in valid_chars:
            raise ValueError("Invalid DNA strand")
            # return "Invalid DNA strand"
        if strand_a[i] != strand_b[i]:
            count += 1
    return count


# tests
print(distance("GAT", "CCT"))
print(distance(12, 24))
print(distance("not", "dna"))
print(distance("", ""))
print(distance("gat", "GAT"))
