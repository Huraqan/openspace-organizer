from typing import List

class Seat:
    def __init__(self, free : bool, occupant : str):
        """Seat object with a "free" boolean, """
        self.free = free
        self.occupant = occupant
    
    def set_occupant(self, name):
        """Seats a person if a spot is avaible"""
    
    def remove_occupant():
        """Removes a random person and returns their name"""

class Table:
    def __init__(self, capacity : int, seats : List[Seat]):
        self.capacity = capacity
        self.seats = seats
    
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
            if seat.free:
                seat.occupant = name
                seat.free = False
    
    def capacity_left(self):
        capacity_left = 0

        for seat in self.seats:
            if seat.free: capacity_left += 1
        
        return capacity_left
        


