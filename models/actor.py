from .base import Base
from sqlalchemy import Table, Integer, ForeignKey, Column, String
from sqlalchemy.orm import relationship
from .movie_actor import movie_actor
class Actor(Base):
    __tablename__ = "actors"

    id = Column("id", Integer(), primary_key=True)
    first_name = Column("first_name", String(), nullable=False)
    last_name = Column("last_name", String(), nullable=False)
    dob = Column("date_of_birth", Integer(), nullable=False)
    movies = relationship("movies", secondary=movie_actor, backref="actors")

    def __repr__(self):
        return "<Actor " \
            + f"id={self.id}, " \
            + f"first_name={self.first_name}" \
            + f"last_name={self.last_name}" \
            + f"dob={self.dob}" \
            + ">"



