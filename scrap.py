import requests
from bs4 import BeautifulSoup


baseUrl = 'https://www.helascaps.com/'
uri = "/all-products"

response = requests.get(baseUrl + uri)

if response.ok:
    swoup = BeautifulSoup(response.text, 'html.parser')
    balises = swoup.findAll("article", {"class": "product"})
    for balise in balises:
        #print(balise)
        titles = swoup.findAll("h3")
        prices = swoup.findAll("div", {"class": "price"})
        sizes = swoup.findAll("div", {"class": "add-to-cart-combination-item"})
        for size in sizes:
            if 'disabled' in size.get('class'):
                size.extract()
        '''
            if not size.has_attr('disabled'):
                print(size)
        balise.extract
        '''


  

