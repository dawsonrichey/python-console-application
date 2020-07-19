from urllib.request import urlopen
from bs4 import BeautifulSoup

default_user = 'dawson89'

html = urlopen(f'https://teamtreehouse.com/{default_user}')
soup = BeautifulSoup(html.read(), 'html.parser')

total_points_section = soup.find('div', {'class': 'contained points-container'})
print(total_points_section.prettify())



