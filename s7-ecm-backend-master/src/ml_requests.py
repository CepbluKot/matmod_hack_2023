import httpx
import asyncio
import requests, json, httpx

from utils import columns_to_dict
from schema import MLInputX
URL = "http://192.168.222.3:5000/ml/predict"  # ML's module URL


def sendFilteredDataX(selected_json):
    parsed = []


    for obj in selected_json:
        pars = columns_to_dict(obj)
        pars['flight_datetime'] = str(pars['flight_datetime'])
        pars['flight_phase'] = str(pars['flight_phase'])
        parsed.append(pars)


    # headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(URL, json=(parsed))
    #
    return response


