"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string text

    Guaranteed constraints:
    4 ≤ text.length ≤ 50.

    [output] string

    The longest word from text. It's guaranteed that there is a unique output.
"""

def longestWord(text):
    badSymbols = [i for i in text if not i.isalpha()]
    for i in badSymbols:
        text = text.replace(i, ' ')
    maxLen = 0
    ind = 0
    splitted = text.split()
    for i, j in enumerate(splitted):
        if len(j) > maxLen:
            maxLen = len(j)
            ind = i
    return splitted[ind]
