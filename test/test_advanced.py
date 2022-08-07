# -*- coding: utf-8 -*-

from .context import sample # Notice the '.'.

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())


if __name__ == '__main__':
    unittest.main()

# This (https://stackoverflow.com/questions/39134718/how-to-add-a-package-to-sys-path-for-testing) was useful for getting this to work.
# To run this from command line, run the following:
# python3 -m unittest test.test_advanced