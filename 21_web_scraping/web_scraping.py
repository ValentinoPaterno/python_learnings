import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.edu/ml/datasets.php'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
print(soup.title)