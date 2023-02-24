from bs4 import BeautifulSoup
import requests
import Toolkit


class Scrapper:
    def __init__(self, page):
        self.page = page
    
    def swoup(self, url, process=''):
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            if process == '':
                return soup
            return process(soup)
        return []
    
    def getLinks(self, elems, name):
        rows = []
        field = [name]
        for el in elems:
            link = self.page.getElement(el, 'a').attrs['href']
            row = {}
            row[name] = link
            rows.append(row)
        Toolkit.Toolkit.fileWriter(name+'s.csv', field, rows )
        
    def getLinksFromOneElement(self, name):
        rows = []
        field = [name]
        links = self.page.getMultipleElements(self.soup, 'a')
        for link in links:
            row = {}
            row[name] = link.attrs['href']
            rows.append(row)
        Toolkit.Toolkit.fileWriter(name+'s.csv', field, rows )

    
    def getPage(self):
        return self.page
    
    def exec(self):
        self.soup = self.swoup(self.page.getUrl())
        elems = self.page.getMultipleElements(self.soup, "article", ({"class": "product"}))
        self.getLinks(elems, 'article')
        lignes = []
        for ligne in Toolkit.Toolkit.fileReader('articles.csv'):
            self.page.setUri(ligne['article'])
            lignes.extend(self.swoup(self.page.getUrl(), self.page.getInfosElement))
        return lignes
                
                
    def execUris(self):
        self.soup = self.swoup(self.page.getUrl())
        self.soup = self.page.getElement(self.soup, "div", ({'class': 'categories-list'}))
        self.getLinksFromOneElement("uri")
        
    def getUri(self, tag, options):
        self.soup = self.swoup(self.page.getUrl())
        self.soup = self.page.getElement(self.soup, tag, options)
        self.getLinksFromOneElement('a', )
        
        
    def getElements(self):
        return self.elements