# FROM directive instructing base image to build upon
FROM python:3.7

# create folder to contain app
RUN mkdir my_django
# set working directory
WORKDIR /my_django

# add requirements file first to leverage Docker cache
ADD ./requirements.txt /my_django/requirements.txt

# install require libraries
RUN pip install -r requirements.txt

# copy all files from current location to folder /my_django in docker container
ADD . /my_django

# set working directory
WORKDIR /my_django/dayoffmanager

# start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]