"""Test the findAtlasReviewChanges package."""

import unittest
import findAtlasReviewChanges


def test_version_is_string():
    print(findAtlasReviewChanges.__version__)
    assert isinstance(findAtlasReviewChanges.__version__, str)


class testPackage(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        print("setUp")

    def tearDown(self):
        """Call after every test case."""
        print("tearDown")

    def testVersion(self):
        """Make sure that there is a version"""
        assert isinstance(findAtlasReviewChanges.__version__, str)

    def testPass(self):
        """Run a test that passes"""
        assert (1 == 1)
