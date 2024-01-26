from src.openspace import OpenSpace
import json
from time import sleep
from random import choice

if __name__ == "__main__":
    def load_room() -> OpenSpace:
        """
        Returns a new OpenSpace object.
        Will attempt to load a configuration from a "config.json" file.
        If no file is found, a room with default settings is returned.
        """

        try:
            with open("config.json", "r") as jsonfile:
                config = json.load(jsonfile)
                print("\nConfig file was found. Loading settings..." +
                      f"\nUsing {config["table_count"]} tables and " +
                      f"{config["table_capacity"]} seats per table.")
                
                return create_room(config["table_count"], config["table_capacity"])
                
        except FileNotFoundError:
            print("\nNo config file was found. Using default settings...")

            return create_room()

    def create_room(table_count: int = 6, table_capacity: int = 4) -> OpenSpace:
        """
        Creates and returns a room with 6 tables and 4 seats per table by default.

        - table_count: number of tables
        - table_capacity: number of seats per table
        """

        print(
            f"\n\nCreating a new room with {table_count} tables with {table_capacity} seats per table, a total of {table_capacity * table_count} seats!")

        return OpenSpace(table_count, table_capacity)

    def load_colleagues(colleagues_filepath : str):
        """
        Takes a room and fills it with people from a list.
        The list must be a txt file with names separated by a comma.

        - colleagues_filepath: a valid filepath to the txt file
        """

        try:
            with open(colleagues_filepath, "r") as file:
                names = file.read().split(",")
                print(f"\nColleagues file found, colleagues names: {names}")
                return names
        except FileNotFoundError:
            print("\nColleagues file not found...")
            return None

    
    print("\n\nWELCOME TO SEATFINDER 2024 - THE BEST TOOL TO GET PEOPLE SEATED\n")
    
    colleagues = load_colleagues(input("Provide a valid txt filename for attendance list: "))

    if not colleagues:
        print(
            "\nNo people were found... Nobody came to the event?" +
            "\nMaybe people don't like me?\nNah! It must be the bad weather..." +
            "\nYeah! That's it! It's misty outside..." +
            "\nPeople don't like mist..." +
            "\n\nIt's the mist.\n\n")
        exit()
    
    current_room = load_room() if input("\nUse JSON config file? \"y\": ") == "y" else create_room()

    current_room.organize(colleagues)

    current_room.display()

    current_room.store("room_seating_distribution.xlsx")


    final_kickout_message = "\nOkay so everyone's got a seat! Would you like to start kicking out random people one by one? After all, you've got ALL the power!!! (y)"

    if input(final_kickout_message) == "y":
        print("\nHere we goooooooo! MOUHAHAHAHAHAHAHA!!!")
        
        while True:
            table = choice(current_room.tables)
            name = table.remove_random_occupant()

            if name:
                print(f"Kicked out {name}!")
                current_room.seated_people -= 1
                sleep(1.0)

            if current_room.seated_people == 0:
                print("\nFinally!\nEveryone's gone.\nNow you can get back to doing that *thing* you always love doing when nobody is around hehehe...\n\n")
                
                break
            
    print("\nThank you for using SEATFINDER 2024\n\n")




