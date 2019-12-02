"""Reviews visits in an area for checklists from a user and then checks the checklist."""

# Copyright (c) 2019 Guy Babineau

from .review_checklist import review_checklist
from ebird.api import get_visits
import sys
from time import sleep
import datetime


def review_visits(ebird_api_key, user, area, day, end_day, max_records, verbose):
    """Checks up to max_records checklists from an area between day and end_day

    According to eBird, this API should not be abused so limit size of data
    retrieved. It has a built in delay to help with this.

    Args
        ebird_api_key : access key from eBird tied to account
        user          : eBird user name (not id)
        area          : ebird region eg. Country-State-County = US-VA-003 for Albemarle County, Virginia, USA
        day           : day to start looking -e.g. 2018-04-08
        end_day       : day to end looking - e.g. 2018-04-15
        max_records   : maximum records to request from eBird
        verbose       : whether to print out additional information


    Returns:
        NA - prints to stdout

    Raises:
        NA - but can exit on max-records
    """

    while day < end_day:
        day_string = day.strftime("%Y-%m-%d")
        records = get_visits(ebird_api_key, area, day_string, max_records)
        if len(records) == max_records:
            sys.exit("Error: got max_records(" + str(max_records) + ") in " + area + " on " + day_string
                     + " - use a smaller area or larger max_records")

        for record in records:
            #
            # ensure it is not anonymous and it is the user we are looking for
            #

            if 'userDisplayName' in record.keys():
                if (record['userDisplayName'] == user):
                    print("Reviewing Checklist from ", day_string, record['loc']['name'])
                    review_checklist(ebird_api_key, record['subId'])
        #
        # Limit get_visit calls to eBird to once every two seconds
        #
        sleep(2)
        day += datetime.timedelta(days=1)
