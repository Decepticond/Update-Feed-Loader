import requests
import json
from parsel import Selector

r = requests.get('https://stackoverflow.com/feeds/tag?tagnames=python&sort=newest')

selector = Selector(text=r.text, type='xml')
selector.remove_namespaces()

entries = selector.xpath('//entry')
