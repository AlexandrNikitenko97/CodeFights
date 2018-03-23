"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString="123aa1", the output should be
longestDigitsPrefix(inputString) = "123".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    Guaranteed constraints:
    3 ≤ inputString.length ≤ 35.

    [output] string
"""

def longestDigitsPrefix(inputString):
    if not inputString[0].isdigit():
        return ''
    else:
        i = 0
        prefix = ''
        while i < len(inputString):
            if not inputString[i].isdigit():
                break
            prefix += inputString[i]
            i += 1
        return prefix
        
