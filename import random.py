import random
my_card = random.randint(1, 200)
oponent_card = random.randint(1, 200)
import requests
url1 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(my_card) 
url2 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(oponent_card)
response1 = requests.get(url1)
response2 = requests.get(url2)
my_pokemon = response1.json()
oponent_pokemon = response2.json()
print('Your Pokemon is {}'. format(my_pokemon['name']))
print('id: {}'.format(my_pokemon['id']))
print('height: {}'.format(my_pokemon['height']))
print('weight: {}'.format(my_pokemon['weight']))
print('base experience: {}'.format(my_pokemon['base_experience']))
category = input('Choose your stat (type id, height, weight or base experience): ')
print("Your oponent's Pokemon is {}". format(oponent_pokemon['name']))
print('iD: {}'.format(oponent_pokemon['id']))
print('height: {}'.format(oponent_pokemon['height']))
print('weight: {}'.format(oponent_pokemon['weight']))
print('base experience: {}'.format(oponent_pokemon['base_experience']))
if category == 'height':
    if my_pokemon['height'] > oponent_pokemon['height']:
     print('You win!')
    elif my_pokemon['height'] < oponent_pokemon['height']:
     print('You lose!')
    elif my_pokemon['height'] == oponent_pokemon['height']:
     print('You draw! Play again')
     category = input('Choose your stat (type id, height, weight or base experience): ')
    else:
     print('error! try again')
elif category == 'weight':
    if my_pokemon['weight'] > oponent_pokemon['weight']:
     print('You win!')
    elif my_pokemon['weight'] < oponent_pokemon['weight']:
     print('You lose!')
    elif my_pokemon['weight'] == oponent_pokemon['weight']:
     print('You draw! Play again')
     category = input('Choose your stat (type id, height, weight or base experience): ')
    else:
     print('error! try again')
elif category == 'id':
    if my_pokemon['id'] > oponent_pokemon['id']:
     print('You win!')
    elif my_pokemon['id'] < oponent_pokemon['id']:
     print('You lose!')
    elif my_pokemon['id'] == oponent_pokemon['id']:
     print('You draw! Play again')
     category = input('Choose your stat (type id, height, weight or base experience): ')
    else:
     print('error! try again')
elif category == 'base experience':
    if my_pokemon['base_experience'] > oponent_pokemon['base_experience']:
     print('You win!')
    elif my_pokemon['base_experience'] < oponent_pokemon['base_experience']:
     print('You lose!')
    elif my_pokemon['base_experience'] == oponent_pokemon['base_experience']:
     print('You draw! Play again')
     category = input('Choose your stat (type id, height, weight or base experience): ')
    else:
     print('error! try again')
else:
 print('please select correct category option!')