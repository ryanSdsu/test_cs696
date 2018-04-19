"""
Exercise 10 - Generators

For this exercise you will be writing a class for several different generator functions.

1) Write a class called "Gens".
    - This class is initialized with a single integer that is called "start"
    - Include a __str__() method so that when an instance of your class is printed, the returned string includes the value of "start"
        EX: "Start value for generators class is: 5"
    - All generator methods should start at the "start" value, if one is not provided, the class should default to a start value of 1

2) Include in this class, the following methods:
    doubles() - yields number * 2 to infinity, starting at self.start
        Gens(1).doubles() -> 1, 2, 4, 8, 16, ...

    fib() - Yields the next number in the fibonacci sequence to infinity, starting at 1
        Gens(100).fib() -> 1, 1, 2, 3, 5, 8, ...

    linear(n) - yields number + n to infinity, starting at self.start
        Gens(1).linear(2) -> 1, 3, 5, 7, 9, ...

    exponential(n) - yields number raised to the power n to infinity, starting at self.start
        Gens(2).exponential(2) -> 2, 4, 16, 256, ...

    sequence(list) - Ignores starting number, yields one value at a time in the list, looping infinitely many times
        Gens(0).sequence([2, 3, 4]) -> 2, 3, 4, 2, 3, 4, ...

    triple_half() -  Yields a number * 3, then the number / 2, repeating to infinity, starting at self.start
        Gens(2).triple_half() -> 2, 6, 3, 9, 4.5, 13.5, ...

"""
import math

class Gens:

    def __init__(self, start=1):
        self.start = start
        return

    def doubles(self):
        while True:
            self.start = self.start * 2
            yield self.start

    def fib(self):
        curr = 0
        next = 1
        while True:
            yield curr
            curr, next = next, curr + next

    def linear(self, increment):
        self.increment = increment
        while True:
            self.start = self.start + self.increment
            yield self.start

    def exponential(self, increment):
        self.increment = increment
        while True:
            self.start = self.start ** self.increment
            yield self.start

    def sequence(self, listOfNumbers):
        startIndex = 0
        while True:
            if startIndex == len(listOfNumbers):
                startIndex = 0
            yield listOfNumbers[startIndex]
            startIndex += 1

    def triple_half(self):
        while True:
            self.start = self.start * 3
            yield self.start
            self.start = self.start / 2
            yield self.start

    def __str__(self):
        return "Start value for generators class is: {}".format(self.start)


x = Gens(2)

# fib = x.fib()
# print(next(fib))
# print(next(fib))

#
# for i in x.doubles():
#     while i < 1000000:
#         print(i)
#         break

# for i in x.linear(2):
#     while i < 100:
#         print(i)
#         break

# for i in x.exponential(2):
#     if i < 1000000:
#         print(i)
#     else:
#         break

# seq = x.sequence([2, 3, 4])
#
# print(next(seq))
# print(next(seq))
# print(next(seq))
# print(next(seq))
# print(next(seq))


# for i in x.sequence([2, 3, 4]):
#     if i < 100:
#         print(i)
#     else:
#         break

# triple = x.triple_half()
#
# print(next(triple))
# print(next(triple))
# print(next(triple))
# print(next(triple))
# print(next(triple))
#
# for i in x.triple_half():
#     if i < 100:
#         print(i)
#     else:
#         break