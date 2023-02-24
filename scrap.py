import PageWeb
import Scrapper
import Toolkit

baseUrl = 'https://www.helascaps.com'

mainPage = PageWeb.PageWeb(baseUrl)
scrapperMain = Scrapper.Scrapper(mainPage)
scrapperMain.execUris()

lignes = []
for uri in Toolkit.Toolkit.fileReader('as.csv'):
    page = PageWeb.PageWeb(baseUrl, uri['a'])
    scrapperArticles = Scrapper.Scrapper(page)
    lignes.extend(scrapperArticles.exec())
fields = ['name', 'price', 'sizes', 'category']
Toolkit.Toolkit.fileWriter("data.csv", fields, lignes)
    
        
        