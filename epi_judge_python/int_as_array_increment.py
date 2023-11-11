from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    of = 1
    for i in range(len(A)-1, -1, -1):
        v = A[i] + of
        of = v // 10
        A[i] = v % 10
        
    if of:
        A = [1] + A

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
