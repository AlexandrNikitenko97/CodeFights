"""
Given a string, return its encoding defined as follows:

    First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
        for example, "aabbbc" is divided into ["aa", "bbb", "c"]
    Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
        for example, substring "bbb" is replaced by "3b"
    Finally, all the new strings are concatenated together in the same order and a new string is returned.

Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string s

    String consisting of lowercase English letters.

    Guaranteed constraints:
    4 ≤ s.length ≤ 15.

    [output] string
"""

def lineEncoding(s):
    count = 1
    s += ' '      # add a space to check last element
    result = ''
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if count == 1:
                result += s[i]
            else:
                result += str(count) + s[i]
                count = 1
        else:
            count += 1
            
    return result
            
        
