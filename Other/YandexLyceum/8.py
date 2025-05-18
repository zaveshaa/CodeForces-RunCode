import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_same_position():
    assert is_under_queen_attack("a1", "a1") is True


def test_horizontal_attack():
    assert is_under_queen_attack("a1", "d1") is True


def test_vertical_attack():
    assert is_under_queen_attack("a1", "a5") is True


def test_diagonal_attack():
    assert is_under_queen_attack("a1", "c3") is True


def test_no_attack():
    assert is_under_queen_attack("a1", "b3") is False


def test_invalid_type_first_arg():
    with pytest.raises(TypeError):
        is_under_queen_attack(123, "a1")


def test_invalid_type_second_arg():
    with pytest.raises(TypeError):
        is_under_queen_attack("a1", ["a2"])


def test_invalid_format_first_arg():
    with pytest.raises(ValueError):
        is_under_queen_attack("i9", "a1")


def test_invalid_format_second_arg():
    with pytest.raises(ValueError):
        is_under_queen_attack("a1", "j5")


def test_both_invalid_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(123, 456)


def test_order_of_checks():
    with pytest.raises(TypeError):
        is_under_queen_attack(123, "i1")
