"""Test the findAtlasReviewChanges package."""

import findAtlasReviewChanges
import os
from  findAtlasReviewChanges import review_checklist
from  findAtlasReviewChanges import review_visits

def test_version_is_string():
    assert isinstance(findAtlasReviewChanges.__version__, str)


def test_CLI_version(capsys):
    ebird_api_key = os.getenv('EBIRDAPIKEY')
    assert(len(ebird_api_key)==12)
    review_checklist(ebird_api_key, 'S35636314')
    captured = capsys.readouterr()
    assert ("cangoo" in captured.out)
