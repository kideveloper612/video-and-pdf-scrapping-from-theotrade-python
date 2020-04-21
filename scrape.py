import os
from bs4 import BeautifulSoup
import requests
import json


def main():
    url = 'https://theotrade.com/member-home/'
    header = {
        'user-agent': 'mozila/5.0'
    }
    login_data = {
        'log': 'psaponjac@yahoo.it',
        'pwd': 'GI$1H!4Y'
    }
    # s = requests.Session()
    # s.post('https://theotrade.com/member-login/', login_data, headers=header)
    # res = s.request(method='GET', url=url, headers=header)
    # print(res.text)

    session = requests.Session()
    session.headers.update({'User-Agent': "myapp1,0"})
    mydata = json.dumps(login_data)
    response = session.post('https://theotrade.com/member-login/', data=mydata)
    session.get('https://theotrade.com/member-login/')
    res = session.post('https://theotrade.com/member-login/')
    print(res.text)
    # soup = BeautifulSoup(s.request(method='GET', url=url, headers=header))
    # features = soup.find_all('div', {'class': 'image-caption'})
    # print(len(features))


if __name__ == "__main__":
    main()