from solutions.day2 import is_valid_part_1, is_valid_part_2, parse_pattern_and_password, count_valid_passwords


def test_is_valid_part_1():
    assert is_valid_part_1("1-3 a: abcde") == True
    assert is_valid_part_1("1-3 b: cdefg") == False
    assert is_valid_part_1("2-9 c: ccccccccc") == True


def test_is_valid_part_2():
    assert is_valid_part_2("1-3 a: abcde") == True
    assert is_valid_part_2("1-3 b: cdefg") == False
    assert is_valid_part_2("2-9 c: ccccccccc") == False


def test_parse_pattern_and_password():
    assert parse_pattern_and_password("1-3 a: abcde") == (1, 3, "a", "abcde")
    assert parse_pattern_and_password("2-9 c: ccccccccc") == (2, 9, "c", "ccccccccc")


def test_count_valid_passwords_part1_and_2():
    assert count_valid_passwords(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"], 1) == 2
    assert count_valid_passwords(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"], 2) == 1
