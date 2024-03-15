from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta


data = {
    1: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    4: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    5: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    9: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    14: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    15: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    16: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    18: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    25: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    27: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    37: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    39: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    74: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
    78: {
        'date': None,
        'saharlik': None,
        'iftorlik': None
    },
}


def get_date():
    today = datetime.now()
    todayGMT5 = today + timedelta(hours=5)
    return todayGMT5


def get_times(city):
    locations = {
        'andijon': 1,
        'fergana': 37,
        'buxoro': 4,
        'jizzah': 9,
        'urganch': 78,
        'namangan': 15,
        'navoiy': 14,
        'qarshi': 25,
        'nukus': 16,
        'samarqand': 18,
        'guliston': 5,
        'termiz': 74,
        'toshkent': 27,
        'rishton': 39,
    }
        
    
    today = get_date()
    city_code = locations[city]
    
    if data[city_code]['date'] == today.date():
        return data[city_code]['saharlik'], data[city_code]['iftorlik']
    
    month = today.month
    url = f'https://islom.uz/vaqtlar/{city_code}/{month}'
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    times = soup.find_all("td", {"class": "bugun"})
    saharlik = times[0].text
    iftorlik = times[1].text
    
    data[city_code]['date'] = today.date()
    data[city_code]['saharlik'] = saharlik
    data[city_code]['iftorlik'] = iftorlik
        
    return saharlik, iftorlik
