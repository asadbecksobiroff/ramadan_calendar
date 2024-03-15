from bs4 import BeautifulSoup
import requests
from datetime import datetime

def get_times(code):
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
    
    # proxiesDict = {
    #               "http": "http://10.10.1.10:3128",
    #               "https": "https://10.10.1.10:1080",
    #             }
    # PROXY_URL = "http://proxy.server:3128"
    
    month = datetime.now().month
    city = locations[code]
    url = f'https://islom.uz/vaqtlar/{city}/{month}'
    # r = requests.get(url, proxies=proxiesDict)
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    times = soup.find_all("td", {"class": "bugun"})
    saharlik = times[0].text
    iftorlik = times[1].text
    
    return saharlik, iftorlik

