import requests
from bs4 import BeautifulSoup
import csv


def swoup(url, process=''):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        if process == '':
            return soup
        return process(soup)
    return []

def getInfo(soup):
    name = soup.find('h1', {'class': "medium-title"}).text
    price = soup.find('div', {'class': "price"}).text
    sizes = soup.find('div', {'class': "add-to-cart-combination-items"})
    divs = sizes.findAll('div')

    allSize = []
    for size in divs:
        allSize.append(size)
    sizesDispo = []
    for s in triTaillesDispos(allSize):
        sizesDispo.append(s.text)
    
    infos = {
        'name': name,
        'price': price,
        'sizes': sizesDispo
    }
    info = [infos]
    return info
    

def triTaillesDispos(objects):
    for object in objects:
        if 'disabled' in object.get('class'):
            object.extract()
    return objects


def fileReader(file):
    result = []
    with open(file, 'r', encoding="UTF8", newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
           result.append(line) 
    return result

def fileWriter(file, fieldnames, data):
    with open(file, 'w', encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return fileReader(file)


baseUrl = 'https://www.helascaps.com'
uriAllProducts = "/all-products"

titles = []
prices = []
allSizes = []
sizes = []
rows = []

field = ["articles"]

endpoints = swoup(baseUrl + uriAllProducts)

articles = endpoints.findAll("article", ({"class": "product"}))
for article in articles:
    link = article.find("a").attrs['href']
    row = {}
    row['articles'] = link
    rows.append(row)
fileWriter('links.csv', field, rows )

lignes = []
for ligne in fileReader('links.csv'):
    lignes.extend(swoup(baseUrl + ligne['articles'], getInfo))

fields = ['name', 'price', 'sizes']
fileWriter("data.csv", fields, lignes)
