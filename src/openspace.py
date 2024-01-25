from src.table import Table
from typing import List
from random import shuffle
import pandas
import openpyxl
import os

class OpenSpace:
    def __init__(self, table_count : int = 6, table_capacity : int = 4):
        """Defines an open space with table_count amount of tables and a table_capacity worth of seats per table"""

        self.tables = [Table(table_capacity) for i in range(table_count)]
        self.table_count = table_count
        self.room_capacity = table_count * table_capacity
        self.people_kicked_out = 0
        self.surplus = []
    
    def organize(self, names : List[str]):
        """Randomly seats every person from the list of names until no longer possible. Remaining people will be kicked out!"""

        shuffle(names)

        if self.room_capacity < len(names):
            seatable = names[:self.room_capacity:]
            self.surplus = names[self.room_capacity::]
            self.people_kicked_out = len(self.surplus)
            print("\nToo many people in the room.\n\nSeating: " + str(seatable) + "\n\nGracefully kicking out: " + str(self.surplus))
        else:
            seatable = names

        for name in seatable:
            for table in self.tables:
                if not table.has_free_spot(): continue

                table.assign_seat(name)
                break
            
    
    def display(self):
        """Displays all tables and their occupants"""

        info = ""
        seats_left = 0

        for i, table in enumerate(self.tables):
            info += f"\n\nTable {i + 1}:\n"
            seats_left += table.capacity_left()
            
            for j, seat in enumerate(table.seats):
                info += f"\n    Seat {j + 1}: {seat.occupant}"
        
        info += f"\n\nPeople present: {self.room_capacity - seats_left}"
        info += f"\nTotal seats: {self.room_capacity}"
        info += f"\nSeats left: {seats_left}"
        info += f"\nPeople kicked out: {self.people_kicked_out} "
        info += str(self.surplus) if self.surplus else ""

        print(info + "\n")

    
    def store(self, filename):
        """Stores all data to an excel file"""

        data = {"Tables" : [], "Seats" : [], "Occupants" : []}

        for i, table in enumerate(self.tables):
            for j, seat in enumerate(table.seats):
                data["Tables"].append(f"Table {i + 1}")
                data["Seats"].append(f"Seat {j + 1}")
                data["Occupants"].append(seat.occupant)

        data_frame = pandas.DataFrame(data)
        data_frame.to_excel(filename, index = False)

        print(f"\nData stored to excel file at: {os.path.abspath(filename)}")
        print("\nThank you for using OrganX 1.0\n\n")