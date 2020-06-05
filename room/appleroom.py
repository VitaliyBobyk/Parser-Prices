import requests
from bs4 import BeautifulSoup as Bs

urls_new = ['-11-pro-max/', '-11-pro/', '-xs-max/', '-xs/', '-xr/', '-x/', '-8-plus/', '-8/', '-7-plus/']
urls_used = ['-11-pro-max-bu/', '-11-pro-bu/', '-xs-max-bu/', '-xs-bu/', '-xr-bu/', '-x-bu/', '-8-plus-bu/', '-8-bu/',
             '-7-plus-bu/']
pages = []


class AppleRoom:
    def new(self):
        f = open('room/new(room).txt', 'a')
        for x in urls_new:
            pages.append(requests.get('https://appleroom.ua/category/iphone' + x))
            for r in pages:
                pages.clear()
                html = Bs(r.content, 'html.parser')
                for el in html.select('div[itemprop="name"]'):
                    name = el.select('a')
                    for elem in html.select('.product-card__price'):
                        title = elem.select('.usd')
                        write = name[0].text + title[0].text
                    f.write(write)
        return f.close

    def used(self):
        f = open('room/used(room).txt', 'a')
        for x in urls_used:
            pages.append(requests.get('https://appleroom.ua/category/iphone' + x))
            for r in pages:
                pages.clear()
                html = Bs(r.content, 'html.parser')
                for el in html.select('div[itemprop="name"]'):
                    name = el.select('a')
                    for elem in html.select('.product-card__price'):
                        title = elem.select('.usd')
                        write = name[0].text + title[0].text
                    f.write(write)
        return f.close


