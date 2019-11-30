from setuptools import setup

url = ""
version = "0.0.0"
readme = open('README.md').read()

setup(
    name="reviewVABBA2data",
    packages=["reviewVABBA2data"],
    version=version,
    description="Review ones own VABBA2 data for changes made by Atlas Reviews",
    long_description=readme,
    include_package_data=True,
    author="Guy L. Babineau",
    author_email="guy.babineau@gmail.com",
    url=url,
    install_requires=[],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
