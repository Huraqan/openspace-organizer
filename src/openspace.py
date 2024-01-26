import os
from random import shuffle

from pandas import DataFrame

from src.table import Table

class OpenSpace:
    def __init__(self, table_count : int = 6, table_capacity : int = 4):
        """
        Defines an open space with "table_count" tables
        and "table_capacity" seats per table.
        """

        self.tables = [Table(table_capacity) for i in range(table_count)]
        self.table_count = table_count
        self.table_capacity = table_capacity
        self.room_capacity = table_count * table_capacity
        self.seated_people = 0
        self.people_kicked_out = 0
        self.surplus = []
    
    def organize(self, names : list[str]):
        """
        Randomly seats as many poeple from the list as possible.
        Remaining people will be kicked out!
        """

        shuffle(names)

        if len(names) > self.room_capacity:
            if input("\nToo many people in the room. Add a table?") == "y":
                self.tables.append(Table(self.table_capacity))
                self.room_capacity += self.table_capacity
                self.organize(names)
                return

            seatable = names[:self.room_capacity:]
            self.surplus = names[self.room_capacity::]
            self.people_kicked_out = len(self.surplus)

            print(
                f"\nSeating: {str(seatable)}\n" +
                f"\nGracefully kicking out: {str(self.surplus)}\n")
        else:
            seatable = names

            print("\nEverybody gets a seat.\n")

        for name in seatable:
            for table in self.tables:
                if not table.has_free_spot(): continue # Ruff says this is bad but I prefer to do this kind of condition check in one line, is it really that bad?

                table.assign_seat(name)
                self.seated_people += 1
                break
            
    
    def display(self):
        """Prints out all tables and their occupants"""

        info = "\nCURRENT DISTRIBUTION:"
        seats_left = 0

        for i, table in enumerate(self.tables):
            info += f"\n\nTable {i + 1}:"
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

        data_frame = DataFrame(data)
        data_frame.to_excel(filename, index = False)

        print(f"\nData stored to excel file at: {os.path.abspath(filename)}")