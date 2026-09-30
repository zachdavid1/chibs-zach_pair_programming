# {{PROBLEM}} Function Design Recipe



## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

## 2. Design the Function Signature

def check_age(dob):
    # return: message -> "Denied access, needs to be {required}, but are {current age} -> "Access granted"


## 3. Create Examples as Tests

def test_check_age():
    assert check_age('2012-01-01') == "Denied access, need to be 16, but are 14"
    assert('1994-02-02') == "Access granted"
    assert check_age('2010-12-6') == "Denied access, need to be 16, but are 15"
    assert check_age('2010-10-31) == "Denied access, need to be 16, but are 15"
    with pytest.raises(Exception) as e:
        check_age(2010)
    assert "Incorrect data" in str(e.value)
