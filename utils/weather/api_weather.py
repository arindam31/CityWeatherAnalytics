"""Module to get weather data
"""
import math
import requests
from datetime import datetime, timedelta


KEY = 'f3817fcfa08a4d13a5206fbdae1a7aba'
weatherbit_url = "https://api.weatherbit.io/v2.0/history/daily"


def get_euclidian_distance(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371 * c
    return km



def get_date(str_date, day_delta=0, to_string=True):
    date_format = '%Y-%m-%d'
    if day_delta:
        date = datetime.strptime(str_date, date_format)
        final_date = date + timedelta(day_delta)
    else:
        final_date = datetime.strptime(str_date, date_format)

    if to_string:
        return final_date.strftime(date_format)

    return final_date


def get_temp_from_response(json_response):
    _data = json_response['data'][0]  # 0 since only 1 day data will be present
    max_temp = _data['max_temp']
    min_temp = _data['min_temp']
    date = _data['datetime']
    return max_temp, min_temp, date


def create_payload(**kwargs):
    payload = kwargs
    return payload


def calculate_mean_for_n_months(sum_highs, sum_lows, n):
    return (sum_highs - sum_lows)/n


def call_api(payload):
    """Call API and get data

    :return Json
    """
    data = requests.get(weatherbit_url, params=payload)
    assert data.status_code == 200, f"Something wrong. Error details: {data.json()['error']}"
    assert 'error' not in data.json().keys(), f'Problem: {data.json()}'
    return data.json()


if __name__ == '__main__':
    payload = create_payload(key=KEY, city_id='1261481', start_date='2020-12-1', end_date='2020-12-2')
    response = call_api(payload)
    from pprint import pprint
    pprint(response)


