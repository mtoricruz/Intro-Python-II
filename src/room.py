# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
#   Room class should have (self, name, description) attributes.
    def __init__(self, name, description):
        self.name = name
        self.description = description
#   Adding dunder string method to return fstring because without it
#   what is returned is {'outside': <room.Room object at 0x01DC8148>, etc.}
    def __str__(self):
        return f'Room: {self.name} \n\nDescription: {self.description}'