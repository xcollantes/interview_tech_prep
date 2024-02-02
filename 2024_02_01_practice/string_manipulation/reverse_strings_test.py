"""Unit test for reverse_strings.py."""

import unittest

import reverse_strings


class TestReverseStrings(unittest.TestCase):
    def test_cases(self, fn) -> None:
        """Common test cases."""
        self.assertEqual(
            fn("Sweet dreams are made of these"),
            ["these", "of", "made", "are", "dreams", "Sweet"],
        )

        self.assertEqual(fn("First second third."), ["third.", "second", "First"])
        self.assertEqual(fn(""), [""])

    def test_simple(self):

        self.test_cases(reverse_strings.reverse_words)
