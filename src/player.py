# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, inventory=[]):
        self.inventory = inventory
        self.location = location
    
    # tries to move the player in the specified direction
    def try_direction(self, action):
        # check the player's current location an dsee if there's
        # a room in the specified direction
        # if there is, move them to that room
        # else print a message saying "you can't go there" and
        # not move the player
        attribute = action + '_to'

        # Python has method 'hasattr' which allows us to check if a class has an attribute
        if hasattr(self.location, attribute):
            # use getattr to fetch the value associated with the attribute
            # update our player's location with the fetched room
            self.location = getattr(self.location, attribute)
        else:
            print("You can't go there ):")
    
    # Add Items
    def add_to_inventory(self, item, room):
        #Take item from a room
        item_taken = input(f"You may take the {item} by entering `take [item name]`\n")

        # Using .split() method to turn the input into a list 
        # that way we can access index 0 and 1 by saying == 'command' and item_name in room.items list
        split_item_taken = item_taken.split(' ')

        if split_item_taken[0] == 'take' and split_item_taken[1] in room.items:
            self.inventory.append(split_item_taken[1])
        else:
            print(f'\nYou leave the item there')

        if len(self.inventory) >= 1:
            print(f"\n You are carrying {self.inventory} in your inventory.\n")

    # Drop Items
    def drop_item(self):
        item_dropped = input('You can drop an item by entering `drop [item name]`')

        split_item_dropped = item_dropped.split(' ')

        if split_item_dropped[0] == 'drop' and split_item_dropped[1] in self.inventory:
            self.inventory.remove(split_item_dropped[1])
            print(f'You dropped {split_item_dropped}')
    

        

    
