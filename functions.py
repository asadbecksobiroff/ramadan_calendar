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


def get_day_info():
    today = get_date()
    day = today.day
    month = today.month
    week_index = today.weekday()
    month_list = ['yanvar', 'fevral', 'mart', 'aprel', 'may', 'iyun', 'iyul', 'avgust', 'sentyabr', 'oktyabr', 'noyabr', 'dekabr']
    week = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba', 'yakshanba']
    
    info = f"{day}-{month_list[month-1]}, {week[week_index]}"
    return info


def get_times(city):
    locations = {
        'andijon': 1,
        "farg'ona": 37,
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
        return data[city_code]['saharlik'], data[city_code]['iftorlik']+':00'
    
    month = today.month
    url = f'https://islom.uz/vaqtlar/{city_code}/{month}'
    try:
        r = requests.get(url)
    except:
        r = None
    
    if r:    
        soup = BeautifulSoup(r.text, 'html.parser')
        times = soup.find_all("td", {"class": "bugun"})
        if len(times) == 2:
            saharlik = times[0].text
            iftorlik = times[1].text
        
            data[city_code]['date'] = today.date()
            data[city_code]['saharlik'] = saharlik
            data[city_code]['iftorlik'] = iftorlik
            
            return saharlik, iftorlik
        return False
    else:
        return False
