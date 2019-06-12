import requests
from bs4 import BeautifulSoup
import re

resp = requests.get('https://db-ip.com/185.50.232.92')
soup = BeautifulSoup(resp.text, 'html.parser')
   

result = soup.find_all('td')

print (len(result[8].text))

