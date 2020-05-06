import requests
from bs4 import BeautifulSoup as BS

urls_new = ['-11-pro-max/', '-11-pro/', '-xs-max/', '-xs/', '-xr/', '-x/', '-8-plus/', '-8/', '-7-plus/']
urls_used = ['-11-pro-max-bu/', '-11-pro-bu/', '-xs-max-bu/', '-xs-bu/', '-xr-bu/', '-x-bu/', '-8-plus-bu/', '-8-bu/', '-7-plus-bu/']
pages =[]
class AppleRoom():
    def new(self):
        f = open('new.txt', 'a')
        for x in urls_new:
            pages.append(requests.get('https://appleroom.ua/category/iphone' + x))
            for r in pages:
                pages.clear()
                html = BS(r.content, 'html.parser')
                for el in html.select('div[itemprop="name"]'):
                    name = el.select('a')
                    for el in html.select('.product-card__price'):
                        title = el.select('.usd')
                        test = name[0].text + title[0].text
                    f.write(test)

        f.close
        return "Done"

    def used(self):
        f = open('used.txt', 'a')
        for x in urls_used:
            pages.append(requests.get('https://appleroom.ua/category/iphone' + x))
            for r in pages:
                pages.clear()
                html = BS(r.content, 'html.parser')
                for el in html.select('div[itemprop="name"]'):
                    name = el.select('a')
                    for el in html.select('.product-card__price'):
                        title = el.select('.usd')
                        test = name[0].text + title[0].text
                    f.write(test)

        f.close
        return "Done"

