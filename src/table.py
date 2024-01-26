from random import choice

class Seat:
    def __init__(self, free : bool = True, occupant : str = "Empty seat"):
        """Seat object which can have an occupant, defined by a string."""
        self.free = free
        self.occupant = occupant
    
    def set_occupant(self, name):
        """Seats a person if a spot is avaible"""
        self.occupant = name
        self.free = False
    
    def remove_occupant(self):
        """Removes and returns a person's name"""
        temp_name = self.occupant
        self.occupant = "Empty seat"
        self.free = True
        return temp_name
        

class Table:
    def __init__(self, capacity : int):
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]
    
    def has_free_spot(self):
        """Returns True or False if a spot is available"""

        for seat in self.seats:
            if seat.free:
                return True
        return False
    
    def assign_seat(self, name : str):
        """Assigns a free spot to a person"""

        if not self.has_free_spot():
            print(f"No seats left for {name}, get out!")
            return
        
        for seat in self.seats:
            if not seat.free:
                continue
            
            seat.set_occupant(name)
            return
    
    def capacity_left(self):
        """Returns total capacity left at this table"""
        
        return sum([int(seat.free) for seat in self.seats])
    
    def remove_random_occupant(self):
        """Removes a random person from the table and returns their name."""
        
        occupied_seats = [seat for seat in self.seats if not seat.free]
        
        if occupied_seats:
            return choice(occupied_seats).remove_occupant()
        else:
            return None

        


