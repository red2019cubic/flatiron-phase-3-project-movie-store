
from sqlalchemy import Integer, Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

movie_actor = Table(
    "movies_actors", Base.metadata,
    Column("id", Integer, primary_key=True),
    Column('movie_id', Integer, ForeignKey('movie.id')),
    Column('actor_id', Integer, ForeignKey('actor.id')),
)


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
    
    actors = relationship("Actor", secondary=movie_actor, back_populates="movies")

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
    

    movies = relationship("Movie", secondary=movie_actor, back_populates="actors")

    def __repr__(self):
        return "<Actor " \
            + f"id={self.id}, " \
            + f"name={self.name}" \
            + ">"
