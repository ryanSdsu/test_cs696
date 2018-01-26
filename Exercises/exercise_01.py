"""
Exercise 1
Place this script inside a new folder in your github repository called "Exercises".
This will be the directory for all of your in-class exercises this semester.

By the end of class on Thursday 1/25, students should have:
    - Created a private github repo for this class
    - Added their information to this sheet:
        https://docs.google.com/spreadsheets/d/1EKNYOqTnxelmBT4jqotRbUer5eVvWYM9RloN5doScyo/edit?usp=sharing
    - Added my github account (kylelevi) as a collaborator for their private repository
    - Completed these definitions and pushed this script to a folder called "Exercises" in their repo

"""

def hello():
    """
    Prints "Hello World"
    :return: None
    """
    print("Hello World")
    return

def percent_decimal(i):
    """
    Converts a percentage to a decimal or a decimal to a percentage depending on the input i
    :param i: a float between 0 and 100
    :return: a float between 0 and 100
    """

    if isinstance(i, int):
        i = float(i)
        i = i * 100
        i = str(i)
        i = i + "%"
        return i

    if isinstance(i, float):
        i = i * 100
        i = str(i)
        i = i + "%"
        return i

    if '%' in i:
        locationOfPercent = i.find("%")
        floatStrippedOfPercent = i[0:locationOfPercent]
        i = float(floatStrippedOfPercent)
        i = i / 100
        return i

def exponent(integer, power):
    """
    Using a loop (no imports!), raise the integer given to the power provided. (integer^power)
    :param integer: a positive, non zero, integer
    :param power: a positive, non zero, integer
    :return: an integer
    """
    total = integer
    if (power == 0):
        print(1)
        return 1
    if (power > 0):
        for index in range(power - 1):
            total = total * integer
        print(total)
        return total
    else:
        power = power * -1
        for index in range(power - 1):
            total = total * integer
        total = 1 / total
        print(total)
        return total

def complement(dna):
    """
    Returns the complement strand of DNA to the input.  C <--> G,  A <--> T
    :param dna: String containing only C, T, A, and G
    :return: String containing only C, T, A, and G
    """
    complementDna = ""
    complementDictionary = {"C":"G", "G":"C", "T":"A", "A":"T"}

    for base in dna:
        complementDna += complementDictionary[base]

    print (complementDna)
    return complementDna
