def solution(start, length):
    checksum = 0
    for i in range(length):
        first = start + length * i - 1
        last = first + length - i
        checksum ^= xor(first) ^ xor(last)
    return checksum


def xor(x):
    return {0: x, 1: 1, 2: x + 1}.get(x % 4, 0)
