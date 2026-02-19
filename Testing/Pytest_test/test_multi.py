# Using pytest
# -----------------------------------------
# The following example is equivalent to TestCases in unittest

import pytest 
from multiplication import addition, sqrt

def test_addition():
    assert addition(34, 5) > 3
    assert addition(54, "6") == 60
    assert addition(-1, 25) == 50

# Exception Handling
def test_sqrt():
    # Expecting a valueError to be raised from the tested script.
    # If not, test fails
    # You can check for TypeError, KeyError, ZeroDivisionError
    with pytest.raises(ValueError):
        sqrt("Catch this error")