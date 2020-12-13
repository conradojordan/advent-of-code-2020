from solutions.day1 import solve
from os import path


def test_part1_and_2():
    file_path = path.join("..", "inputs", "day1_example.txt")

    with open(file_path) as f:
        entries = [int(entry) for entry in f.read().strip().split()]

    a, b = solve(entries, 2)
    assert a * b == 514579

    a, b, c = solve(entries, 3)
    assert a * b * c == 241861950
