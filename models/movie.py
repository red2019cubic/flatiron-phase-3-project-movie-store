from .base import Base
from sqlalchemy import Table, Integer, ForeignKey, Column, String
from sqlalchemy.orm import relationship
from .movie_actor import movie_actor

class Movie(Base):
    __tablename__ = "movies"

    id = Column("id", Integer(), primary_key=True)
    year = Column("year", Integer(), nullable=False)
    length = Column("length", Integer(), nullable=False)
    title = Column("title", String(), nullable=False)
    subject = Column("subject", String(), nullable=False)
    actor = Column("actor", String(), nullable=False)
    actress = Column("actress", String(), nullable=False)
    director = Column("director", String(), nullable=False)
    popularity = Column("popularity", Integer(), nullable=False)
    awards = Column("awards", bool, nullable=False)
    image = Column("image", String(), nullable=False)
    actors = relationship("actors", secondary=movie_actor, backref="movies")

    def __repr__(self):
        return "<Movie " \
            + f"id={self.id}, " \
            + f"title={self.title}, " \
            + f"year={self.length}, " \
            + f"year={self.year}, " \
            + f"year={self.subject}, " \
            + f"year={self.actor}, " \
            + f"year={self.actress}, " \
            + f"year={self.director}, " \
            + f"year={self.popularity}, " \
            + f"year={self.awards}, " \
            + f"year={self.image}, " \
            + ">"
