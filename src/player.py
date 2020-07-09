# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location):
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
