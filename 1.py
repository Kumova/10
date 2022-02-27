from pprint import pprint

import requests 

TOKEN = "2619421814940190"

class Person:
     def name_request():
        url = " https://superheroapi.com"
        params = {
           {"id" : 332, 'name': 'Hulk'},
           {"id" : 149, 'name': 'Captain America'}, 
           {"id" : 655, 'name': 'Thanos'}
        }
        response = requests.get_search_name(url, params=params, token=TOKEN)
        pprint(response)

     def get_intelligence_person(self):
        url = "https://superheroapi.com/api/access-token/search/name"
        response = requests.get(url, token=TOKEN)
        return response.json()

if __name__ == '__main__':
    person = Person()
    pprint(person.get_intelligence_person())