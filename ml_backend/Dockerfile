FROM python:latest

WORKDIR /code

COPY ./splitted_models /code/splitted_models
COPY ./req.txt /code/req.txt
COPY ./* /code/.

RUN pip install -r /code/req.txt

CMD ["python3", "main.py"]
