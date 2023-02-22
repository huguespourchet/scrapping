import requests
from bs4 import BeautifulSoup


baseUrl = 'https://www.helascaps.com/'
uriAllProducts = "/all-products"



def swoup(url):
    response = requests.get(url)
    if response.ok:
        return BeautifulSoup(response.text, 'html.parser')
    return

def getEndPoint(endpoint, tags):
    return endpoint.findAll(tags)
    
def triTaillesDispos(objects):
    for object in objects:
        if 'disabled' in object.get('class'):
            object.extract()
    return objects

endpoints = swoup(baseUrl + uriAllProducts)

titles = []
prices = []
sizes = []

articles = getEndPoint(endpoints, ("article", {"class": "product"}))
for article in articles:
    titles.append(getEndPoint(endpoints, "h3"))
    prices.append(getEndPoint(endpoints, ("div", {"class": "price"})))
    allSizes = getEndPoint(endpoints, ("div", {"class": "add-to-cart-combination-item"}))
    sizes.append(triTaillesDispos(allSizes))

  

