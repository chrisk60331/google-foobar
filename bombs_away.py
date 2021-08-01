def solution(m, f):
    cycles, m, f = 0, int(m), int(f)
    while True:
        if 0 in [f, m]:
            cycles = "impossible"
            break
        elif f == 1:
            cycles += m - 1
            break
        else:
            cycles += m / f
            m, f = f, m % f
    return str(cycles)
