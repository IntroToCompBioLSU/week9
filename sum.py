#!/usr/bin/env python

# Will use sys for command-line arguments
import sys

# Command-line arguments should be numbers
# This list will hold the converted integer values
nums = []
for num in sys.argv[1:]:    # Start at index 1 to avoid program name
    nums.append(int(num))

def sum(listOfInts):
    """This function will calculate the sum of integers in a list."""
    total = 0
    for myInt in listOfInts:
        total = total + myInt
    return total  # The return statement "returns" a variable
                  # so the value can be saved or printed

print(sum(nums))

