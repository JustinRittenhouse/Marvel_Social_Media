from config import Config
import requests
import hashlib

new_hero = input("What hero would you like to look up? ")
hash =  '123' + 'a6bd9aaa534fe2164a1e385f49b95de538b6bd0e' + '8d7f7343746ef834aac9c05d0593a60a'
api_link = f'http://gateway.marvel.com/v1/public/characters?name={new_hero}&ts=123&apikey=8d7f7343746ef834aac9c05d0593a60a&hash={(hashlib.md5(hash.encode())).hexdigest()}'

# for hero in requests.get(api_link).json()['data']['results']:
#     print(hero)

print(requests.get(api_link).json()['data']['results'][0]['name'])