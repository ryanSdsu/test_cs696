"""
Exercise 9


1) Write a decorator function that prints the:
     - real world time taken to run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowlege of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math

def time_decorator(my_def):
    def internal_wrapper():
        t0 = time.time()
        p0 = time.process_time()
        def_result = my_def()
        t1 = time.time()
        p1 = time.process_time()
        print("'{}' finished in {} seconds via real world".format(my_def.__name__, t1-t0))
        print("'{}' finished in {} seconds via processing time".format(my_def.__name__, p1-p0))
        print("The size of the '{}' function is: {}".format(my_def.__name__, sys.getsizeof(def_result)))
        return def_result
    return internal_wrapper # remember, 'internal_wrapper' is not the same as 'internal_wrapper()'

def squares():
    return [x**2 for x in range(1000000)]

time_decorator(squares)()  # note this is "squares" not "squares()"; "squares()" is a list, not a function.

def for_loop():
    emptyList = []
    for index in range(1000000):
        emptyList.append(index)
    return emptyList

time_decorator(for_loop)()  # note this is "squares" not "squares()"; "squares()" is a list, not a function.

def list_comp():
    return [i for i in range(1000000)]

time_decorator(list_comp)()

def numpy_list():
    listOfNumbers = [i for i in range(1000000)]
    return numpy.array(listOfNumbers)

time_decorator(numpy_list)()

def panda_list():
    listOfNumbers = [i for i in range(1000000)]
    df = pandas.DataFrame(listOfNumbers)
    return df

time_decorator(panda_list)()

def generator_list():
    for idx in range(1000000):
        yield idx

time_decorator(generator_list)()

def for_loop_log():
    emptyList = []
    for index in range(1, 1000001):
        emptyList.append(math.log10(index))
    return emptyList

time_decorator(for_loop_log)()  # note this is "squares" not "squares()"; "squares()" is a list, not a function.

def list_comp_log():
    return [math.log10(i) for i in range(1, 1000001)]

time_decorator(list_comp_log)()

def numpy_list_log():
    listOfNumbers = [math.log10(i) for i in range(1, 1000001)]
    return numpy.array(listOfNumbers)

time_decorator(numpy_list_log)()

def panda_list_log():
    listOfNumbers = [math.log10(i) for i in range(1, 1000001)]
    df = pandas.DataFrame(listOfNumbers)
    return df

time_decorator(panda_list_log)()

def generator_list_log():
    for idx in range(1, 1000001):
        yield math.log10(idx)

time_decorator(generator_list_log)()
