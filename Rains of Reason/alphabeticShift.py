"""
Given a string, replace each its character by the next one in the English alphabet (z would be replaced by a).

Example

For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    Non-empty string consisting of lowercase English characters.

    Guaranteed constraints:
    1 ≤ inputString.length ≤ 1000.

    [output] string

    The result string after replacing all of its characters.
"""

import string

def alphabeticShift(inputString):
    alphabet = list(string.ascii_lowercase)
    newString = ''
    for i in range(len(inputString)):
        try:
            newString += alphabet[alphabet.index(inputString[i]) + 1]
        except IndexError:
            newString += alphabet[0]  
return newString
