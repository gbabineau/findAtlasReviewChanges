# relies on the ebird api key to be in the environment variable EBIRDAPIKEY
# this key can be obtained from https://ebird.org/api/keygen
# do not abuse the key or it will be revoked

import os

import argparse

parser = argparse.ArgumentParser(description='Find ebird Atlas reviewer changes.')
parser.add_argument('--version', action='version', version='%(prog)s 0.0.0')
parser.add_argument('--verbose', action='store_true', help='increase verbosity')
parser.add_argument('--user',  required=True, help='User name in quote e.g. --user "Guy Babineau"')
parser.add_argument('--area',  required=True, help='Country, Region, Subregion to look for lists e.g. --region "US-VA-003"')
parser.add_argument('--key',  default="read environment", help='--key "<obtain secret text"')
parser.add_argument('--date',  required=True, help='Date to start e.g. --date "2018-04-08"')
parser.add_argument('--end',  default="one day", help='Date to end e.g. --end "2018-04-12"')
parser.add_argument('--max_records',  default=50, help='Maximum records to pull at once from ebird.org e.g. --max_records 70')


args=parser.parse_args()

if (args.key == "read environment"):
    ebird_api_key= os.getenv('EBIRDAPIKEY')
else:
    ebird_api_key=args.key


from ebird.api import  get_visits, get_totals
import datetime
import sys
from time import sleep

area=args.area 
user=args.user

from dateutil import parser

day = parser.parse(args.date)


if (args.end == 'one day'):
    end_day= day+ datetime.timedelta(days=1)
else:
    end_day=parser.parse(args.end)

area = args.area
max_records=args.max_records

if (args.verbose):
    print ("User:       ", user)
    print ("Area:       ", area)
    print ("Date:       ", day)
    print ("End:        ", end_day)
    if args.key == "read environment":
        print ("Key:         Specified on command line")
    else:
        print ("Key:         Read from Environment Variable EBIRDAPIKEY")



from src.review_checklist import review_checklist

while day < end_day:
    day_string=day.strftime("%Y-%m-%d")
    #totals = get_totals(ebird_api_key, area, day_string)
    records=get_visits(ebird_api_key, area, day_string, max_records)
    if len(records) ==max_records:
        sys.exit("Error: got max_records("+str(max_records)+") in "+area+" on "+day_string+" - use a smaller area or larger max_records")

    for record in records:
        #ensure it is not anonymous and it is the user we are looking for
        if 'userDisplayName' in record.keys():
            if (record['userDisplayName']==user):
                print ("Reviewing Checklist from ", day_string, record['loc']['name'])    
                review_checklist(ebird_api_key,record['subId'])
    sleep (2)
    day+= datetime.timedelta(days=1)

