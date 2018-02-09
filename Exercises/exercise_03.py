"""
exercise_03
2/8/2018

For this Exercise you will write one definition that will take in the name of a
directory as a string, and return a dictionary containing every sequence in every FASTA file where
the sequence header is the key and the DNA sequences are values.

Your definition will be tested with improperly formatted FASTA files and should handle the following cases:
    1) If there are extra new line characters, or empty lines, your program should still process sequences normally
    2) If a duplicate header exists between two entries your definition should check to see if the sequences are the same
        * If the headers and sequences are identical, your program should print a message that "a duplicate entry exists
          for <header>" and continue normally.
        * If the only the headers match, you should print a message that "duplicate headers with non-identical
          sequences were found for <header>" and neither entry should be added in the dictionary.
          (your print statements don't need to be identical to what I have written here)
    3) If a file in the directory is not a fasta file, your program should not open it.
    4) If a sequence contains characters that are not A, C, G, or T, then it should not be added to the dictionary.

If your program is working correctly, the dictionary should only contain the 4 "good sequence"s in the test folder.


The following syntax may be helpful:

# deleting from a dictionary
del my_dictionary[key]

# printing and formatting a string
x = 'my_variable'
print('Error related to variable: {}'.format(x))

# checking your final dictionary by printing out key, value pairs
for key, value in my_dictionary.items():
    print('Key is: {}\tValue is: {}'.format(key, value))

"""

import os

def fasta_folder_to_dict(folder_path):
    """
    Constructs a dictionary of all of the FASTA formatted entries from a folder containing FASTA files.
    :param folder_path: string
    :return: dictionary
    """
    fastaDictionary = {}
    duplicateFastaDictionary = {}
    duplicateSequenceName = "false"

    for file in os.listdir(folder_path):
        if not file.endswith('.fasta'):
            continue

        file = folder_path + "/" + file

        with open(file, "r") as file_one:
            for line in file_one:
                sequence = line.strip()
                if not sequence:
                    continue
                if sequence.startswith(">"):
                    active_sequence_name = line[1:]
                    active_sequence_name = active_sequence_name.replace("\n", "")
                    if active_sequence_name not in fastaDictionary:
                        duplicateSequenceName = "false"
                        fastaDictionary[active_sequence_name] = []
                        continue
                    else:
                        duplicateSequenceName = "true"
                        duplicateFastaDictionary[active_sequence_name] = []
                        continue

                if duplicateSequenceName == "false":
                    fastaDictionary[active_sequence_name].append(sequence)
                else:
                    duplicateFastaDictionary[active_sequence_name].append(sequence)

            concatenateToSingleDna = ""
            for dictKey in fastaDictionary:
                valuesInKey = fastaDictionary[dictKey]
                for numberOfValueInKey in valuesInKey:
                    concatenateToSingleDna += numberOfValueInKey

                    fastaDictionary[dictKey] = concatenateToSingleDna
                concatenateToSingleDna = ""

            concatenateToSingleDna = ""
            for dictKey in duplicateFastaDictionary:
                valuesInKey = duplicateFastaDictionary[dictKey]
                for numberOfValueInKey in valuesInKey:
                    concatenateToSingleDna += numberOfValueInKey

                    duplicateFastaDictionary[dictKey] = concatenateToSingleDna
                concatenateToSingleDna = ""

    keysToBeRemoved = set()
    #Removes all of the empty sequences
    for originalKey in fastaDictionary:
        if fastaDictionary[originalKey] == []:
            keysToBeRemoved.add(originalKey)
            continue

    for key in keysToBeRemoved:
        fastaDictionary.pop(key)

    #Removes all of the proteins
    dnaValidLetters = ["A", "C", "G", "T"]
    for originalKey in fastaDictionary:
        testSequence = fastaDictionary[originalKey]
        for char in range(len(testSequence)):
            if testSequence[char] in dnaValidLetters:
                continue
            else:
                keysToBeRemoved.add(originalKey)
                break

    #Removes all of the duplicate headers with non-identical sequences and keep the ones with the same entries
    for originalKey in fastaDictionary:
        for duplicateKey in duplicateFastaDictionary:
            if duplicateKey == originalKey:
                if duplicateFastaDictionary[duplicateKey] == fastaDictionary[originalKey]:
                    print("a duplicate entry exists for: " + duplicateKey)
                if duplicateFastaDictionary[duplicateKey] != fastaDictionary[originalKey]:
                    print("duplicate headers with non-identical sequences were found for: " + duplicateKey)
                    keysToBeRemoved.add(originalKey)


    #Remove all the invalid keys
    for key in keysToBeRemoved:
        if key in fastaDictionary:
            fastaDictionary.pop(key)

    return fastaDictionary

