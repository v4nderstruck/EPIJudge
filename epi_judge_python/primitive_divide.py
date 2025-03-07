from test_framework import generic_test


def divide(x: int, y: int) -> int:
    q = 0
    if x < y:
        return 0
    if x == y:
        return 1

    while x >= y:
        x -= y
        q += 1


    return q

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
