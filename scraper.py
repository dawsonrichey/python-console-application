from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

html = urlopen('https://teamtreehouse.com/dawson89')
soup = BeautifulSoup(html.read(), 'html.parser')

# print(soup)

# print(soup.prettify())

# print(soup.title)
#
# print(soup.div)
#
# divs = soup.findAll('div', {'class': 'featured'})
# for div in divs:
#     print(div)

# divs = soup.find('div', {'class': 'featured'})
# print(divs)

total_points_section = soup.find('div', {'class': 'contained points-container'})
print(total_points_section.prettify())



