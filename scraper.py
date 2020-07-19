from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://teamtreehouse.com/dawson89')
soup = BeautifulSoup(html.read(), 'html.parser')

total_points_section = soup.find('div', {'class': 'contained points-container'})
print(total_points_section.prettify())



