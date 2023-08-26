import re
import time
from prettycli import red
from simple_term_menu import TerminalMenu
from models import Movie, Actor


class Cli():
    
    def __init__(self):
        current_owner = None
        
    def start(self):
        self.clear_screen(44)
        options = ["View All Movies", "Search for movie by title", "search for actor by name", "Delete Movie", "Add Movie", "Delete Actor"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if options[menu_entry_index] == "View All Movies":
            self.handle_view_movies()
        else:
            self.exit()
            
    def clear_screen(self, lines):
        print("\n" * lines)
        
    def handle_view_movies(self):
        title = input("Please enter your email:\n\n")
        
        if title in Movie:
            print("Find a user by email")
            
            
            self.show_owner_options()
            
        else:
            print(red("Invalid email. Please try again!"))
            time.sleep(2)
            self.start()
        
    def show_owner_options(self):
        options = ["My Toys", "New Toy", "Edit My Info", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        print(options[menu_entry_index])
        
    
    def exit(self):
        print("Bye!")
    
    
app = Cli()
app.start()