# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
#   Room class should have (self, name, description) attributes.
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description
        
        # allow rooms to hold multiple items
        self.items = []
    
    # add items to room
    def add_item_to_room(self, item):
        self.items.append(item)
        print(f"You found {self.items[0]}.")

#   Adding dunder string method to return fstring because without it
#   what is returned is {'outside': <room.Room object at 0x01DC8148>, etc.}
    def __str__(self):
        return f'{self.room_name}\n\n{self.room_description}'
    