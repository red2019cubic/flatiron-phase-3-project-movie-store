from .base import Base
from sqlalchemy import Table, Integer, ForeignKey, Column, String
from sqlalchemy.orm import relationship
from .movie_actor import movie_actor

class Movie(Base):
    __tablename__ = "movies"

    id = Column("movie_id", Integer(), primary_key=True)
    title = Column("title", String(), nullable=False)
    year = Column("year", Integer(), nullable=False)
    actors = relationship("actors", secondary=movie_actor, backref="The_movies")

    def __repr__(self):
        return "<Movie " \
            + f"id={self.id}, " \
            + f"title={self.title}, " \
            + f"year={self.year}, " \
            + ">"
