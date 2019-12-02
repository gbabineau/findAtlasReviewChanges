"""Unit test of the review_checklists function."""
# Copyright (c) 2019 Guy Babineau

import os
from findAtlasReviewChanges import review_checklist


def test_review_checklist(capsys):
    ebird_api_key = os.getenv('EBIRDAPIKEY')
    assert(len(ebird_api_key) == 12)
    review_checklist(ebird_api_key, 'S35636314')
    captured = capsys.readouterr()
    assert ("cangoo" in captured.out)
