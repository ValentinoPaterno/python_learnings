# # While
# x = 10
# while x > 5:
#     print(x)
#     x -= 1# Muestra cuando la condicion es falsa
# # Use of "Break"
# x = 1
# while x < 10:
#     print(x)
#     if x == 5:
#         break
#     x += 1
# # Use of "Continue" -> It's used for skip an iteration
# x = 1
# while x <= 5: # -> Imprime todo menos el 2
#     if x == 2:
#         x += 1
#         continue
#     print(x)
#     x += 1

# # For Loop -> Is used for iterating over a sequence (list, tuple, dictionary, set or a string)
# numbers = [0,1,2,3,4,5]
# for num in numbers:
#     print(num)
# # String
# language = "Python"
# for letter in language:
#     print(letter)
# # Tuple
# numbers = (0,1,2,3,4,5)
# for num in numbers:
#     print(num)
# # Dictionary -> looping gives you the key of the dictionary
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
# for key in person:
#     print(key)

# for key, value in person.items():
#     print(key, value) # this way we get both keys and values printed out
# Loops in sets
# it_companies = {'Facebook','Twitter', 'Instagram', 'Google'}
# for company in it_companies:
#     print(company)
# # Use of Break and Continue in loops
# numbers = (0,1,2,3,4,5)
# for num in numbers:
#     if num == 2:
#         break
#     print(num)

# numbers = (0,1,2,3,4,5)
# for num in numbers:
#     if num == 2:
#         continue
#     print(num)
# # Range Function The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end).
# lst = list(range(11))
# print(lst)
# st = set(range(1,11))
# print(st)

# even_numbers = list(range(0,11,2))
# print(even_numbers) 
# odd_numbers = set(range(1,11,2))
# print(odd_numbers)

# for number in range(0,11,2):
#     print(f"{number} is an even number.")
# for number in range(1,11,2):
#     print(f"{number} is an odd number.")

# # Nested For loop
# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)

