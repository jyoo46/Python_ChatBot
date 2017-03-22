from lxml import html
import requests

# ARR = ["irvine", "ca"]
#
# page = requests.get('https://www.wunderground.com/us/'+ARR[1]+'/'+ARR[0])
# tree = html.fromstring(page.content)
# Temp = tree.xpath('//span[@class="wx-value"]/text()')
# Deg = tree.xpath('//span[@class="wx-unit"]/text()')
#
# print(Temp)


original = "EXAMPLE"
removed = original.replace("E", "")

print(removed)
