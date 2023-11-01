def to_rna(dna_strand):
    DNA_NUCLEOTIDES = 'GCTA'
    RNA_NUCLEOTIDES = 'CGAU'
    dna_to_rna = str.maketrans(DNA_NUCLEOTIDES, RNA_NUCLEOTIDES)
    rna_strand = ""
    for letter in dna_strand:
        rna_strand += letter.translate(dna_to_rna)
    return rna_strand
