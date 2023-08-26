
from sqlalchemy import Integer, Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy.ext.associationproxy import association_proxy
Base = declarative_base()

# # # movie_actor = Table(
# #     "movies_actors", Base.metadata,
   
# #     Column('movie_id', ForeignKey('movie.id'), primary_key=True),
# #     Column('actor_id', ForeignKey('actor.id'), primary_key=True),
# #     extend_existing=True,
# # )

# class Movie_Actor(Base):
#     __tablename__ = "movies_actors"
    
#     id = Column(Integer, primary_key=True)
#     movie_id = Column(ForeignKey("movies.id"))
#     actor_id = Column( ForeignKey("actors.id"))

  
#     movie = relationship("Movie", back_populates="movies_actors")
#     actor = relationship("Actor", back_populates="movies_actors")

#     def __repr__(self):
#         return "<Movie_Actor " \
#             + f"id={self.id}, " \
#             + f"movie_id={self.movie_id}, " \
#             + f"actor_id={self.actor_id}, " \
#             + ">"

# class Movie(Base):
#     __tablename__ = "movies"

#     id = Column("id", Integer(), primary_key=True, autoincrement=True)
#     length = Column("length", Integer())
#     year = Column("year", Integer())
#     title = Column("title", String())
#     subject = Column("subject", String())
#     actor = Column("actor", String())
#     actress = Column("actress", String())
#     director = Column("director", String())
#     popularity = Column("popularity", Integer())
#     awards = Column("awards", String)
#     image = Column("image", String())

#     actors = association_proxy('movies_actors', 'actor',
#         creator=lambda a: Movie_Actor(actor=a))
#     movies_actors = relationship('Movie_Actor', back_populates='movie', cascade='all, delete-orphan')
    
   

#     def __repr__(self):
#         return "<Movie " \
#             + f"id={self.id}, " \
#             + f"year={self.year}, " \
#             + f"length={self.length}, " \
#             + f"title={self.title}, " \
#             + f"subject={self.subject}, " \
#             + f"actor={self.actor}, " \
#             + f"actress={self.actress}, " \
#             + f"director={self.director}, " \
#             + f"popularity={self.popularity}, " \
#             + f"awards={self.awards}, " \
#             + f"image={self.image}, " \
#             + ">"


# class Actor(Base):
#     __tablename__ = "actors"

#     id = Column("id", Integer(), primary_key=True)
#     name = Column("name", String(), nullable=False)
    
    
    
#     movies = association_proxy('movies_actors', 'movie',
#         creator=lambda a: Movie_Actor(movie=a))
#     movies_actors = relationship('Movie_Actor', back_populates='actor', cascade='all, delete-orphan')

#     def __repr__(self):
#         return "<Actor " \
#             + f"id={self.id}, " \
#             + f"name={self.name}" \
#             + ">"





# Declare the tables
# movies = Table('movies', Base.metadata,
#     Column('id', Integer, primary_key=True),
#     Column('title', String, nullable=False),
# )

# actors = Table('actors', Base.metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String, nullable=False),
# )

# Declare the relationship
class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    def __repr__(self):
        return "<Movie " \
            + f"id={self.id}, " \
            + f"year={self.year}, " \
            + f"length={self.length}, " \
            + f"title={self.title}, " \
            + f"subject={self.subject}, " \
            + f"actor={self.actor}, " \
            + f"actress={self.actress}, " \
            + f"director={self.director}, " \
            + f"popularity={self.popularity}, " \
            + f"awards={self.awards}, " \
            + f"image={self.image}, " \
            + ">"
   

# actors.py


class Actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

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