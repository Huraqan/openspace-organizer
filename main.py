from src.table import Table
from src.openspace import OpenSpace
from typing import List
import pandas
import json

if __name__ == "__main__":

    def setup_room(colleagues_filepath, table_count = 6, table_capacity = 4):
        """A valid filename is required for the list of people. Sets up a room with default table count of 6 and seats per table of 4."""

        print(f"\n\nCreating a new room with {table_count} tables with {table_capacity} seats per table, a total of {table_capacity * table_count} seats!")

        try:
            with open(colleagues_filepath, "r") as file:
                names = file.read().split(",")
                print(f"\nColleagues file found, people names: {names}")
        except:
            print("\nFile not found or unable to open...")
            return

        room = OpenSpace(table_count, table_capacity)
        room.organize(names)

        return room

    def create_new_room(colleagues_filepath):
        try:
            with open("config.json", "r") as jsonfile:
                config = json.load(jsonfile)
                print(f"\nConfig file was found. Loading settings... Using {config["table_count"]} tables and {config["table_capacity"]} seats per table.")
                room = setup_room(colleagues_filepath, config["table_count"], config["table_capacity"])
        except:
            print("\nNo config file was found. Using default settings...")
            room = setup_room(colleagues_filepath)

        room.display()
        room.store("test.xlsx")
    

    print("\n\nWELCOME TO ORGANX - THE BEST TOOL TO GET PEOPLE SEATED\n")

    create_new_room("colleagues2.txt")




