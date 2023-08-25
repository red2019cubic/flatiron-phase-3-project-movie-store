
from models import Movie, Actor, Movie_Actor
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import ipdb
import csv

engine = create_engine("sqlite:///db/movie_store.db")
Session = sessionmaker(bind=engine)
session = Session()
# ipdb.set_trace()


session.query(Movie).delete()
session.query(Actor).delete()
session.query(Movie_Actor).delete()

# For working with a csv file and retrieving json data


with open('movies.csv', 'r', encoding="ISO-8859-1") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    csv_reader.__next__()
    csv_reader.__next__()

    for row in csv_reader:
        for i in row:

            movie = Movie(
                year=row[0],
                length=row[1],
                title=row[2],
                subject=row[3],
                actor=row[4],
                actress=row[5],
                director=row[6],
                popularity=row[7],
                awards=row[8],
                image=row[9]
            )

            actor = Actor(
                name=row[4]
            )
        session.add(movie)
        session.add(actor)
        session.commit()
    for i in range(1, 1660, 1):
        movieactors = Movie_Actor( 

                                      movie_id = i,
                                      actor_id = i,
                                      )
                

        
        session.add(movieactors)
        session.commit()
