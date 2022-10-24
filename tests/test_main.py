from main import isLeapYear

def test_year_divided_by_four_and_not_one_hundred_is_not_zero():
    assert isLeapYear(2104) == False

def test_year_divided_by_four_hundred_is_zero():
    assert isLeapYear(2104) == True

def test_year_divided_by_four_and_not_one_hundred_is_zero():
    assert isLeapYear(2105) == False

def test_year_divided_by_four_hundred_is_not_zero():
    assert isLeapYear(2105) == False

