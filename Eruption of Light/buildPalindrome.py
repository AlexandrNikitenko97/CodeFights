"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string 
to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string st

    A string consisting of lowercase latin letters.

    Guaranteed constraints:
    3 ≤ st.length ≤ 10.

    [output] string
"""

def buildPalindrome(st):
    if st == st[::-1]:
        return st
    else:
        tail = ''
        for i in st:
            tail += i
            if (st + tail[::-1]) == (st+tail[::-1])[::-1]:
                return st + tail[::-1]
