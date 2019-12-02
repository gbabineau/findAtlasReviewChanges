"""Unit test of the review_visits function."""
# Copyright (c) 2019 Guy Babineau

import os
import datetime
from dateutil import parser
from findAtlasReviewChanges import review_visits


def test_review_visits(capsys):
    ebird_api_key = os.getenv('EBIRDAPIKEY')
    assert(len(ebird_api_key) == 12)
    day = parser.parse('2018-04-08')
    end_day = day + datetime.timedelta(days=1)
    review_visits(ebird_api_key, 'Guy Babineau', 'US-VA-003', day, end_day, 30, True)
    captured = capsys.readouterr()
    assert ("Chris Greene" in captured.out)
