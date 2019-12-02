# findAtlasReviewChanges

Version 0.0.4

![Application](https://github.com/gbabineau/findAtlasReviewChanges/workflows/Python%20application/badge.svg) ![Labler](https://github.com/gbabineau/findAtlasReviewChanges/workflows/Labeler/badge.svg)

## Installing

This requires some knowledge of working with command lines on your computer.

1. You will need to install Python.

1. Download the latest [WHL file](https://github.com/gbabineau/findAtlasReviewChanges/blob/master/dist/findAtlasReviewChanges-0.0.4-py3-none-any.whl).

1. Install the application using this command line text `pip install findAtlasReviewChanges-0.0.4-py3-none-any.whl`

## Using

Warning, misuse of this utility can place a large demand on eBird.org servers which has a performance and cost impact on others and is not needed. You will be making the requests to eBird.org via a token you request from eBird.org using your eBird login credentials. According to eBird.org misuse of your key to access large amounts of data could result in eBird.org revoking your ability to access the data.

Request your key from [here](https://ebird.org/api/keygen). One you get it, save it as you will need it later.

Then from a command line, you can specify various command line parameters

type `python -m findAtlasReviewChanges --help` for parameters

Example

```batch
C:\directory>python -m findAtlasReviewChanges --user "Guy Babineau" --area "US-VA-003" --date "2018-04-01" --end "2018-04-14"
Reviewing Checklist from  2018-04-08 Bridlepath Yard
Reviewing Checklist from  2018-04-08 750 Bridlepath Drive, Earlysville, Virginia, US (38.126, -78.476)
Reviewing Checklist from  2018-04-08 Chris Greene Lake Dam Area
reshaw  Changed to  Possible  from  CF Carrying Food (Confirmed)
Reviewing Checklist from  2018-04-08 Chris Greene Lake
Reviewing Checklist from  2018-04-13 Bridlepath Yard
Reviewing Checklist from  2018-04-13 Chris Greene Lake

C:\directory>
```

### Optional - save your eBird API key in an environment variable

You can save your API key in an environment variable called EBIRDAPIKEY. If you don't know how, that's fine. You can still use it on the command line. This is done to prevent the API key being shared accidentally in example scripts created for the documentation.

## What it means

Some time after you enter your eBird checklist, automated and manual checks are performed on all checklists. If, for example, a breeding code is
entered outside of the breeding time period for the area, the breeding code is downgraded to 'observed.'

In the example above, the ebirder (me) entered a red-shouldered hawk carrying food. Since hawks will carry food, and not just for young, this should not be a confirmation unless there are other factors involved. Oops on my part. But the review caught the error.

But lets say that I had notes which otherwise established that this should me maintained as a confirmed code, I could add those notes, or perhaps change the code. A good example of where I think this could be done is that when 'Pair in suitable habitat' is used species at least superficially sexually monomorphic species such as Canada Goose, they are automatically downgraded to Observed. Since gender can also be established by voice, and perhaps behavior, a comment added to the observation may have been used by the atlas reviewer to keep the observation coded as 'Pair in suitable habitat.'

## How to fix

If desired, you can go to your observation in eBird and modify the checklist to change the code to the downgraded level, or add notes to better establish the code. No action means that the reviewer established code will be used.

## Developer Notes

[See details](docs\developernotes.md)

## Other

[Contributing](CONTRIBUTING.md)

[License](LICENSE.md)
