# -*- coding: utf-8 -*-

from .context import sample # Notice the '.'.

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()

# This (https://stackoverflow.com/questions/39134718/how-to-add-a-package-to-sys-path-for-testing) was useful for getting this to work.
# To run this from command line, run the following:
# python3 -m unittest test.test_basic