# -------------------- Ejercicios --------------------
# # 1
# for i in range(0,11):
#     print(i)
# i=0
# while i <= 10:
#     print(i)
#     i += 1
# # 2
# for i in range(10,-1,-1):
#     print(i)
# i = 10
# while i >= 0:
#     print(i)
#     i -= 1
# # 3
# for i in range(0,8):
#     print("#"*i)
# # 4
# renglon = ""
# for x in range(0,8):
#     for i in range(0,8):
#         renglon += "# "
#     print(renglon)
#     renglon = ""
# # 5
# for i in range(11):
#     print(f"{i} x {i} = {i*i}")
# # 6
# list = ["Python", "Numpy", "Django", "Pandas", "Flask"]
# for language in list:
#     print(language)
# # 7 y 8
# for i in range(0,101,2):
#     print(i)
# for i in range(1,101,2):
#     print(i)
# # Level 2
# # 1
# result = 0
# for i in range(1,101):
#     result += i 
# else:
#     print("The sum of all number is:",result)
# # 2
# odds = 0
# even = 0
# for i in range(1,101):
#     if(i % 2 == 0):
#         even += i
#     else: 
#         odds += i 
# else:
#     print("The sum of all even numbers is: ", even, ". And the sum of all odds is:",odds)
# # Level 3
# # 1
# countries = [
#     'Afghanistan',
#     'Albania',
#     'Algeria',
#     'Andorra',
#     'Angola',
#     'Antigua and Barbuda',
#     'Argentina',
#     'Armenia',
#     'Australia',
#     'Austria',
#     'Azerbaijan',
#     'Bahamas',
#     'Bahrain',
#     'Bangladesh',
#     'Barbados',
#     'Belarus',
#     'Belgium',
#     'Belize',
#     'Benin',
#     'Bhutan',
#     'Bolivia',
#     'Bosnia and Herzegovina',
#     'Botswana',
#     'Brazil',
#     'Brunei',
#     'Bulgaria',
#     'Burkina Faso',
#     'Burundi',
#     'Cambodia',
#     'Cameroon',
#     'Canada',
#     'Cape Verde',
#     'Central African Republic',
#     'Chad',
#     'Chile',
#     'China',
#     'Colombi',
#     'Comoros',
#     'Congo (Brazzaville)',
#     'Congo',
#     'Costa Rica',
#     "Cote d'Ivoire",
#     'Croatia',
#     'Cuba',
#     'Cyprus',
#     'Czech Republic',
#     'Denmark',
#     'Djibouti',
#     'Dominica',
#     'Dominican Republic',
#     'East Timor (Timor Timur)',
#     'Ecuador',
#     'Egypt',
#     'El Salvador',
#     'Equatorial Guinea',
#     'Eritrea',
#     'Estonia',
#     'Ethiopia',
#     'Fiji',
#     'Finland',
#     'France',
#     'Gabon',
#     'Gambia, The',
#     'Georgia',
#     'Germany',
#     'Ghana',
#     'Greece',
#     'Grenada',
#     'Guatemala',
#     'Guinea',
#     'Guinea-Bissau',
#     'Guyana',
#     'Haiti',
#     'Honduras',
#     'Hungary',
#     'Iceland',
#     'India',
#     'Indonesia',
#     'Iran',
#     'Iraq',
#     'Ireland',
#     'Israel',
#     'Italy',
#     'Jamaica',
#     'Japan',
#     'Jordan',
#     'Kazakhstan',
#     'Kenya',
#     'Kiribati',
#     'Korea, North',
#     'Korea, South',
#     'Kuwait',
#     'Kyrgyzstan',
#     'Laos',
#     'Latvia',
#     'Lebanon',
#     'Lesotho',
#     'Liberia',
#     'Libya',
#     'Liechtenstein',
#     'Lithuania',
#     'Luxembourg',
#     'Macedonia',
#     'Madagascar',
#     'Malawi',
#     'Malaysia',
#     'Maldives',
#     'Mali',
#     'Malta',
#     'Marshall Islands',
#     'Mauritania',
#     'Mauritius',
#     'Mexico',
#     'Micronesia',
#     'Moldova',
#     'Monaco',
#     'Mongolia',
#     'Morocco',
#     'Mozambique',
#     'Myanmar',
#     'Namibia',
#     'Nauru',
#     'Nepal',
#     'Netherlands',
#     'New Zealand',
#     'Nicaragua',
#     'Niger',
#     'Nigeria',
#     'Norway',
#     'Oman',
#     'Pakistan',
#     'Palau',
#     'Panama',
#     'Papua New Guinea',
#     'Paraguay',
#     'Peru',
#     'Philippines',
#     'Poland',
#     'Portugal',
#     'Qatar',
#     'Romania',
#     'Russia',
#     'Rwanda',
#     'Saint Kitts and Nevis',
#     'Saint Lucia',
#     'Saint Vincent',
#     'Samoa',
#     'San Marino',
#     'Sao Tome and Principe',
#     'Saudi Arabia',
#     'Senegal',
#     'Serbia and Montenegro',
#     'Seychelles',
#     'Sierra Leone',
#     'Singapore',
#     'Slovakia',
#     'Slovenia',
#     'Solomon Islands',
#     'Somalia',
#     'South Africa',
#     'Spain',
#     'Sri Lanka',
#     'Sudan',
#     'Suriname',
#     'Swaziland',
#     'Sweden',
#     'Switzerland',
#     'Syria',
#     'Taiwan',
#     'Tajikistan',
#     'Tanzania',
#     'Thailand',
#     'Togo',
#     'Tonga',
#     'Trinidad and Tobago',
#     'Tunisia',
#     'Turkey',
#     'Turkmenistan',
#     'Tuvalu',
#     'Uganda',
#     'Ukraine',
#     'United Arab Emirates',
#     'United Kingdom',
#     'United States',
#     'Uruguay',
#     'Uzbekistan',
#     'Vanuatu',
#     'Vatican City',
#     'Venezuela',
#     'Vietnam',
#     'Yemen',
#     'Zambia',
#     'Zimbabwe',
# ]
# new_countries = []
# for country in countries:
#     if "land" in country:
#         new_countries.append(country)
# # 2
# fruits = ["banana", "orange", "mango", "lemon"]
# i = len(fruits) - 1
# fruits_reversed = []
# while i >= 0:
#     fruits_reversed.append(fruits[i])
#     i -= 1
# print(fruits_reversed)
