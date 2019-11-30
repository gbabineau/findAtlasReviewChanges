# Copyright (c) 2019 Guy Babineau

# relies on the ebird api key to be in the environment variable EBIRDAPIKEY or speficed on command line
# this key can be obtained from https://ebird.org/api/keygen
# do not abuse the key or it will be revoked

# example command line below
# python findAtlasReviewChanges --user "Guy Babineau" --area "US-VA-003" --date "2018-04-01" --end "2018-04-14"

import os
import sys
import argparse
from ebird.api import get_visits
import datetime
from time import sleep
from .review_checklist import review_checklist
from dateutil import parser


arg_parser = argparse.ArgumentParser(description='Find ebird Atlas reviewer changes.')
arg_parser.add_argument('--version', action='version', version='%(prog)s 0.0.3')
arg_parser.add_argument('--verbose', action='store_true', help='increase verbosity')
arg_parser.add_argument('--user',  required=True, help='User name in quote e.g. --user "Guy Babineau"')
arg_parser.add_argument('--area',  required=True, help='Country, Region, Subregion to look for lists e.g. --area "US-VA-003"')
arg_parser.add_argument('--key',  default="read environment", help='--key "<obtain secret text"')
arg_parser.add_argument('--date',  required=True, help='Date to start e.g. --date "2018-04-08"')
arg_parser.add_argument('--end',  default="one day", help='Date to end e.g. --end "2018-04-12"')
arg_parser.add_argument('--max_records',  default=50,
                        help='Maximum records to pull at once from ebird.org e.g. --max_records 70')


args = arg_parser.parse_args()
ebird_api_key_name = 'EBIRDAPIKEY'

if (args.key == "read environment"):
    ebird_api_key = os.getenv(ebird_api_key_name)
    if ebird_api_key == '0':
        sys.exit("ebird API key must be specified on command line or in the "+ebird_api_key_name+" environment variable.")
else:
    ebird_api_key = args.key


area = args.area
user = args.user


day = parser.parse(args.date)

if (args.end == 'one day'):
    end_day = day + datetime.timedelta(days=1)
else:
    end_day = parser.parse(args.end)

area = args.area
max_records = args.max_records

if (args.verbose):
    print("User:       ", user)
    print("Area:       ", area)
    print("Date:       ", day)
    print("End:        ", end_day)
    if args.key == "read environment":
        print("Key:         Specified on command line")
    else:
        print("Key:         Read from Environment Variable EBIRDAPIKEY")
    print("")


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
