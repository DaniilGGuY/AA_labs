import requests as re
import bs4

filename = "urls.txt"
url = "https://www.povareschka.ru"
list_catalogs = set()
list_links = set()

page = re.get(url)
bs = bs4.BeautifulSoup(page.content, 'html.parser')
for groups in bs.find_all('menu')[1:-2]:
    for link in groups.find_all('a'):
        ref = link.get('href')
        if 'recepty' in ref:
            list_catalogs.add(url + ref)

for part in list_catalogs:
    page = re.get(part)
    bs = bs4.BeautifulSoup(page.content, 'html.parser')
    for groups in bs.find_all('main'):
        for link in groups.find_all('a'):
            ref = link.get('href')
            if 'recepty' in ref:
                list_links.add(url + ref)

f = open(filename, "w")
for i in list_links:
    f.write(i + '\n')
