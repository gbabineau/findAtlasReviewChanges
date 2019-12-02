FROM python:3

ADD setup.py .

RUN pip install .

CMD [ "python", "-m findAtlasReviewChanges --help ]