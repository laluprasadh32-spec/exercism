def to_rna(dna_strand):
    rna = ""
    for ch in dna_strand:
        if ch == "G":
            rna += "C"
        elif ch == "C":
            rna += "G"
        elif ch == "T":
            rna += "A"
        elif ch == "A":
            rna += "U"
    return rna