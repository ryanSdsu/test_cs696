"""
Exercise 4

Practicing List Comprehension (with if and if else statements)
Each of these definitions is already complete, solve each of the following definitions using list comprehension.
Solutions do not need to be 1 line long.

List Comprehension is sometimes called List Display:
    https://docs.python.org/3.6/reference/expressions.html#list-displays
"""


def rc(dna):
    """
    This is the third iteration of our reverse compliment function. Use a dictionary AND list comprehension to
    convert a DNA string into its reverse compliment.
    EX: rc("CCCTTTCCCAAA") should return "TTTGGGAAAGGG"
    :param dna: A string containing only C, T, A, and G
    :return: A string containing only C, T, A, and G
    """
    comp_dict = {"A": "T", "G": "C", "T": "A", "C": "G"}

    rc_dna =[comp_dict[char] for char in dna]

    return ''.join(rc_dna[::-1])

#print(rc("CCCTTTCCCAAA"))

def percent_decimal(numbers):
    """
    Takes in a list of numbers and converts a percentage to a decimal or a decimal to a percentage
    depending on the input i
    EX: percent_decimal([0.0, 0.5, 1.0, 50.0, 100.0]) should return [0.0, 50.0, 100.0, 0.5, 1.0]
    :param i: a list of floats between 0 and 100
    :return: a list of floats between 0 and 100
    """

    return [num /100 if num > 1 else num * 100 for num in numbers]

def multiple_proteins_from_rna(rna):
    """
    Using the RNA table provided, translate a string of RNA into every possible protein
    starting at the amino acid Methionine (M) going to the first stop codon (*).
    NOTE: There can be multiple proteins from a single strand of RNA.

    For Example, the RNA string: UCCAUGUUUAUGAGGAGGUGA
    translates into the amino acid string SMFMRR*, which contains two possible proteins
    your program should return the proteins MFMRR and MRR in a list ['MFMRR', 'MRR'].

    It is OK to include the * symbol for this definition.

    :param rna: a string
    :return: a list of strings
    """
    C2AA = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                       "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                       "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
                       "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
                       "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                       "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                       "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                       "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                       "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                       "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                       "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                       "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                       "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                       "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                       "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                       "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}


    # Turn the input string (rna) into its amino acid composition
    #protein = ''
    #for i in range(0, len(rna), 3): # Loop over numbers, not characters and increment by 3 every loop
    #    protein += C2AA[rna[i:i+3]]  # rna[i:i+3] is the 3 letter codon that will be translated with the C2AA dictionary

    protein = [C2AA[rna[i:i+3]] for i in range(0, len(rna), 3)]

    #Now we extract every [M -> end] slice of our protein
    #protein_list = []
    #for index, char in enumerate(protein):  # enumerate() lets us loop over characters and indexes at the same time
    #    if char == "M":
    #        protein_list.append(protein[index:])  # append the found protein from M to the end of the string

    return [''.join(protein[index:])for index, char in enumerate(protein) if char == "M"]

#print(multiple_proteins_from_rna("UCCAUGUUUAUGAGGAGGUGA"))