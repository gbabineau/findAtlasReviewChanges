# Developer Notes

This relies on functionality based on [eBird API 2.0](https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest).

Coding was greatly simplified using these [useful Python access functions](https://github.com/ProjectBabbler/ebird-api).

Unfortunately, there do not appear to be public API calls which let you obtain checklists by user. So it gets checklist from an area (e.g. county) and scans for ones from a particular user.

Then it goes through the checklist to see if breeding codes were changed from what was entered. Some codes were obtained via examination of the returns of the API calls.

## creating the `whl` file

`python setup.py sdist bdist_wheel`

## Testing install in virtual environment

Create the virtual environment
`python -m virtualenv env`

Activate the virtual environment

`.\env\Scripts\activate`

Test the installation

```batch
mkdir temp
rem activate the virtual environment
.\env\Scripts\activate
pushd temp
rem install the package
pip uninstall findAtlasReviewChanges
pip install ..\dist\findAtlasReviewChanges-0.1.0-py3-none-any.whl
python -m findAtlasReviewChanges --user "Guy Babineau" --area "US-VA-003" --date "2018-04-08"
popd
rem Deactivate the virtual environment
deactivate
rd temp
```

## Running Tests

`pytest`

## Create a new release version with `Bump2version`

Here is how to `bump2version` to update the versions across all files and then create a new release

make sure you pip install wheel

```batch
bump2version patch
python setup.py sdist bdist_wheel
git push --tags
```

Then push and pull from remote!
