FROM python:3.11.3-slim-buster

# set work directory
WORKDIR /code


# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt

# copy project
COPY . /code/

CMD ["python3", "main.py"]
