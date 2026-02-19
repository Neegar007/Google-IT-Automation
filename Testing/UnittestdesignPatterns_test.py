#!/usr/bin/venv python3


# Unit test Design Pattern: Arrange, Act, Assert
# Arrange: set up the conditions for the test
# Act: execute the code being tested
# Assert: verify that the code behaved as expected
# -------------- Example -------------------------
# Imagine building a system for a library. 
# The objective is to test whether a new book can be added to
# the library's collection and then to check if the book 
# is in the collection. Using the above structure of 
# arrange, act, and assert, consider the following example code:

# What’s given (arrange): A library with a collection of books

# When to test (act): A new book is added to the collection

# Then check (assert): The new book should be present in the library's
# collection

import unittest


class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)

    def has_book(self, book):
        return book in self.collection

# -------------- Unit Test For The Library System -------------

class TestLibrary:
    def test_add_book_to_library(self):
        # Arrange
        library = Library()
        new_book = "Python Design Patterns"

        # Act
        library.add_book(new_book)

        # Assert
        self.assertTrue(library.has_book(new_book))

# Run the tests

library_test_output = unittest.TextTestRunner().run(unittest.TestLoader.loadTestsFromTestCase(TestLibrary))
print(library_test_output)