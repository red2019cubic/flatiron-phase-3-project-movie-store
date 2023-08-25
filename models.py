
from sqlalchemy import Integer, Column, String, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# movie_actor = Table(
#     "movies_actors", Base.metadata,
   
#     Column('movie_id', ForeignKey('movie.id'), primary_key=True),
#     Column('actor_id', ForeignKey('actor.id'), primary_key=True),
#     extend_existing=True,
# )

class Movie_Actor(Base):
    __tablename__ = "movie_actor"
    id = Column("id", Integer, primary_key=True)
    movie_id = Column("movie_id", Integer,ForeignKey("movie.id"))
    actor_id = Column("actor_id", Integer, ForeignKey("actor.id"))
  
    movie = relationship("Movie", back_populates="actors")
    actor = relationship("Actor", back_populates="movies")

class Movie(Base):
    __tablename__ = "movie"

    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    length = Column("length", Integer())
    year = Column("year", Integer())
    title = Column("title", String())
    subject = Column("subject", String())
    actor = Column("actor", String())
    actress = Column("actress", String())
    director = Column("director", String())
    popularity = Column("popularity", Integer())
    awards = Column("awards", String)
    image = Column("image", String())

    actors = relationship("Movie_Actor", back_populates="movie")
    
    # actors = relationship("Actor", secondary=movie_actor, back_populates="movies")

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


class Actor(Base):
    __tablename__ = "actor"

    id = Column("id", Integer(), primary_key=True)
    name = Column("name", String(), nullable=False)
    
    movies = relationship("Movie_Actor", back_populates="actor")

    # movies = relationship("Movie", secondary=movie_actor, back_populates="actors")

    def __repr__(self):
        return "<Actor " \
            + f"id={self.id}, " \
            + f"name={self.name}" \
            + ">"



###########################################################################################

# class Movie_Actor(Base):
#     __tablename__ = "movie_actor"
#     movie_id = Column(ForeignKey("movie.id"), primary_key=True)
#     actor_id = Column(ForeignKey("actor.id"), primary_key=True)
  
#     movie = relationship("Movie", back_populates="actors")
#     actor = relationship("Ator", back_populates="movies")


# class Parent(Base):
#     __tablename__ = "left_table"
#     id = Column(Integer, primary_key=True)
#     children = relationship("Association", back_populates="parent")


# class Child(Base):
#     __tablename__ = "right_table"
#     id = Column(Integer, primary_key=True)
#     parents = relationship("Association", back_populates="child")