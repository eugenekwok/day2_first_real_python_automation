from utils.calculator import add, subtract


def test_add_two_numbers():
    result = add(2, 3)
    assert result == 5


def test_subtract_two_numbers():
    result = subtract(5, 2)
    assert result == 3