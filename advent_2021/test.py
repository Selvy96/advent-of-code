"""Tests the main functions"""

from main import count_bigger_numbers, count_bigger_numbers_in_threes, calculate_direction


def test_count_bigger_returns_number():
    result = count_bigger_numbers(["34", "36"])

    assert isinstance(result, int)
    assert result == 1

def test_no_bigger_nums_returns_0():
    result = count_bigger_numbers(["34", "33"])

    assert result == 0

def test_count_bigger_returns_number_for_longer_list():
    result = count_bigger_numbers(["34", "36", "54", "17", "33"])

    assert isinstance(result, int)
    assert result == 3

def test_count_bigger_in_threes_returns_correct():
    result = count_bigger_numbers_in_threes(["34", "36", "54", "17", "33", "75"])

    assert isinstance(result, int)
    assert result == 1

def test_calculate_direction_correct_result():
    result = calculate_direction(["forward 5", 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'])

    assert isinstance(result, int)
    assert result == 900