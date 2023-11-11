from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:

    furthes_we_can_go = 0
    i = 0
    while i <= furthes_we_can_go and furthes_we_can_go < len(A) - 1:
        furthes_we_can_go = max(furthes_we_can_go, A[i] + i)
        i+=1



    return furthes_we_can_go >= len(A) - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
