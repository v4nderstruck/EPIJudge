from test_framework import generic_test


def reverse_bits_bf(x: int) -> int:
    r = 0
    for _ in range(16):
        h = (x & 1)
        x = x >> 1
        r = (r << 1) | h
    return r 

lookup = [reverse_bits_bf(i) for i in range(2**16)]

def reverse_bits(x: int) -> int:
    wordsize = 16
    mask = int('0xffff', 16)
    return (lookup[x & mask] << 3 * wordsize | 
            lookup[(x >> wordsize) & mask] << 2 * wordsize |
            lookup[(x >> 2 * wordsize) & mask] << wordsize |
            lookup[(x >> 3 * wordsize) & mask] 
    )

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
