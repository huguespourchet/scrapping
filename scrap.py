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
allSizes = []
sizes = []

articles = getEndPoint(endpoints, ("article", {"class": "product"}))
for article in articles:
    print(article)
    titles.append(getEndPoint(article, "h3"))
    print(getEndPoint(article, ("div", {"class": "price"})))
    print(article.findAll("div", {"class": "price"}))
    

    for price in prices:
        print()
        print(price)
    
    allSizes.append(getEndPoint(article, ("div", {"class":"add-to-cart-combination-item"})))
    #sizes.append(triTaillesDispos(allSizes))
    exit()
