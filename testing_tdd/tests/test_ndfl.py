import pytest

from ndfl.calculator import calculate_tax


@pytest.mark.parametrize("income, expected", [
    (0, 0),
    (200_000, 26_000),
    (2_400_000, 312_000),
    (3_000_000, 402_000),
    (5_000_000, 702_000),
    (20_000_000, 3_402_000),
    (50_000_000, 9_402_000),
    (60_000_000, 11_602_000),
])
def test_all_brackets(income, expected):
    assert calculate_tax(income) == expected


def test_integrity():
    assert calculate_tax(2_400_001) > calculate_tax(2_400_000)


def test_negative():
    with pytest.raises(ValueError):
        calculate_tax(-1)
