from test_framework import generic_test




def parity_bruteforce(x: int) -> int:
    c = 0
    for i in range(64):
        if x & (1 << i):
            c += 1

    return 1 if c % 2 else 0

precompute_parity = dict(zip(list(range(2**16)),[parity_bruteforce(i) for i in range(2 ** 16)]))

def parity(x: int) -> int:
    word_size = 16
    mask = int('0xffff', 16)
    return (precompute_parity[x & mask] ^ 
            precompute_parity[(x >> word_size) & mask] ^
            precompute_parity[(x >> 2 * word_size) & mask] ^
            precompute_parity[(x >> 3 * word_size) & mask] 
            )



if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
