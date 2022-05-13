# Note: indent by 2 is for a better look.

import requests
import json
from parsel import Selector


def main():
  
  r = requests.get('https://stackoverflow.com/feeds/tag?tagnames=python&sort=newest')
  selector = Selector(text=r.text, type='xml')
  selector.remove_namespaces()
  entries = selector.xpath('//entry')
  list_of_entries = [] 

  for entry in entries:
    dict = {
    'title': entry.xpath('title/text()').get(),
    'link': entry.xpath('link').attrib['href'],
  }
  list_of_entries.append(dict)


  print(json.dumps(list_of_entries, indent=2))

if __name__ == '__main__':
  main()
