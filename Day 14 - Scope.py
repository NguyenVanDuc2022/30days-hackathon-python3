"""
Day 14 - Complete the Difference class by writing the following:
A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the
maximumDifference instance variable.
--- Nguyen Van Duc ---
"""


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        sorted_elements = sorted(self.__elements)
        self.maximumDifference = abs(sorted_elements[-1] - sorted_elements[0])


# End of Difference class
ab = [int(e) for e in input("Enter your data: ").split(" ")]
d = Difference(ab)
print(d.maximumDifference)
