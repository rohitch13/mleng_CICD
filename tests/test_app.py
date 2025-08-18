# Run the tests with: pytest tests/test_app.py
"""
Unit test:

"""

from app import add_numbers

def test_add_numbers():
    """
    Testing add_numbers function
    """
    assert 3 == add_numbers(1,2)
