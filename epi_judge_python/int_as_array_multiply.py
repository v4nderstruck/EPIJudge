from typing import List

from test_framework import generic_test

def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1   
    
    if num2[0] < 0:
        num2[0] *= -1
    if num1[0] < 0:
        num1[0] *= -1

    if num1[0] == 0 or num2[0] == 0:
        return [0]

    result = [0] * (len(num1) + len(num2))
    for shift, i in enumerate(num2[::-1]):
        for offset,j in enumerate(num1[::-1]):

            result[shift+offset] += i * j
            result[shift+offset+1] += result[shift+offset] // 10
            result[shift+offset] = result[shift+offset] % 10
    
    cut_off = len(result) - 1
    while result[cut_off] == 0:
        cut_off -= 1

    result[cut_off] *= sign
    result = result[:cut_off+1]
    return result[::-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
