"""
Exercise 8


1) Write a definition called 'compute' which takes in only **kwargs and meets the following specifications:
    - ensure that the key word 'input' is always be a list of integers before proceeding
    - if the key word 'action' is 'sum' then return the sum of all integers
    - if the key word 'action' is 'mean' then return  the mean of all integers
    - if the key word 'return_float' is 'True', then any return value should be a float


2) Implement an argument parser as a main function that meets the following requirements:
    - when run from terminal, your program should be able to accept any number of arguments
    - if -s is used, your program should print the sum of all arguments
        python3 exercise_08.py -s 1 5 20
        26
    - if -m is used, your program should multiply each value by the value of -m and print the result
        python3 exercise_08.py -m 5 1 5 20
        5
        25
        100
    - your program should also have descriptions and help attributes for each argument

"""
import sys
import argparse
import numpy

def compute(**kwargs):
    getInput = kwargs['input']

    def checkInput(list):
        newList = []
        for x in list:
            if type(x) == int:
                newList.append(int(x))
            else:
                return False
        return newList

    listOfInts = checkInput(getInput)

    if input is not False:
        getAction = kwargs['action']
        getFloatKey = kwargs['return_float']

        if getAction == "sum" and getFloatKey == True:
            return float(sum(listOfInts))
        if getAction == "sum" and getFloatKey == False:
            return sum(listOfInts)
        if getAction == "mean" and getFloatKey == True:
            return float(numpy.mean(listOfInts))
        if getAction == "mean" and getFloatKey == False:
            return numpy.mean(listOfInts)



print(compute(input = [0,1,2,3], action='sum', return_float=True))
print(compute(input = [0,1,2,3], action='sum', return_float=False))
print(compute(input = [0,1,2,3], action='mean', return_float=True))
print(compute(input = [0,1,2,3], action='mean', return_float=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This program is meant to take in arguments and return either the sum or multiplcations thereof')
    parser.add_argument('-m', '--multiply', help='This requires one argument and then returns that number multiplied by all the others', type=int)
    parser.add_argument('-s', '--sum', help='This adds all of the arguments after -s and returns the sum', action='store_true')
    parser.add_argument('remainder', help='This contains a list of all the numbers after the argument -s and/or after the 1st argument when using -m', nargs=argparse.REMAINDER)

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(1)

    if args.multiply:
        for number in [int(x) for x in args.remainder]:
            print(number * args.multiply)

    if args.sum:
        summation = 0
        for number in [int(x) for x in args.remainder]:
            summation += number
        print(summation)

    print('it worked')
    print("remainder is: {}".format(args.remainder))
    print(' multiply by: {}'.format(args.multiply))