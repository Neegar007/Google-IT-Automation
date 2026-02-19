#!/usr/bin/venv python 3

# Paramerized Values
"""
Parametrization is a pytest feature that allows you to run a test 
function with different sets of data at once.

For example: Let’s say you have a function that calculates 
the square of a number. To provide enough coverage while testing, 
you would want to test the function with zero, positive, 
and negative numbers.

Instead of writing separate test functions for each scenario, 
you can use parametrization to run a test function with different 
sets of data at once. This approach is more concise, and reduces 
code duplication.

To use parametrization in pytest, we use the @pytest.mark.parametrize
 decorator as shown in the example below:
"""

import pytest

# Function to return the square of a number. 
def square(num):
    return num * num

#Parametrize decorator to test the square 
# function with different inputs

@pytest.mark.parametrize("input_value, expected_output", [
    (2, 4),     
    (-3, 9),    
    (5, 0)    
])
def test_square(input_value, expected_output):
    assert square(input_value) == expected_output