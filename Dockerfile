FROM python:3

RUN pip install dist\findAtlasReviewChanges-0.0.4-py3-none-any.whl

CMD [ "python", "-m findAtlasReviewChanges --help ]