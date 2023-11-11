from test_framework import generic_test


base_to_v = dict(zip(list(map(str,range(10))) + list(map(chr, range(ord("A"), ord("G")))), list(range(16))))
v_to_base = dict(zip(list(range(16)), list(map(str,range(10))) + list(map(chr, range(ord("A"), ord("G"))))))

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    if b1 == b2:
        return num_as_string

    result = ''
    v_base10 = 0
    signess = ""
    for i, c in enumerate(num_as_string[::-1]):
        if c == "-":
            signess = "-"
        else:
            v_base10 += base_to_v[c] * b1**i

    if v_base10 == 0:
        return "0"
    q = v_base10 // b2
    while v_base10 > 0:
        q = v_base10 // b2
        remainder = v_base10 % b2
        result += v_to_base[remainder]

        v_base10 = q
        q = v_base10 // b2

    return  signess + result[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
