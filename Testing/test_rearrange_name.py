#!/usr/bin/env python3

import unittest
# Import the function to be tested
from rearrange_name import rearrange_name

# Define the test case class
class TestRearrangeName(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

# Run the tests
unittest.main()


