import Toolkit
class PageWeb:
    def __init__(self, baseUrl, uri=''):
        self.baseUrl = baseUrl
        self.uri = uri    
        self.absoluteUri = uri
    
    def setUri(self, uri):
        self.uri = uri

    def getUrl(self):
        return self.baseUrl + self.uri
    
    def getMultipleElements(self, soup, tag, option=''):
        return soup.findAll(tag, option)
    
    def getElement(self, soup, tag, option=''):
        return soup.find(tag, option)
    
    def getInfosElement(self, soup):
        name = soup.find('h1', {'class': "medium-title"}).text
        price = soup.find('div', {'class': "price"}).text
        sizes = soup.find('div', {'class': "add-to-cart-combination-items"})
        try:
            divs = sizes.findAll('div')
            allSize = []
            for size in divs:
                allSize.append(size)
            sizesDispo = []
            for s in Toolkit.Toolkit.triTaillesDispos(allSize):
                sizesDispo.append(s.text)
        except:
            print(name + "has no sizes")
            sizesDispo = ''
        infos = [{
            'name': name,
            'price': price,
            'sizes': sizesDispo,
            'category': Toolkit.Toolkit.getCategories(self.absoluteUri)
        }]
        return infos