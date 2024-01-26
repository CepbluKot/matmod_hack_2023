from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import configparser
import os



""" Настройка FastApi  """
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.dirname(__file__)) + "/config_back.ini")
basedir = os.path.abspath(os.path.dirname(__file__))
