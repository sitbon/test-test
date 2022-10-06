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
