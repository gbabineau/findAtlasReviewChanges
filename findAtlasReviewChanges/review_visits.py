from .review_checklist import review_checklist
from ebird.api import get_visits
import sys
from time import sleep
import datetime


def review_visits(ebird_api_key, user, area, day, end_day, max_records, verbose):
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
        sleep(2)
        day += datetime.timedelta(days=1)
