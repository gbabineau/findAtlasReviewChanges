"""Test the findAtlasReviewChanges package."""
# Copyright (c) 2019 Guy Babineau

import findAtlasReviewChanges


def test_version_is_string():
    assert isinstance(findAtlasReviewChanges.__version__, str)
