# reviewVABBA2data

Version 0.0.0

## Installing

You will need to install Python.

```batch
pip install ebird-api
pip install python-dateutil
```

## Using

Warning, misuse of this utility can place a large demand on ebird.org servers which has a performance and cost impact on others and is not needed. You will be making the requests to ebird.org via a token you request from ebird.org using your ebird login credentials. According to ebird.org misuse of your key to access large amounts of data could result in ebird.org revoking your ability to access the data.

Request your key from [here](https://ebird.org/api/keygen). One you get it, save it as you will need it later.

### Optional - save your ebird api key in an environment variable

You can save your api key in an environment variable called EBIRDAPIKEY. If you don't know how, that's ok, you can still use it on the command line. This is done to prevent the api key being shared accidentally in example scripts created for the documentation.

## Developer Notes

This relies on functionality based on [eBird API 2.0](https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest).

Coding was greatly simplified using these [useful Python access functions](https://github.com/ProjectBabbler/ebird-api).

Unfortunately, there do not appear to be public API calls which let you obtain checklists by user. So it gets checklist from an area (e.g. county) and scans for ones from a particular user.

Then it goes through the checklist to see if breeding codes were changed from what was entered. Some codes were obtained via examination of the returns of the API calls.

[Contributing](CONTRIBUTING.md)

[License](LICENSE.md)
