def fizzbuzz(n):
    """Return the nth fizzbuzz number"""
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return str(n)


def fizzbuzz_list(n):
    """Return a list of the first n fizzbuzz numbers"""
    return [fizzbuzz(i) for i in range(1, n + 1)]


def fizzbuzz_list_short(n):
    return list(
        map(
            lambda i: f"{'Fizz' * (not i % 3)}{'Buzz' * (not i % 5)}" or str(i),
            range(1, n + 1),
        )
    )
