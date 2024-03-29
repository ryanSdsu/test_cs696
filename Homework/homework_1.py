"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""


# String Functions
def fast_complement(dna):
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    complementDna = ""
    complementDict = {'C':'G', 'G':'C', 'T':'A', 'A': 'T'}

    for base in dna:
        complementDna += complementDict[base]

    return complementDna


def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    modifiedString = ""
    modifiedString += s[:start]
    modifiedString += s[stop+1:]

    return modifiedString


def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    kmerList = []
    startingInterval = 0

    while(k <= len(s)):
        kmerList.append(s[startingInterval:k])
        startingInterval += 1
        k += 1

    return kmerList

def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmerSet = set()
    startingInterval = 0

    while(k <= len(s)):
        kmerSet.add(s[startingInterval:k])
        startingInterval += 1
        k += 1

    return kmerSet

def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmerList = kmer_list(s, k)
    kmerDictionary = {}

    for element in kmerList:
        if element in kmerDictionary:
            kmerDictionary[element] += 1
        else:
            kmerDictionary[element] = 1

    return kmerDictionary

# Reading Files
def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name, 'r') as x:
        x = x.read().split('\n')
        for i in x[:10]:
            print(i)
    return

def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name, 'r') as x:
        x = x.read().split('\n')
        for i in x[-10:]:
            print(i)
    return

def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name, 'r') as x:
        x = x.read().split('\n')
        [print(x[i]) for i in range(len(x)) if i%2==0]
    return

def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    import csv

    csvFile = open(file_name, 'r')
    csvReader = csv.reader(csvFile)

    return [row for row in csvReader]

def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    import csv

    csvFile = open(file_name, 'r')
    csvReader = csv.reader(csvFile)

    return [row[column - 1] for row in [row for row in csvReader]]


def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    fasta = {}
    with open(file_name, "r") as file_one:
        for line in file_one:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                active_sequence_name = line[1:]
                if active_sequence_name not in fasta:
                    fasta[active_sequence_name] = []
                continue
            sequence = line
            fasta[active_sequence_name].append(sequence)
        singleDna = ""
        for dictKey in fasta:
            valuesInKey = fasta[dictKey]
            for numberOfValueInKey in valuesInKey:
                singleDna += numberOfValueInKey

                fasta[dictKey] = singleDna
            singleDna = ""
    return [fasta[dictKey] for dictKey in fasta]

def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """
    fastaHeaders = []
    with open(file_name, "r") as file_one:
        for line in file_one:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                active_sequence_name = line[1:]
                if active_sequence_name not in fastaHeaders:
                    fastaHeaders.append(active_sequence_name)
                continue
    return fastaHeaders

def fasta_dict(file_name):
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """
    fasta = {}
    with open(file_name, "r") as file_one:
        for line in file_one:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                active_sequence_name = line[1:]
                if active_sequence_name not in fasta:
                    fasta[active_sequence_name] = []
                continue
            sequence = line
            fasta[active_sequence_name].append(sequence)
        singleDna = ""
        for dictKey in fasta:
            valuesInKey = fasta[dictKey]
            for numberOfValueInKey in valuesInKey:
                singleDna += numberOfValueInKey

                fasta[dictKey] = singleDna
            singleDna = ""
    return fasta

def fastq_to_fasta(file_name, new_name=None):
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """
    dotPosition = file_name.find('.')
    fastAFileName = file_name[:dotPosition + 1] + 'fasta'

    with open(file_name, 'r') as fastaQFile:
        with open(fastAFileName, 'w') as fastAFile:
            lineCount = 1
            for line in fastaQFile:
                if lineCount == 1:
                    line = line.replace("@", ">")
                    fastAFile.write(line)
                    lineCount += 1
                elif (lineCount == 2):
                    fastAFile.write(line)
                    lineCount += 1
                elif lineCount == 3:
                    lineCount += 1
                elif lineCount == 4:
                    lineCount = 1
    return

# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    complementDNA = ""

    dnaSequence = list(dna)
    dnaSequence.reverse()

    DNA = ''.join(dnaSequence)
    complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}

    for base in DNA:
        complementDNA += complementDict[base]

    return complementDNA

def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """

    return dna.replace("T","U")

def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
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

    skipCodons = ["UAA", "UGA", "UAG"]
    protenConcatenatedString = ""
    a = 0
    b = 3

    for i in range(len(rna)):
        proteinCodon = rna[a:b]
        if proteinCodon in RNA_CODON_TABLE and proteinCodon not in skipCodons:
            protenConcatenatedString += RNA_CODON_TABLE[proteinCodon]
            a += 3
            b += 3
        else:
            a += 3
            b += 3

    return protenConcatenatedString

def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """

    frames = []
    frames += dna, dna[1:], dna[2:]
    rc = reverse_complement(dna)
    frames += rc, rc[1:], rc[2:]

    return frames

print_even("/Users/RJ/PycharmProjects/test_cs696/Hello World")