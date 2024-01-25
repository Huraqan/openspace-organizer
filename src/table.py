from typing import List

class Seat:
    def __init__(self, free : bool = True, occupant : str = "Empty seat"):
        """Seat object with a "free" boolean"""

        self.free = free
        self.occupant = occupant
    
    def set_occupant(self, name):
        """Seats a person if a spot is avaible"""
    
    def remove_occupant():
        """Removes a random person and returns their name"""
        

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
            if not seat.free: continue
            
            seat.occupant = name
            seat.free = False
            return
    
    def capacity_left(self):
        """Returns total capacity left at this table"""

        capacity_left = 0

        for seat in self.seats:
            if seat.free: capacity_left += 1
        
        return capacity_left
        


