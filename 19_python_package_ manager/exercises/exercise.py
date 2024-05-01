import requests
# romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# response = requests.get(romeo_and_juliet)
# print(response)

# 2
response = requests.get('https://api.thecatapi.com/v1/breeds')
print(response)

cats = response.json()
# print(cats)

for cat in cats:
    print(cat['weight']['metric'])
