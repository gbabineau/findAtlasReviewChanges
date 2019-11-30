# Copyright (c) 2019 Guy Babineau

# relies on the ebird api key to be in the environment variable EBIRDAPIKEY or speficed on command line
# this key can be obtained from https://ebird.org/api/keygen
# do not abuse the key or it will be revoked

# example command line: python find_reviewer_changes.py --user "Guy Babineau" --area "US-VA-003" --date "2018-04-08"

import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Find ebird Atlas reviewer changes.')
parser.add_argument('--version', action='version', version='%(prog)s 0.0.0')
parser.add_argument('--verbose', action='store_true', help='increase verbosity')
parser.add_argument('--user',  required=True, help='User name in quote e.g. --user "Guy Babineau"')
parser.add_argument('--area',  required=True, help='Country, Region, Subregion to look for lists e.g. --area "US-VA-003"')
parser.add_argument('--key',  default="read environment", help='--key "<obtain secret text"')
parser.add_argument('--date',  required=True, help='Date to start e.g. --date "2018-04-08"')
parser.add_argument('--end',  default="one day", help='Date to end e.g. --end "2018-04-12"')
parser.add_argument('--max_records',  default=50, help='Maximum records to pull at once from ebird.org e.g. --max_records 70')


args=parser.parse_args()
ebird_api_key_name='EBIRDAPIKEY'

if (args.key == "read environment"):
    ebird_api_key= os.getenv(ebird_api_key_name)
    if ebird_api_key=='0':
        sys.exit("ebird API key must be specified on command line or in the "+ebird_api_key_name+" environment variable.")
else:
    ebird_api_key=args.key


from ebird.api import  get_visits, get_totals
import datetime
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
    print("")

auxcode_translation =   { 
                        'FO' : {'C value' : 'C1' , 'readable' : 'F Flyover (Observed)'},
                        'OS' : {'C value' : 'C2' , 'readable' : 'H In Appropriate Habitat (Possible)'},
                        'S1' : {'C value' : 'C2' , 'readable' : 'S Singing Male (Possible)'},
                        'S7' : {'C value' : 'C3' , 'readable' : 'S7 Singing Male Present 7+ days (Probable)'},
                        'PO' : {'C value' : 'C3' , 'readable' : 'P Pair in Suitable Habitat (Probable)'},
                        'AB' : {'C value' : 'C3' , 'readable' : 'A Agitated Behavior (Probable)'},
                        'T7' : {'C value' : 'C3' , 'readable' : 'T Territorial Defense (Probable)'},
                        'CC' : {'C value' : 'C3' , 'readable' : 'C Courtship, Display, or Copulation (Probable)'},
                        'VS' : {'C value' : 'C3' , 'readable' : 'N Visiting Probable Nest Site (Probable)'},
                        'NB' : {'C value' : 'C4' , 'readable' : 'NB Nest Building (Confirmed)'},
                        'CM' : {'C value' : 'C4' , 'readable' : 'CN Carrying Nesting Material (Confirmed)'},
                        'FY' : {'C value' : 'C4' , 'readable' : 'CF Carrying Food (Confirmed)'},
                        'UN' : {'C value' : 'C4' , 'readable' : 'UN Used Nest (enter 0 if no birds seen) (Confirmed)'},
                        'ON' : {'C value' : 'C4' , 'readable' : 'ON Occupied Nest (Confirmed)'},
                        'FL' : {'C value' : 'C4' , 'readable' : 'FL Recently Fledged Young (Confirmed)'},
                        'FR' : {'C value' : 'C4' , 'readable' : 'FY Feeding Young (Confirmed)'},
                        'NE' : {'C value' : 'C4' , 'readable' : 'NE Nest with Eggs (Confirmed)'},
                        'NY' : {'C value' : 'C4' , 'readable' : 'NY Nest with Young (Confirmed)'}
                        }

value_translation =     {
                        'C1'    : 'Observed',
                        'C2'    : 'Possible',
                        'C3'    : 'Probable',
                        'C4'    : 'Confirmed'
                        }


from ebird.api import  get_checklist

def review_checklist(ebird_api_key, checklist_name):
    checklist = get_checklist(ebird_api_key, checklist_name)

    observations = checklist['obs']
    for observation_dict in observations:
        # only look at entries with breeding codes
        if 'obsAux' in observation_dict:
            aux_dict=observation_dict['obsAux'][0]
            entered_code= aux_dict['auxCode']
            if  entered_code in auxcode_translation.keys():
                issue_code=aux_dict['value']
                expect_code= auxcode_translation[entered_code]['C value']
                if issue_code != expect_code:
                    print(observation_dict['speciesCode'],' Changed to ', value_translation[issue_code],' from ',auxcode_translation[entered_code]['readable'])
            else:
                print ("auxcode not found:", entered_code)



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

