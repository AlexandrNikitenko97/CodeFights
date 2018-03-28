"""
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.

Example

    For inputString = "bbbaacdafe", the output should be
    isBeautifulString(inputString) = true;
    For inputString = "aabbb", the output should be
    isBeautifulString(inputString) = false;
    For inputString = "bbc", the output should be
    isBeautifulString(inputString) = false.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    A string of lowercase letters.

    Guaranteed constraints:
    3 ≤ inputString.length ≤ 50.

    [output] boolean
"""

from string import ascii_lowercase as ascii
from collections import Counter

def isBeautifulString(inputString):
    sortedInputString = sorted(set(inputString.lower()))
    if ascii[:ascii.index(sortedInputString[len(sortedInputString)-1])+1] != ''.join(sortedInputString):
        return False
    else:
        counts = Counter(inputString) 
        for i in range(len(sortedInputString)-1):
            if counts[sortedInputString[i]] < counts[sortedInputString[i+1]]:
                return False
    return True
    
    
