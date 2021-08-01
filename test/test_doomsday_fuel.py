from fractions import Fraction, gcd

import pytest

from google_foobar.doomsday_fuel import solution


@pytest.mark.parametrize(
    "m, expected",
    [
        (
            [
                [0, 2, 1, 0, 0],
                [0, 0, 0, 3, 4],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            [7, 6, 8, 21],
        ),
        (
            [
                [0, 1, 0, 0, 0, 1],
                [4, 0, 0, 3, 2, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ],
            [0, 3, 2, 9, 14],
        ),
        (
            [
                [0, 0, 0],
            ],
            [1, 1],
        ),
    ],
)
def test_solution(m, expected):
    actual = solution(m)

    assert actual == expected


@pytest.mark.parametrize(
    "res, exp",
    [
        [
            [
                [Fraction(1, 6), Fraction(1, 5), Fraction(1, 5)],
                [Fraction(1, 5), Fraction(1, 5), Fraction(1, 5)],
            ],
            30,
        ],
        [
            [
                [Fraction(1, 3), Fraction(2, 7), Fraction(8, 21)],
                [Fraction(0, 1), Fraction(3, 7), Fraction(4, 7)],
            ],
            21,
        ],
        [
            [
                [Fraction(0, 1), Fraction(3, 14), Fraction(1, 7), Fraction(9, 14)],
                [Fraction(0, 1), Fraction(3, 7), Fraction(2, 7), Fraction(2, 7)],
            ],
            14,
        ],
    ],
)
def test_foo(res, exp):
    p = reduce(lambda p, d: p * d.denominator / gcd(p, d.denominator), res[0], 1)
    l = 1
    for item in res[0]:
        l *= item.denominator / gcd(l, item.denominator)
    assert p == l == exp
