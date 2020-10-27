"""Test for the core.py program."""

import unittest

from Python_practice.smartsquare import square

class TestCore(unittest.TestCase):
    """Test methods class."""

    def test_float(self):
        """Square test."""
        self.assertAlmostEqual(square(2.), 4.)

if __name__ == "__main__":
    unittest.main()
