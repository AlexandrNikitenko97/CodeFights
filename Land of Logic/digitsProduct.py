"""
Given an integer product, find the smallest positive (i.e. greater than 0) 
integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example
    For product = 12, the output should be
    digitsProduct(product) = 26;
    For product = 19, the output should be
    digitsProduct(product) = -1.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer product

    Guaranteed constraints:
    0 ≤ product ≤ 600.

    [output] integer
"""

from math import sqrt

def digitsProduct(product):
    if product == 0:            # if product = 0 then 1*0 = 0 
        return 10
    if product % 2 != 0:        # check prime numbers
        for j in range(2, int(sqrt(product))+1):
            if product % j == 0:
                break
        else:
            if product <= 7:    # maximal one-digit prime number
                return product
            return -1
    resultNum = ''
    while product != 1:         # if product is not a prime => find the smallest positive numbers
        for i in range(9,1,-1):
            if product % i == 0:
                resultNum += str(i)
                product //= i
                break
        else:
            return -1
    return int(resultNum[::-1])
