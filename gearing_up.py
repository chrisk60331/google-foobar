from fractions import Fraction


def solution(peg_positions):
    default = -1, -1
    if len(peg_positions) < 2:
        return default

    even = True if len(peg_positions) % 2 == 0 else False
    gap = - peg_positions[0] + peg_positions[-1] if even else (
        - peg_positions[0] - peg_positions[-1]
    )
    if len(peg_positions) > 2:
        for index in range(1, len(peg_positions) - 1):
            gap += 2 * (-1) ** (index + 1) * peg_positions[index]

    first_gear_radius = Fraction(2 * (
        float(gap) / 3 if even else gap
    )).limit_denominator()

    if first_gear_radius < 2:
        return default

    current_radius = first_gear_radius
    for index in range(len(peg_positions)-2):
        center_distance = peg_positions[index+1] - peg_positions[index]
        next_radius = center_distance - current_radius
        if current_radius < 1 or next_radius < 1:
            return default
        else:
            current_radius = next_radius

    return first_gear_radius.numerator, first_gear_radius.denominator

