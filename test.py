import numpy as np
from lxml import html
import requests
import urllib.request

#
page = requests.get('D:/git/Python_ChatBot/map.html')
tree = html.fromstring(page.content)
wordT = tree.xpath('//div[@style="overflow: auto;"]/text()')


print(wordT)
