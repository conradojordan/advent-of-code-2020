from solutions.day1 import solve
import os


def test_part1_and_2():
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "inputs", "day1_example.txt")

    with open(file_path) as f:
        entries = [int(entry) for entry in f.read().strip().split()]

    a, b = solve(entries, 2)
    assert a * b == 514579

    a, b, c = solve(entries, 3)
    assert a * b * c == 241861950
