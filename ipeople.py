import requests
from bs4 import BeautifulSoup as BS
import cfscrape

scraper = cfscrape.create_scraper()

urls_new = ['iphone-11', 'iphone-11-pro', 'iphone-11-pro-max', 'iphone-xs-max', 'iphone-xs', 'iphone-x', 'iphone-xr', 'iphone-8-plus', 'iphone-8']
urls_used = ['bu-iphone-11', 'bu-iphone-11-pro', 'bu-iphone-11-pro-max', '-bu-iphone-xs-max', 'bu-iphone-xs', 'bu-iphone-xr', 'bu-iphone-x', 'bu-iphone-8-plus', 'bu-iphone-8', 'bu-iphone-7-plus','bu-iphone-7']
pages =[]
class Ipeople():
    def new(self):
        f = open('new(people).txt', 'a')
        for x in urls_new:
            pages.append(scraper.get("http://www.ipeople.in.ua/catalog/" + x))
            for r in pages:
                pages.clear()
                html = BS(r.content, 'html.parser')
                for el in html.select('.product'):
                    name = el.select('.fixed > a')
                    for el in html.select('.yui3-g.prices'):
                        title = el.select('.yui3-u-1-3.usd')
                        test = name[0].text + title[0].text
                    f.write(test + '\n')
        f.close
        return "Done"
    def used(self):
        f = open('used(people).txt', 'a')
        for x in urls_used:
            pages.append(scraper.get("http://www.ipeople.in.ua/catalog/" + x))
            for r in pages:
                pages.clear()
                html = BS(r.content, 'html.parser')
                for el in html.select('.product'):
                    name = el.select('.fixed > a')
                    for el in html.select('.yui3-g.prices'):
                        title = el.select('.yui3-u-1-3.usd')
                        test = name[0].text + ': ' + title[0].text
                    f.write(test + '\n')
        f.close
        return "Done"
