import requests
import json
import os

#function to get json data from url and save it to a file

def get_json(url, filename):
    response = requests.get(url)
    data = response.json()
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
        
#get parent dir of current file
parent_dir = os.path.dirname(os.path.abspath(__file__))
pp_dir = os.path.dirname(parent_dir)
to_save_dir = os.path.join(pp_dir, '_data')
#run function for url: https://zenodo.org/api/records/?page=1&size=10&communities=vliz-openscience&sort=mostrecent
filename = 'vliz-openscience.json'
get_json('https://zenodo.org/api/records/?page=1&size=10&communities=vliz-openscience&sort=mostrecent', os.path.join(to_save_dir, filename))
