"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer inputArray

    Guaranteed constraints:
    3 ≤ inputArray.length ≤ 10,
    -15 ≤ inputArray[i] ≤ 15.

    [output] integer

    The maximal absolute difference.
"""

def arrayMaximalAdjacentDifference(inputArray):
    if len(inputArray) >= 2:
        adj = inputArray[0]-inputArray[1]
    for i in range(1, len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            sub = inputArray[i] - inputArray[i+1]
        else:
            sub = inputArray[i+1] - inputArray[i]
        if sub > adj:
            adj = sub
    return adj
