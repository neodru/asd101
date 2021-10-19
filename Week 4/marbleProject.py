#Proect: Find the Green Marble
#“Mariah recently started a marble collection

#Mariah is having trouble finding green marbles to add to her collection. '
#While on summer vacation, she discovered a marble store nearby that lets customers pick marbles to
#purchase from a secret bag. The catch to picking marbles from the bag is that Mariah is not allowed
#to look inside the bag, and she can pick only five marbles from the bag per day. If she chooses not
#to keep a marble that is picked, she must place the marble back into the bag. Since Mariah wants one green marble,
#she wants to stop picking marbles once a green marble is found.”

#Create a program that keeps track of how many times Mariah has picked a marble from the bag and confirms
#whether the marble picked is green. If Mariah picks a green marble from the bag, add the marble to
#Mariah's collection and remove the marble from the secret bag. Once Mariah picks a green marble,
#she should stop picking marbles from the secret bag. Keep in mind that Mariah is only allowed to pick five marbles
#from the secret bag per day.”


#she wants 1 green marble.

import random

#Create Mariah's Collection

collection = ['red', 'pink', 'orange', 'red', 'pink', 'yellow', 'pink', 'yellow']

secret_bag = ['pink', 'blue', 'green', 'orange', 'red', 'purple', 'green', 'blue', 'blue', 'red', 'green', 'purple', 'yellow', 'red', 'pink', 'red', 'green', 'yellow']


marbles_chosen = []

tries_remaining = 5

for x in range(6):
    if tries_remaining> 0:
        selection = random.choice(secret_bag)
        marbles_chosen.append(selection)
        tries_remaining -= 1
        if selection == 'green':
            collection.append(selection)
            secret_bag.remove(selection)
            if ('green' in collection):
                print(f"""Awesome! You found a green marble.
If you would like another marble,
you have {tries_remaining} pick(s) left.""")
                break
    else:
        print("""Sorry, you are out of tries. Please come back tomorrow and try again!""")
print(f'Here are all the marbles that were chosen: {marbles_chosen}')
