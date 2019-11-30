"""Test the findAtlasReviewChanges package."""

import unittest
import findAtlasReviewChanges


def test_version_is_string():
    import findAtlasReviewChanges
    print (findAtlasReviewChanges.__version__)
    assert isinstance(findAtlasReviewChanges.__version__, str)


class testPackage(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        print ("setUp")

    def tearDown(self):
        """Call after every test case."""
        print ("tearDown")


    def testVersion(self):
        """Test case A. note that all test method names must begin with 'test.'"""
        assert isinstance(findAtlasReviewChanges.__version__, str)

