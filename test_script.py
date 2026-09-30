from script import check_age
import pytest

def test_check_age():
    assert check_age('2012-01-01') == "Denied access, need to be 16, but are 14"
    assert check_age('1994-02-02') == "Access granted"
    assert check_age('2010-12-6') == "Denied access, need to be 16, but are 15"
    assert check_age('2010-10-31') == "Denied access, need to be 16, but are 15"
    with pytest.raises(Exception) as e:
        check_age(2010)
    assert "Incorrect data" in str(e.value)
