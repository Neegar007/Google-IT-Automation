#!/usr/bin/venv python3

# Pytest markers
"""
When working with a large codebase, sometimes running every single test
 can be time-consuming. This is where pytest markers come in handy.

A marker is just like a label that you can attach to a test function 
to categorise it. Once a test is labelled, you can instruct pytest to 
run only tests with certain markers. For example, you may label some 
tests as "slow" if they take longer to execute and run them separately
 from the faster ones.

One advantage to using Markers is that it allows you to run specific 
tests based on categories or specific parameters, and also skip tests 
if certain conditions aren’t met.

pytest comes along with some built-in markers that can be quite useful:

1. @pytest.mark.skip: This marker allows you to skip a test entirely.
  This marker allows you to skip a test unconditionally, and can be 
  useful when you know a test will fail due to an external issue or 
  incomplete code.
2. @pytest.mark.skipif: This marker allows you to skip a test based.
    on a condition. For example, you might want to skip a test if a
    certain library isn’t installed or if the operating system is not
    compatible.
3. @pytest.mark.xfail: This marker is used to indicate that a test is
    expected to fail. This can be useful when you have a known bug in
    your code that you plan to fix later, but you still want to keep
    the test in your suite.
--CUSTOM MARKERS--
https://docs.pytest.org/en/stable/example/markers.html
You can also create your own custom markers to categorise tests based
on your specific needs. For example, you might create markers for
"database tests", "API tests", or "UI tests".
Your custom markers need to be registered in pytest.ini file to avoid
warnings.
Here's an example of how to register these markers in your test code:
# pytest.ini
[pytest]
markers =
    custom_marker: mark test as part of custom group

# Programatically, you can use register markers as follows:
import pytest
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark a test as a smoke test."
    )
    config.addinivalue_line(
        "markers", "integration: mark a test as an integration test."
    )
You run custom marked tests using the -m option:
pytest -m "custom_marker"

"""
import pytest
import sys
from multiplication import addition

@pytest.mark.skip(reason="Skipping this test unconditionally.")
def test_unconditional_skip():
    assert addition(5, 2) == 3

@pytest.mark.skipif(sys.platform == "win32", reason="Skipping test on Windows OS.")
def test_skip_on_windows():
    assert addition(10, 5) == 15 # This test will be skipped on Windows systems

@pytest.mark.xfail(reason="This test is expected to fail.")
def test_expected_failure():
    assert addition(3, 4) == 10  # This test is expected to fail

@pytest.mark.custom_marker
def test_custom_marker():
    assert addition(7, 8) == 15  # This test is marked with a custom marker