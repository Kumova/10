from pprint import pprint

import requests 

TOKEN = "2619421814940190"


def name_request():
    url = " https://superheroapi.com"
    params = {"id" : 332, "id" : 149, "id" : 655}
    headers = {"Authorization": "secret - token - 2619421814940190"}
    response = requests.get_name(url, params=params, headers=headers)
    pprint(response)

