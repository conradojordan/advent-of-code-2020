import os
from typing import List, Tuple


def parse_pattern_and_password(pattern_and_password: str) -> Tuple:
    pattern, password = pattern_and_password.split(":")
    password = password.strip()
    numbers, character = pattern.split()
    first_number, second_number = numbers.split("-")
    return int(first_number), int(second_number), character, password


def is_valid_part_1(pattern_and_password: str) -> bool:
    min_count, max_count, character, password = parse_pattern_and_password(pattern_and_password)
    return min_count <= password.count(character) <= max_count


def is_valid_part_2(pattern_and_password: str) -> bool:
    first_position, second_position, character, password = parse_pattern_and_password(pattern_and_password)
    return (password[first_position - 1] == character) != (password[second_position - 1] == character)


def count_valid_passwords(passwords: List[str], algorithm: int = 1) -> int:
    valid_passwords_count = 0
    for password in passwords:
        if algorithm == 1:
            if is_valid_part_1(password):
                valid_passwords_count += 1
        elif algorithm == 2:
            if is_valid_part_2(password):
                valid_passwords_count += 1
    return valid_passwords_count


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "inputs", "day2.txt")

    with open(file_path) as f:
        passwords = f.read()

    # Part 1
    print(" Part 1 ".center(30, "-"))
    passwords = passwords.strip().split("\n")
    valid_passwords_count = count_valid_passwords(passwords, 1)
    print(f"There are a total of {valid_passwords_count} valid passwords using the firt algorithm.")

    # Part 2
    print(" Part 2 ".center(30, "-"))
    valid_passwords_count = count_valid_passwords(passwords, 2)
    print(f"There are a total of {valid_passwords_count} valid passwords using the second algorithm.")
