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
    fastaDict = {}
    dnaValidLetters = ["A", "C", "G", "T"]
    proteinCheck = "false"

    import os

    for file in os.listdir(folder_path):
        if not file.endswith('.fasta'):
            continue

        file = folder_path + "/" + file

        with open(file, "r") as file_one:
            x = file_one.read()
            sequences = x.split('>')
            fastaList = sequences[1:]

            for element in fastaList:
                elementSplit = element.split('\n', 1)
                header = elementSplit[0]
                sequence = elementSplit[1].replace('\n', "")

                #Removes all the empty sequences
                if sequence == "":
                    continue

                #Removes all of the proteins
                for char in range(len(sequence)):
                    if sequence[char] in dnaValidLetters:
                        continue
                    else:
                        proteinCheck = "true"
                        break

                if proteinCheck == "true":
                    proteinCheck = "false"
                    continue

                #Check if the duplicate headers have the same sequence or not
                if header not in fastaDict:
                    fastaDict[header] = sequence
                elif fastaDict[header] != sequence:
                    fastaDict.pop(header)
                    print("duplicate headers with non-identical sequences were found for: " + header)
                elif fastaDict[header] == sequence:
                    print("a duplicate entry exists for: " + header)

    return fastaDict