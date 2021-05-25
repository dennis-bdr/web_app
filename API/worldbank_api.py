import json
import requests
import pandas as pd


def return_json(url):
    """get a url's content in json format if successful else returns Error """
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return 'HTTPError: ' + str(e)
    try:
        json_obj = response.json()
    except json.decoder.JSONDecodeError as e:
        return 'JSONDecodeError: ' + str(e)
    return json_obj


def get_all_json_elements(base_url):
    """get all elements via from base_url in json format"""
    json_obj = return_json(base_url)
    if not type(json_obj) == list:
        return json_obj
    elements_count = json_obj[0]['total']
    json_obj_all = return_json('{}&per_page={}'.format(base_url, elements_count))
    return json_obj_all


get_countries = ['CH', 'CO']
countries_json = get_all_json_elements('http://api.worldbank.org/v2/country?format=json')
regions = get_all_json_elements('http://api.worldbank.org/v2/region?format=json')
df = pd.DataFrame(countries_json[1])