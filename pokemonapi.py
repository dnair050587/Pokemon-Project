import random
import requests
 
response1 = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(player1))
response2 = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(player2))
 
player1 = response1.json()
player2 = response2.json()
 
def print_card(card):  # this is temporary until ive checked
    
#game_stat

        print("Pokemon name: " + card.name)
        print("height: " + str(card.height))
        print("weight: " + str(card.weight))
        print("id: " + str(card.id))
        
# Generate a random number between 1-151 
    number = randint(1, 151)


category = input('Choose your game_stat (id, height, weight or speed): ')

#Checks the stats of the two players against each other and prints accordingly
    

if category == "height":
    if player1['height'] > player2['height']:
        print("You win the round!")
elif player1['height'] < player2['height']:
     print('You lose the round!')
elif player1['height'] == player2['height']:
     print('You draw! Play again')
     
category = input('Choose your game_stat (id, height, weight or speed): ')
    
    elif category == 'weight':
    if player1['weight'] > player2['weight']:
     print('You win!')
    elif player1['weight'] < player2['weight']:
     print('You lose!')
    elif player1['weight'] == player2['weight']:
     print('You draw! Play again')

    elif category == 'id':
    if player1['id'] > player2['id']:
     print('You win!')
    elif player1['id'] < player2['id']:
     print('You lose!')
    elif player1['id'] == player2['id']:
     print('You draw! Play again')
     category = input('Choose your stat (type id, height, weight or base experience): ')
    
elif category == 'speed':
    if player1['speed'] > player2['speed']:
     print('You win!')
    elif player1['speed'] < player2['speed']:
     print('You lose!')
    elif player1['base_experience'] == player2['speed']:
     print('You draw! Play again')
     category = input('Choose your stat (type id, height, weight or base experience): ') #do we need to add this eeach time??
    else:
     print('error! try again') #do we need this?
else:
 print('please select correct category option!')
   
            

# Start the game
print("~~ Welcome to the Pokemon Top Trumps Game! ~~ \n")
player1name = input("player1, please enter your name: ")
print("Hello " + player1name + ", get ready to enter the world of Pokemon!\n")
player2name = "Computer"
print("You are playing against " + player2name +  ", get ready...\n")


game = Game(player1, computer)

# Keep alternating turns until someone wins
# Whoever wins the round gets to pick another trump
game.create_deck(player1, computer)
while game.winner == None:
    game.player_turn()
    while game.player1.won:
        game.player_turn()
        if game.winner != None:
            break
    if game.winner == None:
        game.computer_turn()
        while game.player2.won:
            game.computer_turn()
        if game.winner != None:
            break

print("Game over!")