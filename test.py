# relies on the ebird api key to be in the environment variable EBIRDAPIKEY
# this key can be obtained from https://ebird.org/api/keygen
# do not abuse the key or it will be revoked

import os
from ebird.api import  get_checklist

ebird_api_key= os.getenv('EBIRDAPIKEY')



# here is a checklist with an issue https://ebird.org/atlasva/checklist/S35636314

#checklist = get_checklist(ebird_api_key, 'S35636314')
#print (checklist)

from src.view_checklist import view_checklist

view_checklist(ebird_api_key,'S35636314')

