from fractions import Fraction, gcd


def gauss_elimination(m, values):
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            ratio = -m[j][i] / m[i][i]
            for k in range(i, len(m)):
                m[j][k] += ratio * m[i][k]
            values[j] += ratio * values[i]
    res = [0 for _ in range(len(m))]
    for i in range(len(m)):
        index = len(m) - 1 - i
        end = len(m) - 1
        while end > index:
            values[index] -= m[index][end] * res[end]
            end -= 1
        res[index] = values[index] / m[index][index]
    return res


def solution(m):
    sum_list = list(map(sum, m))
    bool_indices = list(map(lambda z: z == 0, sum_list))
    indices = set([i for i, y in enumerate(bool_indices) if y])
    new_m = [
        list(
            map(
                lambda x: Fraction(0, 1)
                if (sum_list[i] == 0)
                else Fraction(
                    x / gcd(x, sum_list[i]), sum_list[i] / gcd(x, sum_list[i])
                ),
                m[i],
            )
        )
        for i in range(len(m))
    ]
    transform_m = []
    zeros_m = []
    for i in range(len(new_m)):
        if i not in indices:
            transform_m.append(new_m[i])
        else:
            zeros_m.append(new_m[i])
    transform_m.extend(zeros_m)
    tm = []
    for i in range(len(transform_m)):
        tm.append([])
        extend_m = []
        for j in range(len(transform_m)):
            if j not in indices:
                tm[i].append(transform_m[i][j])
            else:
                extend_m.append(transform_m[i][j])
        tm[i].extend(extend_m)
    res = [tm, len(zeros_m)]
    if res[1] == len(m):
        return [1, 1]
    length_q = len(res[0]) - res[1]
    q = [[int(i == j) - res[0][i][j] for j in range(length_q)] for i in range(length_q)]
    r = [res[0][i][length_q:] for i in range(length_q)]
    tm = [[q[i][j] for i in range(len(q))] for j in range(len(q))]
    inv = [
        gauss_elimination(tm, [Fraction(int(i == j), 1) for j in range(len(q))])
        for i in range(len(tm))
    ]
    res = []
    for i in range(len(inv)):
        res.append([])
        for j in range(len(r[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(inv[0])):
                res[i][j] += inv[i][k] * r[k][j]
    l = reduce(lambda p, d: p * d.denominator / gcd(p, d.denominator), res[0], 1)
    res = list(map(lambda x: x.numerator * l / x.denominator, res[0]))
    res.append(l)
    return res
