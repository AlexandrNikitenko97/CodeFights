"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

    For name = &quot;var_1__Int&quot;, the output should be
    variableName(name) = true;
    For name = &quot;qq-q&quot;, the output should be
    variableName(name) = false;
    For name = &quot;2w2&quot;, the output should be
    variableName(name) = false.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string name

    Guaranteed constraints:
    1 ≤ name.length ≤ 10.

    [output] boolean

    true if name is a correct variable name, false otherwise.
"""

def variableName(name):
    if name[0].isdigit():
        return False
    else:
        counter = 0
        for i in name:
            if i.isdigit() or i.isalpha() or i == '_':
                counter += 1
    return True if counter == len(name) else False
