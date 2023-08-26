import re
import time
from prettycli import red, blue, bright_green, green, bright_yellow
from simple_term_menu import TerminalMenu
from models import Movie, Actor, MoviesActors
import pyfiglet as pyg


class Cli():

    def start(self):
        self.clear_screen(44)
        res = pyg.figlet_format("Welcome to TThe Movie Store", font="slant")
        print(blue(res))
        options = ["View All Movies", "View All Actors", "Add Movie", "Add Actor", "Delete Movie",
                   "Delete Actor", "Add Actor To Movie", "Search For Movie By Id", "Search For Actor By Id", "list movies by actor name", "Exit"]
        # terminal_menu = TerminalMenu(options)
        # menu_entry_index = terminal_menu.show()
        
        self.menu_option()
        option_id = eval(input("Select an option to continue: "))
        while options[option_id] != "Exit":

            if options[option_id] == "View All Movies":
                print(self.handle_view_movies())
                self.menu_option()
                option_id = eval(input("Select an option to continue: "))
                
            elif options[option_id] == "View All Actors":
                print(self.handle_view_actors())
                self.menu_option()
                option_id = eval(input("Select an option to continue: "))
            elif options[option_id] == "Add Movie":
                title = input("Enter the movie title: ")
                print(green("Saving " + title + " to DB......"))
                self.handle_add_movie(title)
                print(green("Record Created Successfully.."))
                self.menu_option()
                option_id = eval(input("Select an option to continue: "))
            elif options[option_id] == "Add Actor":
                name = input("Enter the actor name : ")
                print(green("Saving " + name + " to DB......"))
                time.sleep(2)
                self.handle_add_actor(name)
                print(green("Record Created Successfully.."))
                self.menu_option()
                option_id = eval(input("Select an option to continue: "))
            elif options[option_id] == "Delete Movie":
                id = eval(input("Enter the movie id : "))
                print(green("Deleting movie id number" +
                            str(id) + " record from DB......"))
                time.sleep(2)
                self.handle_delete_movie(id)
                print(red("Record Deleted Successfully.."))
                self.menu_option()
                option_id = eval(input("Select an option to continue: "))
            elif options[option_id] == "Delete Actor":
                id = eval(input("Enter the actor id : "))
                print(green("Deleting actor id number " +
                            str(id) + " record from DB......"))
                time.sleep(2)
                self.handle_delete_actor(id)
                print(red("Record Deleted Successfully.."))
                self.menu_option()
                option_id = eval(input("Select an option to continue: "))
            elif options[option_id] == "Add Actor To Movie":
                actor_id = eval(input("Enter the actor id : "))
                movie_id = eval(input("Enter the actor id : "))
                print(green("Adding actor id number " +
                            str(actor_id) + " to movie "))
                time.sleep(2)
                self.handle_add_actor_to_movie(actor_id, movie_id)
                print(green("Actor added Successfully.."))
                self.menu_option()
                option_id = eval(input("Select an option to continue: "))
            elif options[option_id] == "Search For Movie By Id":
                movie_id = input("Enter the movie id: ")
                print(green("Searching......."))
                time.sleep(2)
                print(green("Movie Found with the id " + str(movie_id)))
                print(self.handle_search_movie_by_id(movie_id))
                self.menu_option()
                option_id = eval(input("Select an option to continue: "))
            elif options[option_id] == "Search For Actor By Id":
                actor_id = input("Enter the actor id: ")
                print(green("Searching......."))
                time.sleep(2)
                print(green("Actor Found with the id " + str(actor_id)))
                print(self.handle_search_actor_by_id(actor_id))
                self.menu_option()
                option_id = eval(input("Select an option to continue: "))
            elif options[option_id] == "Exit":
                self.exit()
        self.exit()
    def menu_option(self):
        options = ["View All Movies", "View All Actors", "Add Movie", "Add Actor", "Delete Movie",
                   "Delete Actor", "Add Actor To Movie", "Search For Movie By Id", "Search For Actor By Id", "list movies by actor name", "Exit"]
        for i in range(len(options)):
            print(bright_yellow(str(i) + " : " + options[i]))
            

    def exit(self):
        res = pyg.figlet_format(
            "Bye! Thanks for visiting our movie store.", font="slant")
        print("Bye!")

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

    def handle_delete_actor(self, id):
        return Actor.delete_actor(id)

    def handle_add_actor_to_movie(self, actor_id, movie_id):
        return MoviesActors.add_actor_to_movie(actor_id, movie_id)

    def handle_search_movie_by_id(self, id):
        return Movie.search_movie_by_id(id)

    def handle_search_actor_by_id(self, id):
        return Actor.search_actor_by_id(id)

    def show_menu_options(self):
        options = ["View All Movies", "View All Actors", "Add Movie", "Add Actor", "Delete Movie",
                   "Delete Actor", "Add Actor To Movie", "Search For Movie By Id", "Search For Actor By Id", "list movies by actor name", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(options[menu_entry_index])

    def exit(self):
        res = pyg.figlet_format(
            "Bye! Thanks for visiting our Movie Store", font="slant")
        print(bright_green(res))


app = Cli()
app.start()
