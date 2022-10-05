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


@pytest.mark.parametrize(
    "fibonacci_function", [fib.fibonacci_iterative, fib.fibonacci_recursive]
)
def test_fibonacci(fibonacci_function, n, expected):
    assert fibonacci_function(n) == expected
