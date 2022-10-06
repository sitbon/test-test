import pytest

from app import fizzbuzz


fizzbuzz_test_data = [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (4, "4"),
    (5, "Buzz"),
    (6, "Fizz"),
    (7, "7"),
    (8, "8"),
    (9, "Fizz"),
    (10, "Buzz"),
    (11, "11"),
    (12, "Fizz"),
    (13, "13"),
    (14, "14"),
    (15, "FizzBuzz"),
    (16, "16"),
    (17, "17"),
    (18, "Fizz"),
    (19, "19"),
    (20, "Buzz"),
]


@pytest.mark.parametrize("n, expected", fizzbuzz_test_data)
def test_fizzbuzz_single(n, expected):
    assert fizzbuzz.fizzbuzz(n) == expected


@pytest.mark.parametrize("n", list(range(1, len(fizzbuzz_test_data) + 1)))
@pytest.mark.parametrize(
    "fizzbuzz_list_fn", [fizzbuzz.fizzbuzz_list, fizzbuzz.fizzbuzz_list_short]
)
def test_fizzbuzz_list(fizzbuzz_list_fn, n):
    assert fizzbuzz_list_fn(n) == [i[1] for i in fizzbuzz_test_data[:n]]
