"""
--- Web Scrapping --- 
For collecting data -> We have to know how to scrape data
• Web Scrapping -> Process of extracting data from websites 
and storing it on a local machine or database
• We will use beatifulsoup and requests package to scrape data.
"""
import requests

from bs4 import BeautifulSoup
url = 'https://www.scrapethissite.com/pages/simple/'

response = requests.get(url)
# print(response.status_code)

# Using beautifulsoup to parse content from the page

content = response.content
soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.body)

countries = soup.find_all('div', {'class': 'country'})
dict_countries = {}

for country in countries:
    parsed_country = ""
    parsed_capital = ""
    for leter in country.h3.get_text():
        if leter in (" ", "\n"):
            continue
        parsed_country += leter
    for leter in country.span.get_text():
        if leter in (" ", "\n"):
            continue
        parsed_capital += leter
    
    parsed_population = country.find('span', {'class': 'country-population'})
    parsed_area = country.find('span', {'class': 'country-area'})
    dict_countries[parsed_country] = {
        "capital": parsed_capital,
        "population": int(parsed_population.get_text()),
        "area": float(parsed_area.get_text())
    } 

print(dict_countries["Andorra"])

