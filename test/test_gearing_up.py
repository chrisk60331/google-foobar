import pytest

from google_foobar.gearing_up import *


@pytest.mark.parametrize(
    "inp, exp",
    [
        ([4, 30, 50], (12, 1)),
        ([4, 30, -30, -50], (-1, -1)),
        ([4], (-1, -1)),
        ([4, 30, 50, 62], (12, 1)),
        ([4, 17, 50], (-1, -1)),
        ([4, 30, 50], (12, 1)),
        ([4, 17, 50], (-1, -1)),
        ([1, 51], (100, 3)),
        ([1, 31], (20, 1)),
        ([1, 31, 51, 71], (20, 1)),
        ([1, 31, 51, 71, 91], (20, 1)),
        ([4, 9, 17, 31, 40], (4, 1)),
    ],
)
def test_solution(inp, exp):
    actual = solution(inp)

    assert actual == exp
