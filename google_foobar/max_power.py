import itertools


def solution(arr):
    negs = [num for num in arr if num < 0]
    pos = [num for num in arr if num > 0]
    if len(arr) == 1 or not pos and not negs:
        return str(arr[0])
    if len(pos) + len(negs) == 1:
        return str(max(arr))
    negs.sort()
    if len(negs) % 2 == 1:
        negs = negs[:-1]
    product = 1
    for x in itertools.chain(pos, negs):
        product *= x
    return str(product)
