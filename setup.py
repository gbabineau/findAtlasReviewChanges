from setuptools import setup

url = ""
version = "0.0.3"
readme = open('README.md').read()

setup(
    name="findAtlasReviewChanges",
    packages=["findAtlasReviewChanges"],
    version=version,
    description="Review ones own VABBA2 data for changes made by Atlas Reviews",
    long_description=readme,
    include_package_data=True,
    author="Guy L. Babineau",
    author_email="guy.babineau@gmail.com",
    url=url,
    install_requires=['ebird-api','python-dateutil'],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
