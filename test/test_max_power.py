import pytest

from max_power import *


@pytest.mark.parametrize(
    "inp, exp",
    [
        ([2, 0, 2, 2, 0], "8"),
        ([-2, -3, 4, -5], "60"),

        ([-2], "-2"),
        ([-12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "0"),


        ([2, -3, 1, 0, -5], "30"),
        ([99, -1], "99"),
        ([1, 2, 3, 4, 5, -1, -2], "240"),
        ([99], "99"),
        ([-2, -3, -4, -1], "24"),
        ([-2, 1, 1, 2, -2], "8"),
        ([-2, 1, 1, -2, 1, 1, -2], "4"),
    ],
)
def test_solution(inp, exp):
    actual = solution(inp)
    assert actual == exp
