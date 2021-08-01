import pytest

from google_foobar.bombs_away import solution


@pytest.mark.parametrize(
    "mach, facula, exp",
    [
        ("4", "7", "4"),
        ("2", "1", "1"),
        ("2", "4", "impossible"),
    ],
)
def test_solution(mach, facula, exp):
    actual = solution(mach, facula)
    assert actual == exp
