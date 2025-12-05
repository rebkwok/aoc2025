import pytest

from solutions.day5 import collapse_ranges


@pytest.mark.parametrize(
    "input,expected",
    [
        (
            [(2, 4), (4, 7)],
            [(2, 7)]
        ),
        (
            # allow for ranges that are entirely contained within another range
            [(3, 5), (2, 6), (8, 11)],
            [(2, 6), (8, 11)]
        ),

    ]
)
def test_collapse_ranges(input, expected):
    assert collapse_ranges(input) == expected