import pytest

from app import fib


pytestmark = pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144),
        (13, 233),
        pytest.param(14, 420, marks=pytest.mark.xfail),
    ],
)


def test_fibonacci_iterative(n, expected):
    assert fib.fibonacci_iterative(n) == expected


def test_fibonacci_recursive(n, expected):
    assert fib.fibonacci_recursive(n) == expected
