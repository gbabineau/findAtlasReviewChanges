
# Copyright (c) 2019 Guy Babineau

# here is a clue these were both entered as in appropriate habitat but blue-gray gnatcatcher was expect to observed - the aux-code was the same but the aux-code is expect
# {'speciesCode': 'whbnut', 'hideFlags': [], 'obsDt': '2017-04-02', 'subnational1Code': 'US-VA', 'howManyAtleast': 2, 'howManyAtmost': 2, 'subId': 'S35636314', 'projId': 'EBIRD_ATL_VA', 'obsId': 'OBS481168880', 'howManyStr': '2', 'present': False, 'obsAux': [{'subId': 'S35636314', 'obsId': 'OBS481168880', 'speciesCode': 'whbnut', 'fieldName': 'breeding_code', 'entryMethodCode': 'ebird_breeding', 'auxCode': 'OS', 'value': 'C2'}]}, 
# {'speciesCode': 'buggna', 'hideFlags': [], 'obsDt': '2017-04-02', 'subnational1Code': 'US-VA', 'howManyAtleast': 3, 'howManyAtmost': 3, 'subId': 'S35636314', 'projId': 'EBIRD_ATL_VA', 'obsId': 'OBS481168890', 'howManyStr': '3', 'present': False, 'obsAux': [{'subId': 'S35636314', 'obsId': 'OBS481168890', 'speciesCode': 'buggna', 'fieldName': 'breeding_code', 'entryMethodCode': 'ebird_breeding', 'auxCode': 'OS', 'value': 'C1'}]}, 

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


