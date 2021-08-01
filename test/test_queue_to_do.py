import pytest

from google_foobar.queue_to_do import solution


@pytest.mark.parametrize(
    "start, length, expected", [(0, 3, 2), (17, 4, 14), (0, 50000, 2364908544)]
)
def test_solution(start, length, expected):
    actual = solution(start, length)

    assert actual == expected
