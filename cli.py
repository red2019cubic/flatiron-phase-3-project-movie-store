import re
import time
from prettycli import red , blue, bright_green
from simple_term_menu import TerminalMenu
from models import Movie, Actor
import pyfiglet as pyg


class Cli():
   
        
    def start(self):
        self.clear_screen(44)
        res= pyg.figlet_format("Welcome to TThe Movie Store", font="slant") 
        print(blue(res))
        options = ["View All Movies", "View All Actors", "Search for movie by title", "search for actor by name", "Delete Movie", "Add Movie", "Delete Actor", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if options[menu_entry_index] == "View All Movies":
            print(self.handle_view_movies())
            self.show_menu_options()
        elif options[menu_entry_index] == "View All Actors":
            print(self.handle_view_actors())
            self.show_menu_options()
        else:
            self.exit()
    
            
    def clear_screen(self, lines):
        print("\n" * lines)
        
    def handle_view_movies(self):
        movies_list = Movie.view_all_movies()
        return movies_list
    
    def handle_view_actors(self):
        actors_list = Actor.view_all_actors()
        return actors_list
            
    def show_menu_options(self):
        options = ["View All Movies","View All Actors", "Search for movie by title", "search for actor by name", "Delete Movie", "Add Movie", "Delete Actor", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(options[menu_entry_index])
        
    
    def exit(self):
        res= pyg.figlet_format("Bye! Thanks for visiting our Movie Store", font="slant") 
        print(bright_green(res))
    
    
app = Cli()
app.start()