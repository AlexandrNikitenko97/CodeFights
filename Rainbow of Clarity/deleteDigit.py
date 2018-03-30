"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

    For n = 152, the output should be
    deleteDigit(n) = 52;
    For n = 1001, the output should be
    deleteDigit(n) = 101.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer n

    Guaranteed constraints:
    10 ≤ n ≤ 106.

    [output] integer
"""

def deleteDigit(n):
    maximum = 0
    for i in range(len(str(n))):
        num = str(n)[:i] + str(n)[i+1:]
        if int(num) > maximum:
            maximum = int(num)
    return maximum
            
