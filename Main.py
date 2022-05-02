
import requests
import json
from parsel import Selector

r = requests.get('https://stackoverflow.com/feeds/tag?tagnames=python&sort=newest')

selector = Selector(text=r.text, type='xml')
selector.remove_namespaces()

entries = selector.xpath('//entry')

for entry in entries:
  dict = {
    'title': entry.xpath('title/text()').get(),
    'link': entry.xpath('link').attrib['href'],
  }
  print(dict)
