import re
import time
from prettycli import red , blue, bright_green, green 
from simple_term_menu import TerminalMenu
from models import Movie, Actor, MoviesActors
import pyfiglet as pyg


class Cli():
   
        
    def start(self):
        self.clear_screen(44)
        res= pyg.figlet_format("Welcome to TThe Movie Store", font="slant") 
        print(blue(res))
        options = ["View All Movies", "View All Actors", "Add Movie", "Add Actor", "Delete Movie", "Delete Actor", "Add Actor To Movie", "Search For Movie By Id", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if options[menu_entry_index] == "View All Movies":
            print(self.handle_view_movies())
            self.show_menu_options()
        elif options[menu_entry_index] == "View All Actors":
            print(self.handle_view_actors())
            self.show_menu_options()
        elif options[menu_entry_index] == "Add Movie":
            title = input("Enter the movie title: ")
            print(title)
            print(Movie)
            print(green("Saving " + title + " to DB......"))
            self.handle_add_movie(title)
            print(green("Record Created Successfully.."))
            
            self.clear_screen(1)
            self.show_menu_options()
        elif options[menu_entry_index] == "Add Actor":
            name = input("Enter the actor name : ")
            print(green("Saving " + name + " to DB......"))
            time.sleep(2)
            self.handle_add_actor(name)
            print(green("Record Created Successfully.."))
            self.show_menu_options()  
        elif options[menu_entry_index] == "Delete Movie":
            id = eval(input("Enter the movie id : "))
            print(green("Deleting movie id number" + str(id) + " record from DB......"))
            time.sleep(2)
            self.handle_delete_movie(id)
            print(red("Record Deleted Successfully.."))
            self.show_menu_options() 
        elif options[menu_entry_index] == "Delete Actor":
            id = eval(input("Enter the actor id : "))
            print(green("Deleting actor id number " + str(id) + " record from DB......"))
            time.sleep(2)
            self.handle_delete_movie(id)
            print(red("Record Deleted Successfully.."))
            self.show_menu_options()   
        elif options[menu_entry_index] == "Add Actor To Movie":
            actor_id = eval(input("Enter the actor id : "))
            movie_id = eval(input("Enter the actor id : "))
            print(green("Adding actor id number " + str(actor_id) + " to movie "))
            time.sleep(2)
            self.handle_add_actor_to_movie(actor_id, movie_id)
            print(green("Actor added Successfully.."))
            self.show_menu_options()  
        elif options[menu_entry_index] == "Search For Movie By Id":
            movie_id = input("Enter the movie id: ")
            print(green("Searching......."))
            time.sleep(2)
            print(green("Movie Found with the id " + str(movie_id)))
            print(self.handle_search_movie_by_id(movie_id))
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
    def handle_add_movie(self, title):
        return Movie.add_movie(title)
    def handle_add_actor(self, name):
        return Actor.add_actor(name)
    def handle_delete_movie(self, id):
        return Movie.delete_movie(id)
    def handle_add_actor_to_movie(self, actor_id, movie_id):
        return MoviesActors.add_actor_to_movie(actor_id, movie_id)
    def handle_search_movie_by_id(self, id):
        return Movie.search_movie_by_id(id)
            
    def show_menu_options(self):
        options = ["View All Movies", "View All Actors", "Add Movie", "Add Actor", "Delete Movie", "Delete Actor", "Update Movie", "Update Actor", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(options[menu_entry_index])
        
    
    def exit(self):
        res= pyg.figlet_format("Bye! Thanks for visiting our Movie Store", font="slant") 
        print(bright_green(res))
    
    
app = Cli()
app.start()