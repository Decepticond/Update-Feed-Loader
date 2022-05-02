import requests
import json
from parsel import Selector

r = requests.get('https://stackoverflow.com/feeds/tag?tagnames=python&sort=newest')
print (r.text) 
