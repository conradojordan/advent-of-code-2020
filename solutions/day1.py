import os
import itertools
from typing import List, Tuple


def solve(entries: List[int], combination_size) -> Tuple:
    for combination in itertools.combinations(entries, combination_size):
        if sum(combination) == 2020:
            return combination
    return (0,) * combination_size


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "inputs", "day1.txt")

    with open(file_path) as f:
        entries = [int(entry) for entry in f.read().strip().split()]

    # Part 1
    a, b = solve(entries, 2)
    print(" Part 1 ".center(30, "-"))
    print(f"The numbers whose sum is 2020 are: {a} and {b}")
    print(f"Their multiplication is {a*b}\n")

    # Part 2
    a, b, c = solve(entries, 3)
    print(" Part 2 ".center(30, "-"))
    print(f"The numbers whose sum is 2020 are: {a}, {b} and {c}")
    print(f"Their multiplication is {a*b*c}")
