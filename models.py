
from sqlalchemy import Integer, Column, String, Table, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.orm import sessionmaker
import ipdb
engine = create_engine("sqlite:///db/movie_store.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    
    @classmethod
    def view_all_movies(cls):
        return session.query(Movie).all()
    @classmethod
    def search_movie_by_title(cls, title):
        return session.query(Movie).filter_by(title=title).one()

    def __repr__(self):
        return "<Movie " \
            + f"id={self.id}, " \
            + f"title={self.title}, " \
            + ">"
   
# ipdb.set_trace()
# actors.py


class Actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String)


    @classmethod
    def view_all_actors(cls):
        return session.query(Actor).all()
        
    def __repr__(self):
        return "<Actor " \
            + f"id={self.id}, " \
            + f"name={self.name}" \
            + ">"
# movies_actors.py


class MoviesActors(Base):
    __tablename__ = 'movies_actors'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    actor_id = Column(Integer, ForeignKey('actors.id'))

    movie = relationship('Movie', backref='actors')
    actor = relationship('Actor', backref='movies')