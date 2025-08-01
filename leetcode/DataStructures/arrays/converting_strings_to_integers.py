
# Problem:
# Given an array of integers as strings and numbers, 
# return the sum of the array values as if all were numbers.
# Return your answer as a number.

def sum_mix(arr):
    test = list(map(int, arr))
    return sum(test)


