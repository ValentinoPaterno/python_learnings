import requests
# url = 'https://www.w3.org/'
# response = requests.get(url) # opening a network and fetching data

# print(response)
# print(response.status_code) # status code, success: 200
# print(response.headers) # headers information
# print(response.text) # gives all the text from the page

# From an API
poke_api = 'https://pokeapi.co/api/v2/pokemon/ditto'
response = requests.get(poke_api)
print(response.status_code)
pokemones = response.json()
print(pokemones["abilities"])
first_ability_of_abilities = pokemones["abilities"][0]['ability']['url']
print(first_ability_of_abilities)
