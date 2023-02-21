import requests
from bs4 import BeautifulSoup


baseUrl = 'https://genius.com'
uri = '/Booba-92i-veyron-lyrics'

response = requests.get(baseUrl + uri)

if response.ok:
    swoup = BeautifulSoup(response.text, 'html.parser')
    balises = swoup.findAll("div", {"class": "Lyrics__Container-sc-1ynbvzw-6 YYrds"})
    lyrics = []
    for balise in  balises:
        lyric = balise.findAll("span", {"class": "ReferentFragmentdesktop__Highlight-sc-110r0d9-1"})
        for l in lyric:
            print(l.text)
    
  

