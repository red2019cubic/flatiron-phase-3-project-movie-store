import re
import time
from prettycli import red , blue, bright_green
from simple_term_menu import TerminalMenu
from models import Movie, Actor
import pyfiglet as pyg


class Cli():
    
    def __init__(self):
        current_owner = None
        
    def start(self):
        self.clear_screen(44)
        res= pyg.figlet_format("Welcome to TThe Movie Store", font="slant") 
        print(blue(res))
        options = ["View All Movies", "Search for movie by title", "search for actor by name", "Delete Movie", "Add Movie", "Delete Actor"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if options[menu_entry_index] == "View All Movies":
            print(self.handle_view_movies())
        else:
            self.exit()
            
    def clear_screen(self, lines):
        print("\n" * lines)
        
    def handle_view_movies(self):
        
        movies_list = Movie.view_all_movies()
        return movies_list
            
    def show_owner_options(self):
        options = ["My Toys", "New Toy", "Edit My Info", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        print(options[menu_entry_index])
        
    
    def exit(self):
        res= pyg.figlet_format("Bye! Thanks for visiting our Movie Store", font="slant") 
        print(res)
    
    
app = Cli()
app.start()