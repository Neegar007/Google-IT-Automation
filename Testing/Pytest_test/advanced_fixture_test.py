#!/usr/bin/env python3

# Advanced Fixture Usage in Pytest
"""
fixtures allow you to create reusable default data that can be 
shared across multiple tests. By using fixtures, you can reduce 
code repetition, making your tests cleaner and more maintainable.

In pytest, fixtures are defined with the @pytest.fixture decorator
as shown in the example below:

Let’s say we have several tests that rely on a list of user data.
Instead of repeating the same data in each test, we can create a 
fixture to hold this data, and the fixture is passed across the tests
 that need it.
"""

import pytest 

@pytest.fixture
def user_data():
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]

# Test function to check for a specific user by name and age
def test_user_exists(user_data):
    user = {"name": "Alice", "age": 30}

    # Check if the target user is in the list
    assert user in user_data

# Test average age of users
def test_average_age(user_data):
    ages = [user["age"] for user in user_data]
    avg_age = sum(ages) / len(ages)
    assert avg_age == 30