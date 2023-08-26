from models import Movie, Actor, MoviesActors
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import ipdb

engine = create_engine("sqlite:///db/movie_store.db")
Session = sessionmaker(bind=engine)
session = Session()
session.query(Movie).delete()
session.query(Actor).delete()
session.query(MoviesActors).delete()

# movies
movie1 = Movie(title='The Shawshank Redemption')
movie2 = Movie(title='The Godfather')
movie3 = Movie(title='The Dark Knight')
movie4 = Movie(title='Tie me up!')
movie5 = Movie(title='Jaws')
movie6 = Movie(title='Die Hard')
movie7 = Movie(title='The Irish man')
session.add_all([movie1, movie2, movie3, movie4, movie5, movie6, movie7])
session.commit()
# actors
actor1 = Actor(name='Antonio Banderas')
actor2 = Actor(name='Morgan Freeman')
actor3 = Actor(name='Al Pacino')
actor4 = Actor(name='Robert Dinero')
actor5 = Actor(name='Bruce Willis')
actor6 = Actor(name='Julia Robert')
actor7 = Actor(name='Ben Aflak')

session.add_all([actor1, actor2, actor3, actor4, actor5, actor6, actor7])
session.commit()

# relationships between movies and actors
movies_actors1 = MoviesActors(movie_id=movie1.id, actor_id=actor1.id)
movies_actors2 = MoviesActors(movie_id=movie1.id, actor_id=actor2.id)
movies_actors3 = MoviesActors(movie_id = movie7.id, actor_id=actor3.id)
movies_actors4 = MoviesActors(movie_id = movie7.id, actor_id=actor4.id)
movies_actors5 = MoviesActors(movie_id = movie6.id, actor_id=actor5.id)
movies_actors6 = MoviesActors(movie_id = movie6.id, actor_id=actor6.id)
movies_actors7 = MoviesActors(movie_id = movie5.id, actor_id=actor7.id)

session.add_all([movies_actors1, movies_actors2, movies_actors3, movies_actors4, movies_actors5, movies_actors6, movies_actors7])
session.commit()
