"""Test the findAtlasReviewChanges package."""

import findAtlasReviewChanges


def test_version_is_string():
    print(findAtlasReviewChanges.__version__)
    assert isinstance(findAtlasReviewChanges.__version__, str)


def test_CLI_version():
    assert isinstance(1 == 1)
