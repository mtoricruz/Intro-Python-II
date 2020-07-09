from room import Room
from player import Player
from item import Item
import textwrap
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
# to add items in room, can I append from the specific room key value ex: room['foyer'].append(item)
# the answer is no. there is no explicit method to append an item to a dict



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

game_items = ['mug', 'coin', 'sword', 'map']


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
possible_directions = ['n', 's', 'e', 'w']
# Write a loop that:
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game
while True:
    print('\n')
    print(player.location)
    action = input('\nAction: ').strip().lower().split()[0]
    action = action[0]
    
    if action == 'q':
        break

    if action in possible_directions:
        # check to see if we can go in that direction
        # if we can, go there
        player.try_direction(action)

        # Add item to room
        player.location.add_item_to_room(random.choice(game_items))

        # add item to player's inventory
        player.add_to_inventory(player.location.items[0], player.location)

    elif action == 'i':
        print('You have ', player.inventory, 'in your inventory')
        player.drop_item
