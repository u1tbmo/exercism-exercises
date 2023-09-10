protein_dict = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
}

def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)] # split sequence into codons
    proteins = []
    for codon in codons:
        if protein_dict[codon] == 'STOP':
            break
        else:
            proteins.append(protein_dict[codon])
    return proteins