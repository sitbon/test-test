def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("n must be >= 0")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_recursive(n):
    if n <= 1:
        if n < 0:
            raise ValueError("n must be >= 0")

        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
