
# Copyright (c) 2019 Guy Babineau

# here is a clue these were both entered as in appropriate habitat but blue-gray gnatcatcher was changed to observed - the aux-code was the same but the aux-code is changed
# {'speciesCode': 'whbnut', 'hideFlags': [], 'obsDt': '2017-04-02', 'subnational1Code': 'US-VA', 'howManyAtleast': 2, 'howManyAtmost': 2, 'subId': 'S35636314', 'projId': 'EBIRD_ATL_VA', 'obsId': 'OBS481168880', 'howManyStr': '2', 'present': False, 'obsAux': [{'subId': 'S35636314', 'obsId': 'OBS481168880', 'speciesCode': 'whbnut', 'fieldName': 'breeding_code', 'entryMethodCode': 'ebird_breeding', 'auxCode': 'OS', 'value': 'C2'}]}, 
# {'speciesCode': 'buggna', 'hideFlags': [], 'obsDt': '2017-04-02', 'subnational1Code': 'US-VA', 'howManyAtleast': 3, 'howManyAtmost': 3, 'subId': 'S35636314', 'projId': 'EBIRD_ATL_VA', 'obsId': 'OBS481168890', 'howManyStr': '3', 'present': False, 'obsAux': [{'subId': 'S35636314', 'obsId': 'OBS481168890', 'speciesCode': 'buggna', 'fieldName': 'breeding_code', 'entryMethodCode': 'ebird_breeding', 'auxCode': 'OS', 'value': 'C1'}]}, 

auxcode_translation = { 'auxCode':[ 'OS', 'Princi', 'Gaurav', 'Anuj'],
                        'value':[   'C1', 24, 22, 32],
                        'name':[    'H In Appropriate Habitat (Possible)', 'Kanpur', 'Allahabad', 'Kannauj']}

from ebird.api import  get_checklist

def view_checklist(ebird_api_key, checklist):
    checklist = get_checklist(ebird_api_key, 'S35636314')


    print(type(checklist)) 

    observations = checklist['obs']
    print(type(observations)) 
    for observation_dict in observations:
        #print(observation_list)
        print (len(observation_dict))
        # only look at entries with breeding codes
        if 'obsAux' in observation_dict:
            aux_dict=observation_dict['obsAux']
            print(observation_dict['speciesCode'],type(aux_dict),'->',aux_dict)


