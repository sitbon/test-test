"""A simple function.
"""


def print_hi(name1, name2):
    if not name1 or not name2:
        raise ValueError("name1 and name2 must not be empty")

    print(f"Hi, {name1} & {name2}!")
